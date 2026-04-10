# SimplOS - Feature Documentation

## Complete Feature List

### 🖥️ Desktop Environment

**Features:**
- Windows-like green desktop background
- Application icons for quick access
- Window management system
- Multi-window support
- Clean and intuitive UI/UX

**Technical Details:**
- Built with Python Tkinter
- Responsive layout
- Professional appearance
- Scalable window manager

---

## 📁 File Manager

A complete file browser with full functionality:

### Features
- **Browse Directories** - Navigate through folder structure
- **File Operations** - Create, delete, rename files and folders
- **View Details** - See file type and size information
- **Address Bar** - Jump to any directory path
- **Navigation Buttons** - Back/Forward/Home navigation
- **Right-Click Menu** - Quick access to file operations
- **Double-Click** - Open folders and files

### How to Use
```
1. Launch File Manager from desktop
2. Navigate using folder buttons or address bar
3. Right-click for options (create, delete)
4. Double-click folders to enter them
5. Double-click files to open with default app
```

### File Operations
- Create new folder
- Create new file
- Delete files/folders (with confirmation)
- View folder structure
- Read file properties

---

## ⌨️ Terminal Emulator

A functional command-line interface with built-in commands:

### Built-in Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `help` | `help` | Show all available commands |
| `ls` / `dir` | `ls` | List directory contents |
| `cd` | `cd Documents` | Change directory (.. goes parent) |
| `pwd` | `pwd` | Print working directory |
| `mkdir` | `mkdir FolderName` | Create new folder |
| `touch` | `touch filename.txt` | Create new file |
| `del` | `del filename.txt` | Delete file/folder |
| `type` / `cat` | `type file.txt` | Display file contents |
| `cls` / `clear` | `cls` | Clear screen |
| `exit` | `exit` | Close terminal |

### Advanced Features
- **Command History** - Use Up/Down arrows to navigate
- **Directory Navigation** - Full path support
- **Error Handling** - Graceful error messages
- **Directory Display** - Shows current directory in prompt

### Example Session
```bash
SimplOS> mkdir Projects
Created directory: Projects

SimplOS> cd Projects
Projects> touch myfile.txt
Created file: myfile.txt

Projects> ls
<DIR>        Documents
<FILE>       README.txt
<FILE>       myfile.txt

Projects> pwd
C:\Users\YourName\SimplOS\Projects
```

---

## 📝 Text Editor

Full-featured text editing application:

### File Operations
- **New** - Create new documents
- **Open** - Load text files from disk
- **Save** - Save to current file
- **Save As** - Save with new name/location

### Editing Features
- **Undo/Redo** - Full edit history
- **Text Wrapping** - Automatic word wrap
- **Scrolling** - Scroll bars for large files
- **Status Bar** - Shows current state
- **Multi-line** - Edit large documents

### Usage Tips
- Use File menu for all operations
- Changes are tracked automatically
- Supports common file types (.txt, .py, .md, etc.)
- Fast file I/O

---

## 🧮 Calculator

A fully functional arithmetic calculator:

### Operations
- **Basic Math** - Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Advanced** - Square root (√), Percentage (%)
- **Backspace** - Delete last digit (←)
- **Clear** - Clear all (C)

### Features
- Large display with green text on black
- Professional button layout
- Real-time calculation
- Error handling for invalid operations

### Example Calculations
```
7 + 3 = 10
25 * 4 = 100
16 √ = 4
100 % 10 = 10
45 / 3 = 15
```

---

## 📓 Notepad

Quick note-taking application:

### Features
- **Quick Notes** - Fast text entry
- **Character Count** - Track document size
- **Clear Function** - Quick clear with confirmation
- **Text Wrapping** - Automatic line wrapping
- **Auto-Update** - Real-time statistics

### Usage
- Open Notepad icon
- Start typing immediately
- Character count updates automatically
- Click Clear to wipe all text (with confirmation)

---

## 🖱️ Taskbar

System taskbar with essential information:

### Components

**Left Side:**
- **Start Button** - Access application menu
- **Window List** - Shows open applications

**Right Side (System Tray):**
- **System Clock** - Real-time display updates every second
- **Volume Icon** - System audio status (🔊)
- **Network Icon** - Connection status (📡)

### Start Menu
Click "Start" to see all available applications:
- File Manager
- Terminal
- Text Editor
- Calculator
- Notepad
- Shutdown option

### Window Management
- Click window names in taskbar to switch between open apps
- Minimize/restore windows
- Close applications from taskbar

---

## 🔧 System Features

### Window Manager
- **Unique IDs** - Each window gets unique identifier
- **State Tracking** - Knows which windows are open
- **Active Window** - Tracks currently active window
- **Window Registry** - Central window management

### File System
- **Virtual Root** - All files stored in SingleOS folder
- **Directory Structure** - Organized folder tree
- **File Operations** - Create, read, delete, list
- **Path Handling** - Full path support

### UI/UX Elements
- **Professional Fonts** - Segoe UI family
- **Color Scheme** - Windows-inspired colors
- **Responsive Layout** - Adapts to window size
- **Icons/Emojis** - Visual app identification

---

## 🎨 Customization Guide

### Change Desktop Color
Edit `core/os.py`:
```python
self.root.config(bg="#0078d4")  # Blue
self.root.config(bg="#c0c0c0")  # Gray
self.root.config(bg="#ff0000")  # Red
```

### Add New Application
1. Create file in `apps/` folder: `myapp.py`
2. Add to `app_launcher.py` app list
3. Handle in `desktop.py` open function

### Modify Taskbar
Edit `ui/taskbar.py` to:
- Add system tray icons
- Change clock format
- Add new buttons
- Customize colors

---

## 📊 System Statistics

| Metric | Value |
|--------|-------|
| **Total Lines of Code** | ~1500+ |
| **Number of Modules** | 11 |
| **Number of Apps** | 5 |
| **Supported Commands** | 10+ |
| **File Types Supported** | All text files |
| **Max Windows** | Unlimited |
| **Memory Efficient** | Yes |
| **Cross-Platform** | Windows, Linux, macOS |

---

## 🚀 Performance

### Speed
- Instant app launch
- Fast file operations
- Quick calculations
- Responsive UI

### Resource Usage
- Lightweight GUI framework
- Minimal memory footprint
- Efficient window management
- Optimized file access

---

## 🔐 Security Features

- **File Isolation** - All files in virtual directory
- **Safe Operations** - Confirmation dialogs for deletions
- **Error Handling** - Graceful error messages
- **No System Access** - Restricted to virtual OS

---

## 📚 Educational Value

This project demonstrates:
1. **Object-Oriented Programming** - Classes and inheritance
2. **GUI Development** - Tkinter framework
3. **File I/O** - File system operations
4. **Window Management** - Multi-window applications
5. **Command Parsing** - Terminal command interpretation
6. **String Manipulation** - Text processing
7. **Threading** - Clock update thread
8. **Event Handling** - User interactions

---

## 🎉 Conclusion

SimplOS provides a complete, functional operating system simulation with professional UI/UX and practical applications for learning and productivity!
