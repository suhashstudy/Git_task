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


def calling_function():
    local_repository_path = 'D:\Git\Git_task'
    repo = Repo(local_repository_path)

    branches = get_branches(repo)

    if branches:
        print(f"Branches: {branches}")

        selected_branch = input("Enter the branch name: ")

        folders = get_folders(repo, selected_branch)

        if folders:
            print(f"Folders: {folders}")

            selected_folder = input("Enter the folder name: ")

            files = get_files(repo, selected_branch, selected_folder)

            if files:
                print(f"Files: {files}")

                selected_file = input("Enter the file name: ")

                file_content = get_file_content(repo, selected_branch, selected_folder + '/' + selected_file)

                if file_content:
                    print(f"Content of {selected_folder}/{selected_file}:\n{file_content}")
        else:
            print("No folders found.")
        
    else:
        print("Branches not found")

# if __name__ == '__main__':
#     calling_function()