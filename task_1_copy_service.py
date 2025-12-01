import shutil
import sys
from pathlib import Path


def main():
    args = sys.argv[1:]

    if not args:
        print("❌ Enter source dir path. Example: python script.py <source_dir> [output_dir]")
        return

    source_dir = Path(args[0])
    output_dir = Path(args[1]) if len(args) > 1 else Path("dist")
  
    sort_dir(source_dir, output_dir)
    

def copy_files_move_to_new_dir(source_path: Path, output_path: Path):
    for item in source_path.iterdir():
        if item.is_dir():
            copy_files_move_to_new_dir(item, output_path)
        else:
            sub_folder = output_path / item.suffix.lstrip(".")
            if sub_folder.is_dir():
                copy_file(item, sub_folder)
            else:
                sub_folder.mkdir(exist_ok=True)


def sort_dir(source_dir: str, output_dir: str):
    source_path = Path(source_dir)

    if not source_path.exists():
        print("this path does'n exist")
    elif not source_path.is_dir():
       print("this is not a directory")
    else:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        copy_files_move_to_new_dir(source_path, output_path)


def copy_file(file: Path, sub_folder: Path):
    shutil.copy2(file, sub_folder / file.name)


if __name__ == "__main__":
    main()