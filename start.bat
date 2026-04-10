@echo off
REM Prama's OS - Quick Start Batch File
REM For Windows users to easily launch Prama's OS

echo.
echo ========================================
echo     SimplOS Operating System
echo ========================================
echo.
echo Starting SimplOS...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please install Python from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

REM Check if tkinter is available
python -c "import tkinter" >nul 2>&1
if errorlevel 1 (
    echo ERROR: Tkinter is not installed!
    echo Install it with: pip install tk
    pause
    exit /b 1
)

REM Launch SimplOS
echo Python ✓
echo Tkinter ✓
echo SimplOS ✓
echo.
echo Launching SimplOS...
python main.py

if errorlevel 1 (
    echo.
    echo ERROR: SimplOS failed to start!
    echo Try running: python verify_installation.py
    pause
    exit /b 1
)
