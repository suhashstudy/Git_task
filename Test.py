import git

repo = git.Repo(search_parent_directories=True)

branches = list(repo.branches)

branch_name = input("Enter the branch name: ")

branch = repo.branches[branch_name]

# folders = [f.name for f in branch.commit.tree.blobs if f.is_dir()]

tree = branch.commit.tree

directories = []
for blob in tree.blobs:
    if blob.name.endswith("/"):
        directories.append(blob.name[:-1])

print(tree.blobs)


# for f in branch:
#     print(branch)

# print("Folders in branch '%s':" % branch_name)
# print(folders)

# extracted_branch_names = []

# for branch_name in branches:
#     print(branch_name)
#     # split_branch_name = branch_name.rsplit('/', 1)

#     # extracted_branch_name = split_branch_name[-1].replace('\"', '')

#     # extracted_branch_names.append(extracted_branch_name)

# # print(extracted_branch_names)



