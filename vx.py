import os
import time
from tqdm import tqdm

# ---------- AUTO INSTALL REQUESTS ----------
import subprocess
import sys

try:
    import requests
except ImportError:
    print("📦 'requests' package not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

# ---------- VERSION ----------
VERSION = "v1.0.5"  # current script version
GITHUB_VERSION_URL = "https://raw.githubusercontent.com/gmr375648/cm45/main/ver.txt"

# ---------- HEADER ----------
print("=" * 60)
print("🔥 FILE EXTENSION CHANGER – PROFESSIONAL Egvhgvkhvk 🔥")
print("👨‍💻 Developer: Your Name")
print("📂 Purpose: Rename all files to a custom extension")

# ---------- VERSION CHECK ----------
try:
    latest_version = requests.get(GITHUB_VERSION_URL, timeout=5).text.strip()
    print(f"🔢 Current version: {VERSION}")
    print(f"🌐 Latest version: {latest_version}")
    if latest_version != VERSION:
        print("⚠️ Update available! Type 'update' to fetch the latest version")
    else:
        print("✅ You are running the latest version")
except:
    print("⚠️ Could not check latest version online")

print("🔄 Tip: Type 'update' anytime to fetch the latest version from GitHub")
print("=" * 60)
time.sleep(0.5)

# ---------- USER INPUT ----------
TARGET_DIR = input("📁 Enter target folder path (or type 'update'): ").strip()

# ---------- UPDATE COMMAND ----------
if TARGET_DIR.lower() == "update":
    print("\n🔄 Updating script from GitHub...\n")
    time.sleep(0.5)

    repo_path = os.path.dirname(os.path.abspath(__file__))

    # Force update local repo
    os.system(f"cd {repo_path} && git fetch origin && git reset --hard origin/main && clear")

    print("✅ Update complete! Relaunching latest version...\n")
    time.sleep(1)
    os.system(f"cd {repo_path} && python vx.py")
    exit()

# ---------- NORMAL FILE RENAME MODE ----------
NEW_EXT = input("🧩 Enter new extension (e.g. .hidex): ").strip()

if not NEW_EXT.startswith("."):
    NEW_EXT = "." + NEW_EXT

if not os.path.exists(TARGET_DIR):
    print(f"\n❌ Path not found: {TARGET_DIR}")
    exit()

# ---------- COLLECT FILES ----------
all_files = []
for root, dirs, files in os.walk(TARGET_DIR):
    for file in files:
        all_files.append((root, file))

total_files = len(all_files)
if total_files == 0:
    print("\n⚠️ No files found in the target directory.")
    exit()

# ---------- MAIN PROCESS ----------
print(f"\n🔍 {total_files} files detected. Starting rename process...\n")
count = 0

for root, file in tqdm(all_files, desc="Processing", unit="file"):
    old_file = os.path.join(root, file)
    base_name = os.path.splitext(file)[0]
    new_file = os.path.join(root, base_name + NEW_EXT)
    try:
        os.rename(old_file, new_file)
        count += 1
    except Exception as e:
        print(f"\n❌ Error renaming {file}: {e}")

# ---------- SUMMARY ----------
print("\n" + "=" * 60)
print(f"✅ Successfully renamed {count} files.")
print("🏁 Operation completed. Thank you for using this tool!")
print("=" * 60)
