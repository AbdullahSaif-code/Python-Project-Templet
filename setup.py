import os
import shutil
import subprocess
import sys
import venv
from pathlib import Path

# Define the virtual environment directory
venv_path = Path("venv")

# Delete existing virtual environment if it exists
if venv_path.exists() and venv_path.is_dir():
    print(f"🗑️  Removing existing virtual environment at: {venv_path}")
    shutil.rmtree(venv_path)

# Create a new virtual environment
print("📦 Creating a new virtual environment...")
venv.create(venv_path, with_pip=True)

# Determine pip executable path
if os.name == "nt":  # Windows
    pip_executable = venv_path / "Scripts" / "pip.exe"
else:  # Linux/macOS
    pip_executable = venv_path / "bin" / "pip"

# Upgrade pip
print("⬆️  Upgrading pip...")
subprocess.run([str(pip_executable), "install", "--upgrade", "pip"], check=True)

# Install dependencies from requirements.txt if available
requirements_file = Path("requirements.txt")
if requirements_file.exists():
    print("📄 Installing dependencies from requirements.txt...")
    subprocess.run([str(pip_executable), "install", "-r", str(requirements_file)], check=True)
else:
    print("⚠️  No requirements.txt found. Skipping package installation.")

# Print activation instructions
print("\n✅ Setup complete!")
if os.name == "nt":
    print("🔹 To activate the virtual environment (Windows):")
    print("    venv\\Scripts\\activate")
else:
    print("🔹 To activate the virtual environment (Linux/macOS):")
    print("    source venv/bin/activate")
