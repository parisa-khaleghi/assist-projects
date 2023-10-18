from git import repo
import datetime
import dateutil.tz

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
month = datetime.datetime.now().month-2
day = datetime.datetime.now().day
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute

# HTML code with embedded video
html_code = """
<html>
<body>
    <iframe src="https://player.vimeo.com/video/872245861?badge=0&amp;autopause=0&amp;quality_selector=1&amp;progress_bar=1&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Leap Year Savings">
    </iframe>
</body>
</html>
"""


message = 'update: reading embedded code'

# call the function with custom data
commit(project_path, file_path, message, year, month, day, hour, minute)