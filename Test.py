import git

repo = git.Repo(search_parent_directories=True)

branches = list(repo.branches)

branch_name = input("Enter the branch name: ")

branch = repo.branches[branch_name]

tree = branch.commit.tree

contents = []
for blob in tree.blobs:
    contents.append(blob.name)

print(contents)


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



