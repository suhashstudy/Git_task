import streamlit as st
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
    st.title("Git Repository Explorer")

    local_repository_path = 'D:\Git\Git_task'
    repo = Repo(local_repository_path)

    branches = get_branches(repo)

    if branches:
        selected_branch = st.selectbox("Select branch:", branches,)

        folders = get_folders(repo, selected_branch)

        if folders and selected_branch  is not None :
            selected_folder = st.selectbox("Select folder:", folders,)

            files = get_files(repo, selected_branch, selected_folder)

            if files and selected_folder  is not None :
                selected_file = st.selectbox("Select file:", files,)

                file_content = get_file_content(repo, selected_branch, selected_folder + '/' + selected_file)

                if file_content:
                    st.write(f"Content of {selected_folder}/{selected_file}:")
                    st.code(file_content, language='python')
            else:
                st.warning("No files found in the selected folder.")
        else:
            st.warning("No folders found.")
    else:
        st.error("Branches not found.")

# if __name__ == "__main__":
#     main()
