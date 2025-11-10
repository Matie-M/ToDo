#!/bin/bash

# TaskFlow Setup Script
# This script helps you set up the TaskFlow application quickly

set -e  # Exit on error

echo "🚀 TaskFlow Setup Script"
echo "======================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if required tools are installed
echo "📋 Checking prerequisites..."

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is not installed${NC}"
    exit 1
fi
echo -e "${GREEN}✓${NC} Python 3 found"

if ! command -v node &> /dev/null; then
    echo -e "${RED}❌ Node.js is not installed${NC}"
    exit 1
fi
echo -e "${GREEN}✓${NC} Node.js found"

if ! command -v yarn &> /dev/null; then
    echo -e "${YELLOW}⚠ Yarn not found, installing...${NC}"
    npm install -g yarn
fi
echo -e "${GREEN}✓${NC} Yarn found"

echo ""
echo "🔧 Setting up backend..."
cd backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating backend .env file..."
    cp .env.example .env
    echo -e "${YELLOW}⚠ Please update backend/.env with your MongoDB URL${NC}"
fi

cd ..

echo ""
echo "🎨 Setting up frontend..."
cd frontend

# Install Node dependencies
echo "Installing Node dependencies..."
yarn install

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating frontend .env file..."
    cp .env.example .env
    echo -e "${YELLOW}⚠ Please update frontend/.env with your backend URL${NC}"
fi

cd ..

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "📚 Next steps:"
echo "1. Update backend/.env with your MongoDB connection string"
echo "2. Update frontend/.env with your backend URL (if different from default)"
echo "3. Start the backend: cd backend && source venv/bin/activate && uvicorn server:app --reload"
echo "4. Start the frontend: cd frontend && yarn start"
echo ""
echo "🌐 The app will be available at:"
echo "   Frontend: http://localhost:3000"
echo "   Backend:  http://localhost:8001"
echo "   API Docs: http://localhost:8001/docs"
echo ""