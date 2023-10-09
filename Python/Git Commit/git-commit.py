from git import repo

r = repo.Repo("/Users/parisakhaleghi/Desktop/Coding/assist-projects", search_parent_directories=True)
print("=====you repository is '{}'".format(r))

r.index.add("/Users/parisakhaleghi/Desktop/Coding/assist-projects/Python/Git Commit/git-commit.py")
r.index.commit('fix: change directory path')

origin = r.remotes[0]
origin.push()
