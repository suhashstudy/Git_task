import git

repo = git.Repo(search_parent_directories=True)

branches = list(repo.branches)

print(branches)

