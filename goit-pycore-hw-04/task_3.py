from pathlib import Path

def visualize_directory_structure(directory_path):
    path = Path(directory_path)
    if not path.exists() or not path.is_dir():
        print(f"Error: Path '{directory_path}' is not a valid directory.")
        return
    
    def display_dir_content(dir_path, indent=0):
        for item in dir_path.iterdir():
            if item.is_dir():
                print(f"{' ' * indent}\033[94m{item.name}\033[0m")
                display_dir_content(item, indent + 2)
            else:
                print(f"{' ' * indent}\033[92m{item.name}\033[0m")

    print(f"Structure of '{directory_path}':")
    display_dir_content(path)

visualize_directory_structure("../goit-pycore-hw-04")
