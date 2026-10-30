import shutil

from pathlib import Path

def identify_file(file):
    extension = file.suffix.lower()

    if extension == ".pdf":
        return "Document"

    elif extension in [".jpg", ".png", ".jpeg"]:
        return "Image"

    elif extension == ".txt":
        return "Text File"

    elif extension == ".csv":
        return "Data File"

    elif extension in [".mp3", ".wav", ".aac", ".flac"]:
        return "Audio"
    
    else:
        return "Unknown File"

def get_unique_path(destination):
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_path = destination.with_stem(
            f"{destination.stem}_{counter}"
        )

        if not new_path.exists():
            return new_path

        counter += 1

folder = Path("test_files")
summary = {}

for file in folder.iterdir():
    if not file.is_file():
        continue

    category = identify_file(file)
    summary[category] = summary.get(category, 0) + 1

    destination = Path("organized_files") / category

    target = get_unique_path(destination / file.name)

    try:
        shutil.move(str(file), str(target))
        print(file.name, "->", target.name)

    except OSError as error:
        print("Could not move:", file.name)
        print("Reason:", error)

categories = ["Document", "Image", "Text File", "Data File", "Audio", "Unknown File"]

for category in categories:
    folder_path = Path("organized_files") / category
    folder_path.mkdir(parents=True, exist_ok=True)

print("\n========== ORGANIZATION SUMMARY ==========")

for category, count in summary.items():
    print(category, ":", count)

print("Total files organized:", sum(summary.values()))