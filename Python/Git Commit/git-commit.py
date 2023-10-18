from git import repo
import datetime
import dateutil.tz


# def commit(message, year, month, day, hour, minute, )
r = repo.Repo("/Users/parisakhaleghi/Desktop/Coding/assist-projects", search_parent_directories=True)
r.index.add("/Users/parisakhaleghi/Desktop/Coding/assist-projects/Python/Git Commit/git-commit.py")
r.index.commit('update: change timezone to turkey', 
            commit_date=datetime.datetime(2016, 10, 4, 12, 15, tzinfo=dateutil.tz.tzoffset(u'TRT', 3*3600)), )

origin = r.remotes[0]
origin.push()
