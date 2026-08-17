#!/bin/bash

# CyberSecurity Toolkit Pro Installer
# By STYVEN Emmanuel

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║     🔐 CyberSecurity Toolkit Pro Installer                  "
echo "║     By STYVEN Emmanuel                                     "
echo "╚═══════════════════════════════════════════════════════════════╝"

# Update packages
echo -e "\n📦 Updating packages..."
pkg update && pkg upgrade -y

# Install dependencies
echo -e "\n📥 Installing dependencies..."
pkg install -y python python-pip nmap traceroute dnsutils git

# Install Python packages
echo -e "\n📦 Installing Python packages..."
pip install dnspython python-whois requests colorama termcolor

# Download the tool
echo -e "\n📥 Downloading CyberSecurity Toolkit..."
curl -o cybersec_pro.py https://raw.githubusercontent.com/Styven-Emmanuel-Dev/cybersec-toolkit/main/cybersec_pro.py

# Make executable
chmod +x cybersec_pro.py

# Create alias
echo -e "\n🔗 Creating alias..."
echo "alias cyber='python cybersec_pro.py'" >> ~/.bashrc
echo "alias cybersec='python cybersec_pro.py'" >> ~/.bashrc

echo -e "\n✅ Installation complete!"
echo -e "\n📱 Follow me on:"
echo -e "   📺 Telegram: https://t.me/StyvenEmmanuelDev"

echo -e "   📱 WhatsApp: https://whatsapp.com/channel/0029VbCUG0XHltYAlmcp9A3T"
echo -e "   🐙 GitHub: https://github.com/Styven-Emmanuel-Dev"
echo -e "\n🚀 To start: python cybersec_pro.py"
echo -e "   Or: cyber (after restarting Termux)"