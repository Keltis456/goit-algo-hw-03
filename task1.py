import os
import sys
import shutil


def parse_args():
    import argparse

    parser = argparse.ArgumentParser(
        description=(
            "Рекурсивно копіює файли та сортує їх у піддиректоріях "
            "за розширенням"
        )
    )
    parser.add_argument(
        'src',
        help="Шлях до вихідної директорії"
    )
    parser.add_argument(
        'dst',
        nargs='?',
        default='dist',
        help="Шлях до директорії призначення (за замовчуванням: dist)"
    )
    return parser.parse_args()


def copy_and_sort_files(src_dir, dst_dir):
    try:
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            if os.path.isdir(src_path):
                # Рекурсивно обходимо піддиректорію
                copy_and_sort_files(src_path, dst_dir)
            elif os.path.isfile(src_path):
                _, ext = os.path.splitext(item)
                ext = ext[1:] if ext else 'no_extension'
                dst_subdir = os.path.join(dst_dir, ext)
                os.makedirs(dst_subdir, exist_ok=True)
                dst_path = os.path.join(dst_subdir, item)
                try:
                    shutil.copy2(src_path, dst_path)
                except Exception as e:
                    print(
                        f"Не вдалося скопіювати файл {src_path} → "
                        f"{dst_path}: {e}"
                    )
    except Exception as e:
        print(
            f"Помилка при обробці директорії {src_dir}: {e}"
        )


def main():
    args = parse_args()
    src = os.path.abspath(args.src)
    dst = os.path.abspath(args.dst)
    if not os.path.isdir(src):
        print(f"Вихідна директорія не існує: {src}")
        sys.exit(1)
    if os.path.commonpath([src]) == os.path.commonpath([src, dst]):
        print(
            "Директорія призначення не повинна бути вкладеною у "
            "вихідну директорію!"
        )
        sys.exit(2)
    os.makedirs(dst, exist_ok=True)
    copy_and_sort_files(src, dst)
    print("Файли успішно скопійовано та відсортовано.")


if __name__ == "__main__":
    main()
