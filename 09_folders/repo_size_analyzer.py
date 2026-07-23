from pathlib import Path
from time import perf_counter

# =============================================================================
# CONFIGURATION
# =============================================================================

# Repository path to analyze
REPO_PATH = Path(r"C:\Repos\MyRepository" ) # Update this path

# Number of results to display
TOP_FILES = 100
TOP_FOLDERS = 50

# Folders that will be skipped
IGNORED_FOLDERS = {
    ".git",
    ".terraform",
    ".idea",
    ".vs",
    ".vscode",
    "bin",
    "obj",
    "__pycache__",
}

# =============================================================================
# HELPERS

# Convert bytes into a human-readable format
def format_size(size_bytes: int) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024

    return f"{size_bytes:.2f} PB"


print("=" * 100)
print(f"Analyzing repository: {REPO_PATH}")
print("=" * 100)

files = []
folder_sizes = {}
total_size = 0

# Recursively scan all files in the repository
for file_path in REPO_PATH.rglob("*"):

    # Skip directories and process only files
    if not file_path.is_file():
        continue

    try:
        # Get file size in bytes
        file_size = file_path.stat().st_size

        # Store file information
        files.append((file_path, file_size))

        # Update total repository size
        total_size += file_size

        # Add the file size to the current directory
        current_folder = file_path.parent

        # Propagate the size up through all parent directories
        while True:

            folder_sizes[current_folder] = (
                folder_sizes.get(current_folder, 0) + file_size
            )    

            # Stop when reaching the repository root
            if current_folder == REPO_PATH:
                break

            current_folder = current_folder.parent

    except (PermissionError, FileNotFoundError):   
        # Skip files that cannot be accessed
        continue

# Sort files by size (largest first)
largest_files = sorted(
    files,
    key=lambda item: item[1],
    reverse=True
)

# Sort directories by size (largest first)
largest_folders = sorted(
    folder_sizes.items(),
    key=lambda item: item[1],
    reverse=True
)

print()
print("=" * 100)
print(f"TOTAL REPOSITORY SIZE: {format_size(total_size)}")
print("=" * 100)

print()
print("TOP LARGEST FILES")
print("-" * 100)

for file_path, file_size in largest_files[:TOP_FILES]:
    print(f"{format_size(file_size):>12}  {file_path}")

print()
print("=" * 100)
print("TOP LARGEST DIRECTORIES")
print("=" * 100)

for folder_path, folder_size in largest_folders[:TOP_FOLDERS]:
    print(f"{format_size(folder_size):>12}  {folder_path}")