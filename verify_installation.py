"""
Prama's OS - Installation Verification Script
Run this script to verify your Prama's OS installation is complete
"""

import os
import sys
from pathlib import Path


def check_python_version():
    """Check if Python version is 3.6 or higher"""
    print("\n[1] Checking Python Version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 6:
        print(f"    ✓ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"    ✗ Python {version.major}.{version.minor} - UPGRADE NEEDED (3.6+ required)")
        return False


def check_tkinter():
    """Check if tkinter is installed"""
    print("\n[2] Checking Tkinter Installation...")
    try:
        import tkinter
        print("    ✓ tkinter is installed - OK")
        return True
    except ImportError:
        print("    ✗ tkinter is NOT installed")
        print("    Install with: pip install tk")
        return False


def check_project_structure():
    """Check if all required files and directories exist"""
    print("\n[3] Checking Project Structure...")
    
    base_path = Path(__file__).parent
    
    required_files = [
        'main.py',
        'config.py',
        'requirements.txt',
        'README.md',
        'QUICKSTART.md',
        'FEATURES.md',
        'PROJECT_SUMMARY.md',
        'core/os.py',
        'ui/desktop.py',
        'ui/taskbar.py',
        'apps/file_manager.py',
        'apps/terminal.py',
        'apps/text_editor.py',
        'apps/calculator.py',
        'apps/notepad.py',
        'apps/app_launcher.py',
        'utils/window_manager.py',
        'utils/file_system.py',
    ]
    
    all_ok = True
    for file in required_files:
        file_path = base_path / file
        if file_path.exists():
            print(f"    ✓ {file}")
        else:
            print(f"    ✗ {file} - MISSING!")
            all_ok = False
            
    return all_ok


def check_applications():
    """Check if all applications are available"""
    print("\n[4] Checking Available Applications...")
    
    apps = [
        ("📁", "File Manager", "apps/file_manager.py"),
        ("⌨️", "Terminal", "apps/terminal.py"),
        ("📝", "Text Editor", "apps/text_editor.py"),
        ("🧮", "Calculator", "apps/calculator.py"),
        ("📓", "Notepad", "apps/notepad.py"),
    ]
    
    base_path = Path(__file__).parent
    all_ok = True
    
    for emoji, name, filepath in apps:
        file_path = base_path / filepath
        if file_path.exists():
            print(f"    ✓ {emoji} {name}")
            lines = len(file_path.read_text().split('\n'))
            print(f"      ({lines} lines of code)")
        else:
            print(f"    ✗ {emoji} {name} - MISSING!")
            all_ok = False
            
    return all_ok


def check_virtual_fs():
    """Check virtual file system"""
    print("\n[5] Checking Virtual File System...")
    
    vfs_path = Path.home() / "Pramas_OS"
    if vfs_path.exists():
        print(f"    ✓ Virtual FS directory exists: {vfs_path}")
        
        subdirs = [
            "Documents", "Desktop", "Downloads", 
            "Pictures", "Applications", "System"
        ]
        all_ok = True
        for dir in subdirs:
            dir_path = vfs_path / dir
            if dir_path.exists():
                print(f"      ✓ {dir}/")
            else:
                print(f"      - {dir}/ (will be created on first run)")
        return all_ok
    else:
        print(f"    - Virtual FS will be created on first run")
        return True


def main():
    """Run all verification checks"""
    print("=" * 60)
    print("Prama's OS - Installation Verification Script")
    print("=" * 60)
    
    checks = [
        ("Python Version", check_python_version),
        ("Tkinter", check_tkinter),
        ("Project Structure", check_project_structure),
        ("Applications", check_applications),
        ("Virtual File System", check_virtual_fs),
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"    ✗ Error during check: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status:8} - {name}")
    
    print("=" * 60)
    print(f"Result: {passed}/{total} checks passed")
    print("=" * 60)
    
    if passed == total:
        print("\n🎉 All checks passed! Prama's OS is ready to run!")
        print("\nTo start Prama's OS:")
        print("  python main.py")
        return 0
    else:
        print("\n⚠️  Some checks failed. Please fix the issues above.")
        print("   Check README.md for help.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    
    print("\nPress Enter to exit...")
    input()
    
    sys.exit(exit_code)
