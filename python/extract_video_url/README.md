# Extracting Video URLs from HTML with BeautifulSoup

This Python script demonstrates how to use the BeautifulSoup library to parse HTML content and extract video URLs from embedded iframes. 

## HTML Code

The HTML code provided in the script contains embedded video iframes from YouTube and Vimeo. You can replace these iframe sources with the URLs of the videos you want to extract.

```html
<html>
<body>
    <p>Check out this embedded video:</p>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" frameborder="0" allowfullscreen></iframe>
    <p>And another one:</p>
    <iframe width="560" height="315" src="https://www.vimeo.com/embed/VIDEO_ID" frameborder="0" allowfullscreen></iframe>
</body>
</html>
```

# How It Works

1. The script begins by importing the BeautifulSoup library, which is used for parsing HTML content.
2. It defines the html_code variable, which holds the HTML content that contains embedded video iframes. You can replace the src attribute values with the URLs of the videos you want to extract.
3. The HTML code is parsed using BeautifulSoup with the 'html.parser' option, creating a BeautifulSoup object named soup.
4. The script finds all iframe elements within the HTML using soup.find_all('iframe').
5. It then extracts the video URLs from the src attributes of the iframes and stores them in the video_urls list.
6. Finally, the script prints the extracted video URLs to the console.


This script is a starting point for extracting video URLs from HTML content and can be customized to suit your specific needs.
