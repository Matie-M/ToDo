# TaskFlow - Modern To-Do App

A beautiful, modern to-do application built with React, FastAPI, and MongoDB. Manage your tasks efficiently with categories, due dates, and smart filtering.

![TaskFlow App](https://img.shields.io/badge/Status-Production%20Ready-green)
![React](https://img.shields.io/badge/React-19.0-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green)
![MongoDB](https://img.shields.io/badge/MongoDB-4.5-green)

## ✨ Features

### Core Features
- 📝 **Create Tasks** - Add tasks with title, description, due date, and category
- ✏️ **Edit Tasks** - Update any task details through an intuitive modal
- ✅ **Toggle Completion** - Mark tasks as complete/incomplete with a single click
- 🗑️ **Delete Tasks** - Remove tasks with confirmation dialog
- 🎨 **Category System** - Organize tasks with color-coded categories:
  - 💼 Work (Blue)
  - 👤 Personal (Purple)
  - 🛒 Shopping (Pink)
  - 💚 Health (Green)
  - 📋 Other (Gray)

### Smart Filtering
- **Status Filters**: View All Tasks, Active Only, or Completed Only
- **Category Filters**: Filter by specific categories
- **Combine Filters**: Mix status and category filters for precise task views

### Visual Feedback
- 📅 **Due Date Indicators**:
  - 🔴 Overdue tasks highlighted in red
  - 🟠 Tasks due today/tomorrow in orange
  - ⚪ Future tasks in neutral gray
- 🎉 **Toast Notifications** for all actions
- 🌈 **Modern, Colorful UI** with smooth animations
- 📱 **Responsive Design** for all screen sizes

## 🚀 Getting Started

### Prerequisites

- Node.js (v16 or higher)
- Python 3.11+
- MongoDB (local or remote instance)
- Yarn package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd taskflow-app
   ```

2. **Backend Setup**
   ```bash
   cd backend
   
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Configure environment variables
   cp .env.example .env
   # Edit .env and set your MONGO_URL
   
   # Start backend server
   uvicorn server:app --host 0.0.0.0 --port 8001 --reload
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   
   # Install dependencies
   yarn install
   
   # Configure environment variables
   cp .env.example .env
   # Edit .env and set REACT_APP_BACKEND_URL
   
   # Start frontend server
   yarn start
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8001
   - API Docs: http://localhost:8001/docs

## 🏗️ Project Structure

```
taskflow-app/
├── backend/
│   ├── server.py              # FastAPI application
│   ├── requirements.txt       # Python dependencies
│   └── .env                   # Backend environment variables
├── frontend/
│   ├── src/
│   │   ├── App.js            # Main application component
│   │   ├── App.css           # Global styles
│   │   └── components/
│   │       ├── TaskForm.js   # Task creation form
│   │       ├── TaskList.js   # Task list container
│   │       ├── TaskItem.js   # Individual task component
│   │       ├── FilterBar.js  # Filtering controls
│   │       ├── EditModal.js  # Task editing modal
│   │       ├── EmptyState.js # Empty state component
│   │       └── ui/           # Shadcn/ui components
│   ├── package.json          # Node dependencies
│   └── .env                  # Frontend environment variables
├── design_guidelines.md      # Design system documentation
├── plan.md                   # Project plan and phases
└── README.md                 # This file
```

## 🔧 Configuration

### Backend Environment Variables (.env)

```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=todo_app
CORS_ORIGINS=*
```

### Frontend Environment Variables (.env)

```env
REACT_APP_BACKEND_URL=http://localhost:8001
```

## 📡 API Endpoints

### Tasks

- `GET /api/tasks` - Get all tasks (with optional filters)
  - Query params: `status` (all|active|completed), `category` (Work|Personal|Shopping|Health|Other)
- `POST /api/tasks` - Create a new task
- `PUT /api/tasks/{task_id}` - Update a task
- `PATCH /api/tasks/{task_id}/toggle` - Toggle task completion
- `DELETE /api/tasks/{task_id}` - Delete a task

### Example Request

```bash
# Create a task
curl -X POST http://localhost:8001/api/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project proposal",
    "description": "Finish Q1 project proposal",
    "due_date": "2025-01-15T00:00:00Z",
    "category": "Work"
  }'
```

## 🎨 Design System

### Color Palette

- **Primary**: Teal (#14B8A6) - Main brand color
- **Secondary**: Coral (#FF6F61) - Accents
- **Success**: Mint Green (#6EE7B7) - Completed tasks
- **Warning**: Orange (#FB923C) - Due soon
- **Error**: Red (#EF4444) - Overdue tasks

### Typography

- **Headings**: Space Grotesk (Modern, geometric)
- **Body**: Inter (Highly readable, UI-optimized)

### Components

- Built with [shadcn/ui](https://ui.shadcn.com/)
- Styled with [Tailwind CSS](https://tailwindcss.com/)
- Icons from [Lucide React](https://lucide.dev/)

See [design_guidelines.md](./design_guidelines.md) for complete design system documentation.

## 🧪 Testing

### Backend Tests

```bash
cd backend
pytest
```

### Frontend Tests

```bash
cd frontend
yarn test
```

### Manual Testing Checklist

- [ ] Create task with all fields
- [ ] Edit task details
- [ ] Mark task as complete/incomplete
- [ ] Delete task with confirmation
- [ ] Filter by status (All/Active/Completed)
- [ ] Filter by category
- [ ] Verify due date colors (overdue/today/future)
- [ ] Check category badge colors
- [ ] Test empty states
- [ ] Verify toast notifications

## 🚢 Deployment

### Backend (FastAPI)

**Option 1: Docker**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8001"]
```

**Option 2: Platform as a Service**
- Deploy to Heroku, Railway, Render, or similar
- Set environment variables
- Configure MongoDB connection string

### Frontend (React)

**Build for production:**
```bash
cd frontend
yarn build
```

Deploy the `build/` folder to:
- Vercel
- Netlify
- AWS S3 + CloudFront
- GitHub Pages
- Any static hosting service

**Important**: Update `REACT_APP_BACKEND_URL` to point to your production backend URL.

## 🛠️ Tech Stack

### Frontend
- **React 19** - UI framework
- **Axios** - HTTP client
- **date-fns** - Date utilities
- **Sonner** - Toast notifications
- **shadcn/ui** - Component library
- **Tailwind CSS** - Styling
- **Lucide React** - Icons

### Backend
- **FastAPI** - Web framework
- **Pydantic** - Data validation
- **PyMongo** - MongoDB driver
- **Uvicorn** - ASGI server
- **python-dotenv** - Environment variables

### Database
- **MongoDB** - NoSQL database

## 📝 Data Model

### Task Schema

```javascript
{
  "id": "uuid-string",
  "title": "string",
  "description": "string",
  "due_date": "ISO 8601 datetime",
  "category": "Work | Personal | Shopping | Health | Other",
  "completed": "boolean",
  "created_at": "ISO 8601 datetime",
  "updated_at": "ISO 8601 datetime"
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Design inspiration from modern task management apps
- Built with [shadcn/ui](https://ui.shadcn.com/) components
- Icons by [Lucide](https://lucide.dev/)

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: [your-email@example.com]

---

**Made with ❤️ using React, FastAPI, and MongoDB**