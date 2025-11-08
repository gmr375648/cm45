import os
import time
from tqdm import tqdm
import subprocess
import sys
import shutil   # ✅ copy2 এর জন্য দরকার

# ---------- AUTO INSTALL REQUESTS ----------
try:
    import requests
except ImportError:
    print("📦 'requests' package not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

# ---------- VERSION ----------
VERSION = "v1.1.0"
GITHUB_VERSION_URL = "https://raw.githubusercontent.com/gmr375648/cm45/main/ver.txt"

# ---------- HEADER ----------
print("=" * 60)
print("🔥 FILE EXTENSION CHANGER – hidex 🔥")
print("👨‍💻 Developer: Your Name")
print("📂 Purpose: Copy all files with new extension, handle conflicts")
print("=" * 60)

# ---------- VERSION CHECK ----------
try:
    latest_version = requests.get(GITHUB_VERSION_URL, timeout=5).text.strip()
    print(f"🔢 Current version: {VERSION}")
    print(f"🌐 Latest version: {latest_version}")
    if latest_version != VERSION:
        print("⚠️ Update available! Type 'update' to fetch latest version")
    else:
        print("✅ You are running the latest version")
except:
    print("⚠️ Could not check latest version online")
time.sleep(0.5)
print("🔄 Tip: Type 'update' anytime to fetch the latest version")
print("=" * 60)

# ---------- USER INPUT ----------
TARGET_DIR = input("📁 Enter target folder path (or type 'update'): ").strip()
if TARGET_DIR.lower() == "update":
    print("\n🔄 Updating script from GitHub...")
    repo_path = os.path.dirname(os.path.abspath(__file__))
    os.system(f"cd {repo_path} && git fetch origin && git reset --hard origin/main && clear")
    print("✅ Update complete! Relaunch the script...")
    os.system(f"cd {repo_path} && python {os.path.basename(__file__)}")
    exit()

NEW_EXT = input("🧩 Enter new extension (e.g. .hidex): ").strip()
if not NEW_EXT.startswith("."):
    NEW_EXT = "." + NEW_EXT

if not os.path.exists(TARGET_DIR):
    print(f"\n❌ Path not found: {TARGET_DIR}")
    exit()

# ---------- HELPER FUNCTION ----------
def get_unique_name(path):
    """
    Conflict হলে sequential number (1,2,3...) যোগ করে unique name তৈরি করবে
    bracket ছাড়া
    """
    base = os.path.splitext(path)[0]
    ext = os.path.splitext(path)[1]
    counter = 1
    new_path = path
    while os.path.exists(new_path):
        new_path = f"{base}{counter}{ext}"  # only number, no brackets
        counter += 1
    return new_path

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
print(f"\n🔍 {total_files} files detected. Starting process...\n")
count = 0

for root, file in tqdm(all_files, desc="Processing", unit="file"):
    old_file = os.path.join(root, file)
    base_name = os.path.splitext(file)[0]       # remove old extension
    new_file = os.path.join(root, f"{base_name}{NEW_EXT}")
    new_file = get_unique_name(new_file)        # sequential numbering if conflict
    try:
        shutil.copy2(old_file, new_file)
        count += 1
    except Exception as e:
        print(f"\n❌ Error processing {file}: {e}")

# ---------- SUMMARY ----------
print("\n" + "=" * 60)
print(f"✅ Successfully created {count} files with new extension.")
print("🏁 Operation completed. Original files remain unchanged.")
print("=" * 60)
