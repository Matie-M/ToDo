@echo off
REM TaskFlow Setup Script for Windows
REM This script helps you set up the TaskFlow application quickly

echo.
echo ================================
echo TaskFlow Setup Script (Windows)
echo ================================
echo.

REM Check Python
echo Checking prerequisites...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python 3 is not installed
    exit /b 1
)
echo [OK] Python 3 found

REM Check Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js is not installed
    exit /b 1
)
echo [OK] Node.js found

REM Check Yarn
yarn --version >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Yarn not found, installing...
    npm install -g yarn
)
echo [OK] Yarn found

echo.
echo Setting up backend...
cd backend

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install Python dependencies
echo Installing Python dependencies...
pip install -r requirements.txt

REM Create .env if it doesn't exist
if not exist ".env" (
    echo Creating backend .env file...
    copy .env.example .env
    echo [WARNING] Please update backend\.env with your MongoDB URL
)

cd ..

echo.
echo Setting up frontend...
cd frontend

REM Install Node dependencies
echo Installing Node dependencies...
yarn install

REM Create .env if it doesn't exist
if not exist ".env" (
    echo Creating frontend .env file...
    copy .env.example .env
    echo [WARNING] Please update frontend\.env with your backend URL
)

cd ..

echo.
echo [SUCCESS] Setup complete!
echo.
echo Next steps:
echo 1. Update backend\.env with your MongoDB connection string
echo 2. Update frontend\.env with your backend URL (if different from default)
echo 3. Start the backend: cd backend ^&^& venv\Scripts\activate ^&^& uvicorn server:app --reload
echo 4. Start the frontend: cd frontend ^&^& yarn start
echo.
echo The app will be available at:
echo    Frontend: http://localhost:3000
echo    Backend:  http://localhost:8001
echo    API Docs: http://localhost:8001/docs
echo.
pause