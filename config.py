"""
Prama's OS Configuration File
Customize your operating system here!
"""

# ============================================================
# DISPLAY SETTINGS
# ============================================================

# Window title
WINDOW_TITLE = "Prama's OS - Simple Operating System"

# Window size (width, height)
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700

# Desktop background color (hex code)
DESKTOP_COLOR = "#008000"  # Green (classic Windows)

# Taskbar color
TASKBAR_COLOR = "#c0c0c0"  # Light gray

# ============================================================
# SYSTEM SETTINGS
# ============================================================

# System font
SYSTEM_FONT = "Segoe UI"

# Display 12-hour or 24-hour clock
CLOCK_FORMAT = "24"  # Options: "12" or "24"

# ============================================================
# APPLICATIONS
# ============================================================

# Available applications (can customize here)
APPLICATIONS = [
    {"emoji": "📁", "name": "File Manager", "app_type": "file_manager"},
    {"emoji": "⌨️", "name": "Terminal", "app_type": "terminal"},
    {"emoji": "📝", "name": "Text Editor", "app_type": "text_editor"},
    {"emoji": "🧮", "name": "Calculator", "app_type": "calculator"},
    {"emoji": "📓", "name": "Notepad", "app_type": "notepad"},
]

# ============================================================
# FILE SYSTEM
# ============================================================

# Virtual file system root directory
# Leave empty to use user's home folder
VIRTUAL_FS_ROOT = ""  # Or set to specific path like "C:/SimplOS"

# ============================================================
# ADVANCED SETTINGS
# ============================================================

# Enable debug mode (prints extra information)
DEBUG_MODE = False

# Auto-save notepad every N seconds (0 = disabled)
AUTOSAVE_INTERVAL = 5

# Maximum number of open windows
MAX_WINDOWS = 20

# Theme (can add more themes here)
THEME = "classic"  # Options: "classic", "modern", "dark"

# ============================================================
# CUSTOMIZATION EXAMPLES
# ============================================================

# To change desktop color to blue:
# DESKTOP_COLOR = "#0078d4"

# To add a new application, add to APPLICATIONS list:
# {"emoji": "🎮", "name": "Game", "app_type": "game_app"}
# Then create game_app.py in apps/ folder

# To change window size:
# WINDOW_WIDTH = 1600
# WINDOW_HEIGHT = 900

# ============================================================
# LOADING CONFIG
# ============================================================

def load_config():
    """Load all configuration settings"""
    return {
        "window_title": WINDOW_TITLE,
        "window_width": WINDOW_WIDTH,
        "window_height": WINDOW_HEIGHT,
        "desktop_color": DESKTOP_COLOR,
        "taskbar_color": TASKBAR_COLOR,
        "system_font": SYSTEM_FONT,
        "clock_format": CLOCK_FORMAT,
        "applications": APPLICATIONS,
        "virtual_fs_root": VIRTUAL_FS_ROOT,
        "debug_mode": DEBUG_MODE,
        "autosave_interval": AUTOSAVE_INTERVAL,
        "max_windows": MAX_WINDOWS,
        "theme": THEME,
    }

if __name__ == "__main__":
    # Print current configuration
    cfg = load_config()
    for key, value in cfg.items():
        print(f"{key}: {value}")
