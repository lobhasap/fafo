#!/bin/bash

# 🚀 House Price Prediction API Deployment Script
# This script sets up the complete ML API pipeline

echo "🏠 House Price Prediction API - Deployment Script"
echo "=================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Train the model
echo "🧠 Training the ML model..."
python train_model.py

# Check if model was created successfully
if [ ! -f "house_price_model.pkl" ]; then
    echo "❌ Model training failed. Please check the error messages above."
    exit 1
fi

echo "✅ Model trained successfully!"

# Start the API server in the background
echo "🚀 Starting API server..."
python app.py &
API_PID=$!

# Wait for server to start
echo "⏳ Waiting for server to start..."
sleep 5

# Test the API
echo "🧪 Testing API endpoints..."
python test_api.py

# Check if tests passed
if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Deployment successful!"
    echo "=================================================="
    echo "📊 API Server: http://localhost:5000"
    echo "🌐 Frontend: Open index.html in your browser"
    echo "📋 API Docs: http://localhost:5000/"
    echo "🏥 Health Check: http://localhost:5000/health"
    echo ""
    echo "💡 To stop the server, run: kill $API_PID"
    echo "💡 To test the frontend, open index.html in your browser"
    echo ""
    echo "🚀 Ready for deployment to Render/Heroku!"
else
    echo "❌ API tests failed. Please check the error messages above."
    kill $API_PID 2>/dev/null
    exit 1
fi

# Keep the script running
echo "Press Ctrl+C to stop the server..."
wait $API_PID 