#!/bin/bash
# Update CyberSecurity Toolkit
# By STYVEN Emmanuel

echo "🔄 Updating CyberSecurity Toolkit..."
git pull origin main

echo "📦 Updating dependencies..."
pip install -r requirements.txt --upgrade

echo "✅ Update complete!"
python cybersec_pro.py