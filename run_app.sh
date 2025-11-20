#!/bin/bash

# Fraternity Family Tree App - Quick Start Script
# This script makes it easy to run the app with one command!

echo "🌲 Starting Fraternity Family Tree Visualization..."
echo ""

# Check if we're in the right directory
if [ ! -f "graph_app.py" ]; then
    echo "❌ Error: graph_app.py not found!"
    echo "Please run this script from the project directory:"
    echo "  cd '/Users/neelgandhi/Desktop/Brother code'"
    echo "  ./run_app.sh"
    exit 1
fi

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "⚠️  Streamlit not found. Installing dependencies..."
    pip install -r requirements.txt
fi

# Run the app
echo "✅ Launching app at http://localhost:8501"
echo "   Press Ctrl+C to stop the server"
echo ""

streamlit run graph_app.py





