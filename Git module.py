from git import Repo

def get_branches(repo):
    branches = [branch.name for branch in repo.branches]
    return branches

def get_folders(repo, branch, folder_path=""):
    commit = repo.commit(branch)
    tree = commit.tree
    if folder_path:
        parts = folder_path.split('/')
        for part in parts:
            tree = tree[part]
    folders = [item.name for item in tree.traverse() if item.type == 'tree']
    return folders

def get_files(repo, branch, folder_path=""):
    commit = repo.commit(branch)
    tree = commit.tree
    if folder_path:
        parts = folder_path.split('/')
        for part in parts:
            tree = tree[part]
    files = [item.name for item in tree.traverse() if item.type == 'blob']
    return files

def get_file_content(repo, branch, file_path):
    commit = repo.commit(branch)
    tree = commit.tree
    parts = file_path.split('/')
    for part in parts:
        tree = tree[part]
    file_content = repo.git.show(tree)
    return file_content

# Replace this with the path to your local Git repository
local_repository_path = 'D:\Git\Git_task'
repo = Repo(local_repository_path)

# Get the list of branches
branches = get_branches(repo)

if branches:
    print(f"Branches: {branches}")

    # Select a branch
    selected_branch = input("Enter the branch name: ")

    # Get the list of folders in the selected branch
    folders = get_folders(repo, selected_branch)

    if folders:
        print(f"Folders: {folders}")

        # Select a folder
        selected_folder = input("Enter the folder name: ")

        # Get the list of files in the selected folder
        files = get_files(repo, selected_branch, selected_folder)

        if files:
            print(f"Files: {files}")

            # Select a file
            selected_file = input("Enter the file name: ")

            # Get the content of the selected file
            file_content = get_file_content(repo, selected_branch, selected_folder + '/' + selected_file)

            if file_content:
                print(f"Content of {selected_folder}/{selected_file}:\n{file_content}")
    else:
        print("No folders found.")
