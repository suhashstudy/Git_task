import git

repo = git.Repo(search_parent_directories=True)

# branches = list(repo.branches)

branches = [str(branch) for branch in repo.branches]

print(branches)

branch_name = input("Enter the branch name: ")

branch = repo.branches[branch_name]

tree = branch.commit.tree

directories = []

for entry in tree.trees:
    directories.append(entry.name)

print(directories)





