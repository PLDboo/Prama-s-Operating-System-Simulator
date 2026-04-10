# SimplOS - Quick Start Guide

## 🚀 Getting Started (5 minutes)

### Step 1: Navigate to the project folder
```bash
cd "C:\Users\ASUS\OneDrive\Documents\Python Project\OS"
```

### Step 2: Run SimplOS
```bash
python main.py
```

A window will open showing the SimplOS desktop with a green background!

## 🖱️ First Steps

1. **Look at the desktop** - You'll see 5 application icons ready to use
2. **Click the Start button** (bottom-left) - Opens the application menu
3. **Launch an app** - Click any icon to open that application
4. **View the taskbar** - Bottom of screen shows system info and clock

## 📱 Applications Overview

| App | What it does | How to use |
|-----|-------------|-----------|
| 📁 File Manager | Browse your files | Click to navigate folders, double-click to open |
| ⌨️ Terminal | Command-line interface | Type commands like `ls`, `mkdir`, `cd` |
| 📝 Text Editor | Create/edit text files | File > New/Open/Save |
| 🧮 Calculator | Do math | Click buttons or type numbers |
| 📓 Notepad | Quick notes | Just start typing |

## 💡 Tips & Tricks

### File Manager
- Use the address bar to jump directly to a folder
- Right-click for quick options (create, delete)
- Click "Home" to go back to your main folder

### Terminal
```bash
# Show all commands
help

# Create a folder
mkdir MyFolder

# List files
ls

# Change folder
cd Documents

# Go back one folder
cd ..

# Create a file
touch newfile.txt

# Delete
del filename.txt

# Clear screen
cls
```

### Opening Files
- Double-click in File Manager to open files
- Use Text Editor to edit text files
- Terminal can view files with `type filename.txt`

## 🎮 Keyboard Shortcuts

| Key | Action |
|-----|--------|
| Up Arrow | Previous terminal command |
| Down Arrow | Next terminal command |
| Return | Execute terminal command |
| Ctrl+A | Select all (in text editor) |
| Ctrl+Z | Undo (in text editor) |

## 📊 Default Folders

When you first open File Manager, these folders are created:
- **Documents** - For storing documents
- **Desktop** - Desktop files
- **Downloads** - Downloaded files
- **Pictures** - Image files
- **Applications** - App shortcuts
- **System** - System files

All files are stored in: `C:\Users\[YourUsername]\SimplOS\`

## ❓ Troubleshooting

**Problem:** Window doesn't open
- Check that Python is installed: `python --version`
- Ensure you're in right folder: `cd C:\Users\ASUS\OneDrive\Documents\Python Project\OS`

**Problem:** "No module named tkinter"
- Install tkinter: `pip install tk`
- On Linux: `sudo apt-get install python3-tk`

**Problem:** Application crashes on open
- Check README.md for more details
- Make sure all files are in correct folders

## 🛠️ Customization Ideas

1. **Change colors** - Edit `core/os.py` line with `bg="#0078d4"`
2. **Add apps** - Create new app in `apps/` folder
3. **Modify terminal** - Edit `apps/terminal.py`
4. **Change taskbar** - Edit `ui/taskbar.py`

## 📚 Learning Resources

This project teaches:
- Object-oriented Python programming
- GUI development with Tkinter
- File system operations
- Window management
- Terminal emulation basics

## 🎉 Have Fun!

SimplOS is designed for learning and exploration. Try:
- Creating files in File Manager
- Using terminal commands
- Doing calculations
- Taking notes
- Editing text files

---

**Questions?** Check the main README.md for complete documentation!
