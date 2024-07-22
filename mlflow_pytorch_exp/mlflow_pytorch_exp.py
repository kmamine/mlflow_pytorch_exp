import argparse
import os
import shutil

def copy_template_files(dest_path):
    # Get the path to the templates directory
    templates_path = os.path.join(os.path.dirname(__file__), 'templates')

    # Copy the template files to the destination folder
    shutil.copytree(templates_path, dest_path)

def create_project(args):
    dest_path = args.folder
    if os.path.exists(dest_path):
        print(f"Error: Folder '{dest_path}' already exists.")
        return

    # Create the destination folder
    #os.makedirs(dest_path)

    # Copy the template files
    copy_template_files(dest_path)
    print(f"Project boilerplate created at '{dest_path}'.")

def main():
    parser = argparse.ArgumentParser(description="Create a PyTorch project with MLflow boilerplate.")
    subparsers = parser.add_subparsers(dest='command')

    # 'create' command
    create_parser = subparsers.add_parser('create', help='Create a new project boilerplate.')
    create_parser.add_argument('folder', type=str, help='Destination folder path for the new project.')

    args = parser.parse_args()

    if args.command == 'create':
        create_project(args)

if __name__ == "__main__":
    main()
