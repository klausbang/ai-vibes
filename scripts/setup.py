#!/usr/bin/env python3
"""
Quick setup script for AI Vibes development environment.
This script helps new contributors get started quickly.
"""

import subprocess
import sys
import os
import platform
from pathlib import Path


def run_command(cmd, description="", check=True):
    """Run a command with optional description."""
    if description:
        print(f"🔧 {description}")
    
    try:
        if isinstance(cmd, str):
            result = subprocess.run(cmd, shell=True, check=check, capture_output=True, text=True)
        else:
            result = subprocess.run(cmd, check=check, capture_output=True, text=True)
        
        if result.stdout:
            print(result.stdout)
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
        if check:
            sys.exit(1)
        return e


def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required.")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        sys.exit(1)
    else:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")


def check_git():
    """Check if Git is installed."""
    try:
        result = run_command(["git", "--version"], check=False)
        if result.returncode == 0:
            print(f"✅ {result.stdout.strip()}")
            return True
        else:
            print("❌ Git is not installed or not in PATH")
            return False
    except FileNotFoundError:
        print("❌ Git is not installed")
        return False


def setup_virtual_environment():
    """Set up Python virtual environment."""
    venv_path = Path("venv")
    
    if venv_path.exists():
        print("📁 Virtual environment already exists")
        return
    
    print("🐍 Creating virtual environment...")
    run_command([sys.executable, "-m", "venv", "venv"])
    
    # Get activation script path based on OS
    if platform.system() == "Windows":
        activate_script = venv_path / "Scripts" / "activate.bat"
        pip_path = venv_path / "Scripts" / "pip.exe"
    else:
        activate_script = venv_path / "bin" / "activate"
        pip_path = venv_path / "bin" / "pip"
    
    print(f"✅ Virtual environment created at: {venv_path.absolute()}")
    print(f"💡 To activate, run: {activate_script}")
    
    return str(pip_path)


def install_dependencies(pip_path=None):
    """Install project dependencies."""
    if pip_path is None:
        pip_path = "pip"
    
    requirements_files = ["requirements.txt", "requirements-dev.txt"]
    
    for req_file in requirements_files:
        if Path(req_file).exists():
            print(f"📦 Installing dependencies from {req_file}...")
            run_command([pip_path, "install", "-r", req_file])
        else:
            print(f"⚠️  {req_file} not found, skipping...")


def setup_pre_commit():
    """Set up pre-commit hooks."""
    if Path(".pre-commit-config.yaml").exists():
        print("🔗 Setting up pre-commit hooks...")
        run_command(["pre-commit", "install"])
        print("✅ Pre-commit hooks installed")
    else:
        print("⚠️  .pre-commit-config.yaml not found, skipping pre-commit setup")


def check_ai_tools():
    """Check for AI development tools."""
    print("\n🤖 Checking AI Development Tools:")
    
    # Note: These are just informational checks
    print("   📝 Recommended AI Tools:")
    print("   • GitHub Copilot (VS Code extension)")
    print("   • ChatGPT/Claude (web interfaces)")
    print("   • AI-powered IDEs (Cursor, Replit, etc.)")
    print("   💡 Install these tools for enhanced development experience")


def display_next_steps():
    """Display next steps for the user."""
    print("\n🎉 Setup Complete!")
    print("=" * 50)
    print("📝 Next Steps:")
    print("1. Activate your virtual environment:")
    
    if platform.system() == "Windows":
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    
    print("2. Verify installation:")
    print("   python -m pytest --version")
    print("   black --version")
    print("   flake8 --version")
    
    print("3. Read the documentation:")
    print("   • docs/getting-started.md")
    print("   • guides/github-workflow.md")
    print("   • guides/vibe-coding.md")
    
    print("4. Make your first contribution:")
    print("   • Check issues labeled 'good first issue'")
    print("   • Follow the GitHub workflow guide")
    print("   • Use AI assistance with proper attribution")
    
    print("\n🚀 Happy Coding with AI Vibes!")


def main():
    """Main setup function."""
    print("🎯 AI Vibes Development Environment Setup")
    print("=" * 50)
    
    # Check prerequisites
    check_python_version()
    
    if not check_git():
        print("💡 Please install Git and try again.")
        print("   Download from: https://git-scm.com/downloads")
        sys.exit(1)
    
    # Setup development environment
    pip_path = setup_virtual_environment()
    install_dependencies(pip_path)
    setup_pre_commit()
    check_ai_tools()
    
    # Display next steps
    display_next_steps()


if __name__ == "__main__":
    main()
