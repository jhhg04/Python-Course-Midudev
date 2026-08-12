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
# =============================================================================

# Convert bytes into a human-readable format
def format_size(size_bytes: int) -> str:

    size = float(size_bytes)

    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"

# Return True if the path contains an ignored folder
def should_ignore(path: Path) -> bool:
    return any(part in IGNORED_FOLDERS for part in path.parts)

# Scan the repository and return: - files - folder sizes - total size - file count
def scan_repository(REPO_PATH: Path):

    files = []
    folder_sizes = {}
    total_size = 0
    file_count = 0

    # Recursively scan all files in the repository
    for file_path in REPO_PATH.rglob("*"):

        if should_ignore(file_path):
            continue

        if not file_path.is_file():
            continue

        try:
            file_size = file_path.stat().st_size

            files.append((file_path, file_size))

            total_size += file_size

            file_count += 1

            current_folder = file_path.parent

            while True:

                folder_sizes[current_folder] = (
                    folder_sizes.get(current_folder, 0)
                    + file_size
                )

                if current_folder == REPO_PATH:
                    break

                current_folder = current_folder.parent

        except (PermissionError, FileNotFoundError, OSError):
            continue

    return files, folder_sizes, total_size, file_count

# =============================================================================
# MAIN
# =============================================================================

def main():

    if not REPO_PATH.exists():
        print(f"Repository not found: {REPO_PATH}")
        return

    print("=" * 100)
    print(f"Repository Analyzer")
    print("=" * 100)
    print(f"Repository : {REPO_PATH}")
    print()

    start = perf_counter()

    files, folder_sizes, total_size, file_count = scan_repository(REPO_PATH)

    elapsed = perf_counter() - start

    largest_files = sorted(
        files,
        key=lambda item: item[1],
        reverse=True,
    )