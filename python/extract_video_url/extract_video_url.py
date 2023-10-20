from git import repo
import datetime
import dateutil.tz
from bs4 import BeautifulSoup

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
    <p>Check out this embedded video:</p>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" frameborder="0" allowfullscreen></iframe>
    <p>And another one:</p>
    <iframe width="560" height="315" src="https://www.vimeo.com/embed/VIDEO_ID" frameborder="0" allowfullscreen></iframe>
</body>
</html>
"""

# Parse the HTML code with BeautifulSoup
soup = BeautifulSoup(html_code, 'html.parser')

# Find all iframe elements
iframes = soup.find_all('iframe')

# Extract video URLs from iframe src attributes
video_urls = [iframe['src'] for iframe in iframes]

# Print the extracted video URLs
for url in video_urls:
    print(url)


message = 'update: use BeautifulSoup to extract video links'

# call the function with custom data
commit(project_path, file_path, message, year, month, day, hour, minute)