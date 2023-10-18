from git import repo
import datetime
import dateutil.tz

r = repo.Repo("/Users/parisakhaleghi/Desktop/Coding/assist-projects", search_parent_directories=True)
# print("=====you repository is '{}'".format(r))

# print(datetime.datetime.now()-datetime.timedelta(minutes=5))
# print(datetime.now(datetime.timezone.utc))

# print(datetime.datetime(2016, 10, 4, 12, 13, tzinfo=dateutil.tz.tzoffset(u'CEST', -7200)))

r.index.add("/Users/parisakhaleghi/Desktop/Coding/assist-projects/Python/Git Commit/git-commit.py")
r.index.commit('test: fixing error to commit for 5 min earlier', 
               commit_date=datetime.datetime(2016, 10, 4, 12, 13, tzinfo=dateutil.tz.tzoffset(u'CEST', -7200)))

origin = r.remotes[0]
origin.push()
