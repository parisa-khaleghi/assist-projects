from git import repo
import datetime

r = repo.Repo("/Users/parisakhaleghi/Desktop/Coding/assist-projects", search_parent_directories=True)
# print("=====you repository is '{}'".format(r))

print(datetime.datetime)

r.index.add("/Users/parisakhaleghi/Desktop/Coding/assist-projects/Python/Git Commit/git-commit.py")
r.index.commit('update: check date-time')

origin = r.remotes[0]
origin.push()
