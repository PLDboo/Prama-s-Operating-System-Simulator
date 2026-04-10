"""
Prama's OS - A Python-based Operating System Simulator
Main entry point for the OS
"""

from core.os import OperatingSystem

def main():
    """Initialize and run the operating system"""
    os = OperatingSystem()
    os.run()

if __name__ == "__main__":
    main()
