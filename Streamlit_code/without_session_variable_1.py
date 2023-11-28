import streamlit as st
from git import Repo
from functools import lru_cache

st.cache_resource()
def get_repo(local_repository_path):
    return Repo(local_repository_path)

st.cache_resource()
def get_branches(repo):
    branches = [branch.name for branch in repo.branches]
    return branches

st.cache_resource()
def get_folders(repo, branch, folder_path=""):
    commit = repo.commit(branch)
    tree = commit.tree
    if folder_path:
        parts = folder_path.split('/')
        for part in parts:
            tree = tree[part]
    folders = [item.name for item in tree.traverse() if item.type == 'tree']
    return folders

st.cache_resource()
def get_files(repo, branch, folder_path=""):
    commit = repo.commit(branch)
    tree = commit.tree
    if folder_path:
        parts = folder_path.split('/')
        for part in parts:
            tree = tree[part]
    files = [item.name for item in tree.traverse() if item.type == 'blob']
    return files

st.cache_resource()
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
    repo = get_repo(local_repository_path)

    branches = get_branches(repo)

    if branches:
        import streamlit as stm
        selected_branch = stm.radio("Select branch:", branches,index = None)

        folders = get_folders(repo, selected_branch)

        if folders and selected_branch  is not None :
            selected_folder = stm.selectbox("Select folder:", folders,index = None)

            files = get_files(repo, selected_branch, selected_folder)

            if files and selected_folder  is not None :
                selected_file = stm.selectbox("Select file:", files,index = None)

                if selected_file is not None:
                    file_content = get_file_content(repo, selected_branch, selected_folder + '/' + selected_file)
                    if file_content:
                        stm.write(f"Content of {selected_folder}/{selected_file}:")
                        stm.code(file_content, language='python')
            elif selected_folder is None:
                pass
            else:
                stm.warning("No files found in the selected folder.")
        elif selected_branch is None:
                pass
        else:
            stm.warning("No folders found.")
    else:
        st.error("Branches not found.")
