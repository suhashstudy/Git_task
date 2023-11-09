import git

repo = git.Repo(search_parent_directories=True)

branches = list(repo.branches)

branch_name = input("Enter the branch name: ")

branch = repo.branches[branch_name]

# tree = branch.commit.tree

# contents = []
# for blob in tree.blobs:
#     contents.append(blob.name)

# print(contents)

commit_hash = branch.commit.hexsha

commit_iterator = repo.iter_commits(commit_hash)

directories = []
for commit in commit_iterator:
    tree = commit.tree
    print(tree.blobs)

    # for blob in tree.blobs:
    #     if blob.name.endswith("/"):
    #         directories.append(blob.name[:-1])






