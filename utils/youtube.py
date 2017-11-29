import urllib
import jinja2
import csv

from apiclient.discovery import build
from optparse import OptionParser

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

# Set DEVELOPER_KEY to the "API key" value from the Google Developers Console:
# https://console.developers.google.com/project/_/apiui/credential
# Please ensure that you have enabled the YouTube Data API for your project.
with open ('api_keys.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        DEVELOPER_KEY = reader['Youtube']
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
app = Flask(__name__)

def search(search):
    youtube = build(
        YOUTUBE_API_SERVICE_NAME, 
        YOUTUBE_API_VERSION, 
        developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
        q="Hello",
        part="id,snippet",
        maxResults=5
        ).execute()

    videos = []
    
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"], 
            search_result["id"]["videoId"]))

    return videos