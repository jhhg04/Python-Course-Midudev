from pathlib import Path

# Repository path to analyze
REPO_PATH = Path(r"C:\Repos\MyRepository" ) # Update this path

# Number of results to display
TOP_FILES = 100
TOP_FOLDERS = 50


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