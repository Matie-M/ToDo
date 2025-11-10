# TaskFlow - Quick Start Guide

## Prerequisites

Before you begin, ensure you have:
- ✅ Python 3.11+ installed
- ✅ Node.js 16+ installed
- ✅ MongoDB running (local or cloud)
- ✅ Yarn package manager

## Quick Setup (5 minutes)

### Option 1: Automated Setup (Recommended)

**Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

**Windows:**
```cmd
setup.bat
```

### Option 2: Manual Setup

**Step 1: Backend Setup**
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and set MONGO_URL
```

**Step 2: Frontend Setup**
```bash
cd frontend

# Install dependencies
yarn install

# Configure environment
cp .env.example .env
# Edit .env and set REACT_APP_BACKEND_URL
```

## Running the Application

### Start Backend
```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

### Start Frontend
```bash
cd frontend
yarn start
```

## Access Points

- 🌐 **Frontend**: http://localhost:3000
- 🔌 **Backend API**: http://localhost:8001
- 📚 **API Documentation**: http://localhost:8001/docs
- 🔍 **API Explorer**: http://localhost:8001/redoc

## First Steps in the App

1. Click **"Add Task"** button
2. Fill in:
   - Title (required)
   - Description (optional)
   - Due Date (optional)
   - Category (required)
3. Click **"Create Task"**
4. Try the features:
   - ✅ Click checkbox to mark complete
   - ✏️ Click edit icon to update
   - 🗑️ Click delete icon to remove
   - 🔍 Use filters to organize

## Environment Variables

### Backend (.env)
```env
MONGO_URL=mongodb://localhost:27017  # Your MongoDB connection
DB_NAME=todo_app                      # Database name
CORS_ORIGINS=*                        # CORS settings
```

### Frontend (.env)
```env
REACT_APP_BACKEND_URL=http://localhost:8001  # Backend URL
```

## Troubleshooting

### MongoDB Connection Issues
- Ensure MongoDB is running
- Check MONGO_URL in backend/.env
- Test connection: `mongosh mongodb://localhost:27017`

### Port Already in Use
**Backend (8001):**
```bash
# Find and kill process
lsof -ti:8001 | xargs kill -9  # Mac/Linux
netstat -ano | findstr :8001   # Windows
```

**Frontend (3000):**
```bash
# Find and kill process
lsof -ti:3000 | xargs kill -9  # Mac/Linux
netstat -ano | findstr :3000   # Windows
```

### Module Not Found
**Backend:**
```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

**Frontend:**
```bash
cd frontend
rm -rf node_modules yarn.lock
yarn install
```

## Development Tips

### Backend Development
- API auto-reloads on file changes
- View logs in terminal
- Test APIs at http://localhost:8001/docs

### Frontend Development
- Hot reload enabled
- View console in browser DevTools
- React DevTools recommended

## Production Deployment

See [README.md](./README.md#-deployment) for detailed deployment instructions.

## Need Help?

- 📖 Full Documentation: [README.md](./README.md)
- 🎨 Design System: [design_guidelines.md](./design_guidelines.md)
- 📋 Project Plan: [plan.md](./plan.md)
- 🤝 Contributing: [CONTRIBUTING.md](./CONTRIBUTING.md)
- 🐛 Issues: Open a GitHub issue

---

**Happy Task Managing! 🎉**