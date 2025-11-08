import os
import time
from tqdm import tqdm  # for progress bar

# ---------- HEADER ----------
print("=" * 60)
print("🔥 FILE EXTENSION CHANGER – PjxhbvjhvbvN mm🔥")
print("👨‍💻 Developer: Your Name")
print("📂 Purpose: Rename all files to a custom extension")
print("=" * 60)
time.sleep(0.5)

# ---------- USER INPUT ----------
TARGET_DIR = input("📁 Enter target folder path: ").strip()
NEW_EXT = input("🧩 Enter new extension (e.g. .hidex): ").strip()

# ---------- VALIDATION ----------
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
