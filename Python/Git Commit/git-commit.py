from git import repo

r = repo.Repo("/Users/parisakhaleghi/Desktop/Coding/assist-projects", search_parent_directories=True)
print("=====you repository is '{}'".format(r))

r.index.add("git-commit.py")
r.index.commit('update: add commit')

origin = r.remotes[0]
origin.push()
