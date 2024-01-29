import shutil
import os

def delete_pycache_on_exit():
    def delete_pycache(folder):
        pycache_path = os.path.join(folder, "__pycache__")
        if os.path.exists(pycache_path):
            try:
                shutil.rmtree(pycache_path)
                print(f"Deleted __pycache__ folder: {pycache_path}")
            except Exception as e:
                print(f"Error deleting __pycache__ folder: {e}")

    # Delete __pycache__ in the current working directory
    delete_pycache(os.getcwd())

    # Delete __pycache__ in subdirectories (e.g., tools/__pycache__)
    for root, dirs, files in os.walk(os.getcwd()):
        for directory in dirs:
            delete_pycache(os.path.join(root, directory))
