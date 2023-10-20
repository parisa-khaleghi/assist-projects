from bs4 import BeautifulSoup

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
