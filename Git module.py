import os
from git import Repo

def get_branches(repository_path):
    repo = Repo(repository_path)
    branches = [branch.name for branch in repo.branches]
    return branches

def get_folders(repository_path, branch, folder_path=""):
    repo = Repo(repository_path)
    tree = repo.tree(branch, folder_path) if folder_path else repo.tree(branch)
    folders = [item.name for item in tree.traverse() if item.type == 'tree']
    return folders

def get_files(repository_path, branch, folder_path=""):
    repo = Repo(repository_path)
    tree = repo.tree(branch, folder_path) if folder_path else repo.tree(branch)
    files = [item.name for item in tree.traverse() if item.type == 'blob']
    return files

def get_file_content(repository_path, branch, file_path):
    repo = Repo(repository_path)
    blob = repo.blob(file_path, branch)
    return blob.data_stream.read().decode("utf-8")

# Replace this with the path to your local Git repository
repository_path = 'D:\Git\Git_task'

# Get the list of branches
branches = get_branches(repository_path)

if branches:
    print(f"Branches: {branches}")

    # Select a branch
    selected_branch = input("Enter the branch name: ")

    # Get the list of folders in the selected branch
    folders = get_folders(repository_path, selected_branch)

    if folders:
        print(f"Folders: {folders}")

        # Select a folder
        selected_folder = input("Enter the folder name: ")

        # Get the list of files in the selected folder
        files = get_files(repository_path, selected_branch, selected_folder)

        if files:
            print(f"Files: {files}")

            # Select a file
            selected_file = input("Enter the file name: ")

            # Get the content of the selected file
            file_content = get_file_content(repository_path, selected_branch, os.path.join(selected_folder, selected_file))

            if file_content:
                print(f"Content of {selected_folder}/{selected_file}:\n{file_content}")
