from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional, List
from dotenv import load_dotenv
import os
import uuid

# Load environment variables
load_dotenv()

app = FastAPI()

# MongoDB setup
MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    raise ValueError("MONGO_URL environment variable is not set")

client = MongoClient(MONGO_URL)
db = client['todo_app']
tasks_collection = db['tasks']

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Helper functions
def serialize_doc(doc):
    if doc and "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc

def serialize_docs(docs):
    return [serialize_doc(doc) for doc in docs]

# Pydantic models
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = ""
    due_date: Optional[datetime] = None
    category: str = Field(..., pattern="^(Work|Personal|Shopping|Health|Other)$")

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    category: Optional[str] = Field(None, pattern="^(Work|Personal|Shopping|Health|Other)$")
    completed: Optional[bool] = None

class TaskResponse(BaseModel):
    id: str
    title: str
    description: str
    due_date: Optional[datetime]
    category: str
    completed: bool
    created_at: datetime
    updated_at: datetime

# Routes
@app.get("/")
def read_root():
    return {"message": "To-Do App API"}

@app.get("/api/tasks", response_model=List[TaskResponse])
def get_tasks(
    status: str = Query("all", pattern="^(all|active|completed)$"),
    category: Optional[str] = Query(None, pattern="^(Work|Personal|Shopping|Health|Other)$")
):
    """Get all tasks with optional filtering by status and category"""
    query = {}
    
    # Filter by status
    if status == "active":
        query["completed"] = False
    elif status == "completed":
        query["completed"] = True
    
    # Filter by category
    if category:
        query["category"] = category
    
    tasks = list(tasks_collection.find(query).sort("created_at", -1))
    
    # Convert to response format
    result = []
    for task in tasks:
        result.append({
            "id": task["id"],
            "title": task["title"],
            "description": task.get("description", ""),
            "due_date": task.get("due_date"),
            "category": task["category"],
            "completed": task["completed"],
            "created_at": task["created_at"],
            "updated_at": task["updated_at"]
        })
    
    return result

@app.post("/api/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    """Create a new task"""
    now = datetime.now(timezone.utc)
    task_id = str(uuid.uuid4())
    
    task_dict = {
        "id": task_id,
        "title": task.title,
        "description": task.description or "",
        "due_date": task.due_date,
        "category": task.category,
        "completed": False,
        "created_at": now,
        "updated_at": now
    }
    
    tasks_collection.insert_one(task_dict)
    
    return TaskResponse(**task_dict)

@app.put("/api/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: str, task: TaskUpdate):
    """Update an existing task"""
    existing_task = tasks_collection.find_one({"id": task_id})
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    update_data = {k: v for k, v in task.model_dump().items() if v is not None}
    
    if update_data:
        update_data["updated_at"] = datetime.now(timezone.utc)
        tasks_collection.update_one({"id": task_id}, {"$set": update_data})
    
    updated_task = tasks_collection.find_one({"id": task_id})
    
    return TaskResponse(
        id=updated_task["id"],
        title=updated_task["title"],
        description=updated_task.get("description", ""),
        due_date=updated_task.get("due_date"),
        category=updated_task["category"],
        completed=updated_task["completed"],
        created_at=updated_task["created_at"],
        updated_at=updated_task["updated_at"]
    )

@app.patch("/api/tasks/{task_id}/toggle", response_model=TaskResponse)
def toggle_task(task_id: str):
    """Toggle task completion status"""
    existing_task = tasks_collection.find_one({"id": task_id})
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    new_completed = not existing_task["completed"]
    now = datetime.now(timezone.utc)
    
    tasks_collection.update_one(
        {"id": task_id},
        {"$set": {"completed": new_completed, "updated_at": now}}
    )
    
    updated_task = tasks_collection.find_one({"id": task_id})
    
    return TaskResponse(
        id=updated_task["id"],
        title=updated_task["title"],
        description=updated_task.get("description", ""),
        due_date=updated_task.get("due_date"),
        category=updated_task["category"],
        completed=updated_task["completed"],
        created_at=updated_task["created_at"],
        updated_at=updated_task["updated_at"]
    )

@app.delete("/api/tasks/{task_id}", status_code=204)
def delete_task(task_id: str):
    """Delete a task"""
    result = tasks_collection.delete_one({"id": task_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)