# SimplOS - Python Operating System Simulator

A fully functional desktop operating system simulator built with Python and Tkinter. It mimics Windows by providing a graphical desktop environment with a taskbar, file manager, terminal, calculator, text editor, and notepad.

## Features

✨ **Desktop Environment**
- Windows-like graphical interface
- Customizable desktop with green background
- Multiple window management
- Professional taskbar with system clock

📂 **File Manager**
- Browse directories and manage files
- Create folders and files
- Delete files and folders
- View file properties (type, size)
- Address bar for direct navigation
- Double-click to open files

⌨️ **Terminal Emulator**
- Command-line interface
- Built-in commands: `ls`, `cd`, `pwd`, `mkdir`, `touch`, `del`, `cls`, `type`, `help`, `exit`
- Command history with arrow keys
- Real directory navigation

📝 **Text Editor**
- Create and edit text files
- Open and save functionality
- File dialog integration
- Syntax-aware interface

📋 **Notepad**
- Quick note-taking application
- Character counter
- Clear functionality
- Auto-save ready

🧮 **Calculator**
- Basic arithmetic operations
- Square root function
- Percentage calculation
- Clear and backspace buttons

## Project Structure

```
SimplOS/
├── main.py                  # Entry point
├── core/
│   └── os.py               # Core OS engine
├── ui/
│   ├── desktop.py          # Main desktop environment
│   └── taskbar.py          # System taskbar
├── apps/
│   ├── app_launcher.py     # Application launcher
│   ├── file_manager.py     # File manager
│   ├── terminal.py         # Terminal emulator
│   ├── text_editor.py      # Text editor
│   ├── calculator.py       # Calculator
│   └── notepad.py          # Notepad
├── utils/
│   ├── window_manager.py   # Window management system
│   └── file_system.py      # Virtual file system
└── README.md              # This file
```

## Installation

### Requirements
- Python 3.6 or higher
- tkinter (usually included with Python)

### Setup

1. **Clone or download the project**
```bash
cd "C:\Users\ASUS\OneDrive\Documents\Python Project\OS"
```

2. **Verify Python installation**
```bash
python --version
```

3. **Run the OS**
```bash
python main.py
```

## Usage

### Starting the OS
```bash
python main.py
```

The main desktop window will open with a green background and application icons.

### Using Applications

1. **Click on any application icon** to launch it
   - 📁 File Manager
   - ⌨️ Terminal
   - 📝 Text Editor
   - 🧮 Calculator
   - 📓 Notepad

2. **Taskbar Controls**
   - Click **Start** button for application menu
   - View system **clock** on the right
   - **Volume** and **Network** status indicators

### File Manager
- Navigate directories with back/forward buttons
- Use address bar to jump to specific paths
- Right-click for context menu (create, delete)
- Double-click to open folders/files

### Terminal Commands
```
help       - Show all available commands
ls / dir   - List directory contents
cd <path>  - Change directory (.. goes to parent)
pwd        - Print working directory
mkdir      - Create new directory
touch      - Create new file
del        - Delete file/folder
cls/clear  - Clear screen
type/cat   - Display file contents
exit       - Close terminal
```

### Text Editor
- **File > New** - Create new document
- **File > Open** - Open existing file
- **File > Save** - Save current document
- **Edit > Clear All** - Clear all text

## Customization

### Changing Colors
Edit `core/os.py` - modify the background color in line:
```python
self.root.config(bg="#0078d4")  # Change this hex color
```

### Adding New Applications
1. Create new file in `apps/` directory
2. Inherit from `tk.Frame`
3. Add to `app_launcher.py` apps list
4. Handle in `desktop.py` `open_app_window()` method

### Customizing Taskbar
Edit `ui/taskbar.py` to add:
- New system tray icons
- Additional buttons
- Custom widgets

## File System

The OS creates a virtual file system in:
```
C:\Users\[YourUsername]\SimplOS\
├── Documents/
├── Desktop/
├── Downloads/
├── Pictures/
├── Applications/
└── System/
```

All file operations within the OS stay within this directory.

## Known Limitations

- No actual network connectivity
- File operations limited to Python's OS module
- Single-user environment
- No multi-processing
- Simple virtual file system

## Future Enhancements

- [ ] System settings panel
- [ ] Sound support
- [ ] Desktop shortcuts
- [ ] System tray menu customization
- [ ] More built-in applications (Paint, Notepad++)
- [ ] File drag-and-drop
- [ ] Window minimize/maximize properly
- [ ] Boot animation
- [ ] User profiles
- [ ] Network simulator

## Troubleshooting

### "ModuleNotFoundError: No module named 'tkinter'"
```bash
# Install tkinter
# Windows (if not included):
pip install tk

# Linux:
sudo apt-get install python3-tk

# macOS:
brew install python-tk
```

### Application doesn't start
- Ensure all files are in the correct directories
- Check Python version (3.6+)
- Verify tkinter is installed

### File Manager shows empty
- Check if SimplOS folder exists in your home directory
- The folder is auto-created on first run

## Performance Tips

- Keep the number of open windows reasonable
- Close unused applications to free memory
- Large files may be slow in the terminal

## License

This project is open source. Feel free to modify and extend it for your needs.

## Author Notes

SimplOS was created as an educational project to demonstrate:
- Object-oriented programming in Python
- GUI development with Tkinter
- Window management systems
- File system operations
- Terminal emulation basics

It's a great learning project for beginners to understand how operating systems work at a high level!

---

Enjoy your SimplOS experience! 🎉
