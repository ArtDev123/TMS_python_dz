import os
import shutil
from typing import Dict, List, Tuple


def get_os_name() -> str:
    return os.name


def get_current_path() -> str:
    return os.getcwd()


def group_files_by_extension() -> None:
    current_dir: str = os.getcwd()
    files: List[str] = [
        f
        for f in os.listdir(current_dir)
        if os.path.isfile(os.path.join(current_dir, f))
    ]

    extension_dirs: Dict[str, List[str]] = {}
    total_files_moved: int = 0
    total_size_bytes: int = 0

    for file in files:
        name, ext = os.path.splitext(file)
        ext = ext.lower()

        if not ext:
            continue

        if ext not in extension_dirs:
            os.makedirs(ext[1:], exist_ok=True)
            extension_dirs[ext] = []

        dest_dir: str = ext[1:]
        new_name: str = file

        if len(extension_dirs[ext]) == 0:
            new_name = f"some_{name}{ext}"
            print(f"Файл {file} был переименован в {new_name}")
        else:
            new_name = file

        old_path: str = os.path.join(current_dir, file)
        new_path: str = os.path.join(current_dir, dest_dir, new_name)
        shutil.move(old_path, new_path)

        extension_dirs[ext].append(new_name)
        total_files_moved += 1
        total_size_bytes += os.path.getsize(new_path)

    for ext, files_in_ext in extension_dirs.items():
        size_gb: float = sum(
            os.path.getsize(os.path.join(ext[1:], f)) for f in files_in_ext
        ) / (1024**3)
        print(
            f"в папке с {ext} файлами перемещено {len(files_in_ext)} файлов,"
            f"их суммарный размер - {size_gb:.2f} гигабайт"
        )


def main() -> None:
    os_name: str = get_os_name()
    print(f"Имя вашей ОС: {os_name}")

    current_path: str = get_current_path()
    print(f"Путь до текущей папки: {current_path}")

    group_files_by_extension()


if __name__ == "__main__":
    main()
