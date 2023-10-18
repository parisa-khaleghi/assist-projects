from git import repo
import datetime
import dateutil.tz
from dateutil.relativedelta import relativedelta



# function to commit in costum date
def commit(project_path, file_path, message, year, month, day, hour, minute):
    r = repo.Repo(project_path, search_parent_directories=True)
    r.index.add(file_path)
    r.index.commit(message, commit_date=datetime.datetime(year, month, day, hour, minute, tzinfo=dateutil.tz.tzoffset(u'TRT', 3*3600)))
    origin = r.remotes[0]
    origin.push()

# fill out information for project path and file path on your system
project_path = "/Users/parisakhaleghi/Desktop/Coding/assist-projects"
file_path = "/Users/parisakhaleghi/Desktop/Coding/assist-projects/Python/Extract video url/extract-video-url.py"

# fill out information for commiting
year = datetime.datetime.now().year
month = datetime.datetime.now()-relativedelta(months=2)
day = datetime.datetime.now().day
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute






message = 'init: create the file and add primary codes'

# call the function with custom data
commit(project_path, file_path, message, year, month, day, hour, minute)