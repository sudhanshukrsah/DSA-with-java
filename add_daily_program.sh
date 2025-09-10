#!/bin/bash

# Daily Java Streak Command
# Usage: ./add_daily_program.sh

echo "🚀 Adding one Java program for daily streak..."
echo "======================================"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3 to use this script."
    exit 1
fi

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ This is not a git repository."
    echo "Please run this script from the root of your git repository."
    exit 1
fi

# Run the daily streak automation
python3 daily_streak.py

# Check if the Python script succeeded
if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Daily program added successfully!"
    echo ""
    echo "Next steps:"
    echo "1. Review the generated code"
    echo "2. Push to GitHub: git push origin main"
    echo "3. Keep the streak alive! 🔥"
else
    echo ""
    echo "❌ Failed to add daily program."
    echo "Please check the error messages above."
    exit 1
fi