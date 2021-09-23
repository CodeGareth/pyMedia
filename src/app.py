import ast
import os
import random

import requests
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)

@app.route("/")
def landing_page(): 

    return render_template("home.html")

@app.route("/YouTube/<mode>/<query>", methods = ['GET'])
def youtube_route(mode, query):

    """Dependent on the mode selected by the user, return the appropiate template with the addition of wrangled youtube api search data"""

    youtube_search = requests.get(f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=21&q={query}&key={os.getenv('YOUTUBE_API')}")
    youtube_search_json_results = youtube_search.json()

    storage_collection = []

    ## Youtube Results return several types of links 
    ## For ease - filter only to videos and the elements we need to create our own browser screen
    for item in youtube_search_json_results["items"]:
        
        trimmed_item = {}
        
        if "video" not in item["id"]["kind"]:
            pass
        else:
            trimmed_item["id"] = item["id"]["videoId"]
            trimmed_item["description"] = item["snippet"]["description"]
            trimmed_item["title"] = item["snippet"]["title"]
            trimmed_item["medium_thumb"] = item["snippet"]["thumbnails"]["medium"]["url"]
    
            storage_collection.append(trimmed_item)

    if len(storage_collection) == 0: 
        return "No information present in storage collection - suggests YouTube API unable to return info based on your query - please change your search query and try again", 422
    elif mode == "Browse":
        ## FYI: For loop within template converts list of dicts to html
        return render_template("youtube_search_return.html", youtube_search_results = storage_collection)
    elif mode == "Watch":
        ## For ease, always return the first item from storage collection
        return render_template("youtube_watch.html", video_id = storage_collection[0]["id"])

@app.route("/Flickr/<number_request>/<query>", methods = ['GET'])
def flickr_route(query, number_request):

    """Dependent on the number of photos requested by the user, return the appropiate length array of images with pre-prepared html tags"""

    ## Flickr public api will return a bytes string with json format which needs to be converted 
    flickr_response = requests.get(f"https://www.flickr.com/services/feeds/photos_public.gne?format=json&tags={query}")

    ## Note - Using literal eval vs eval as safer 
    ## ref: https://docs.python.org/3/library/ast.html - search or ast.literal_eval 
    converted_flickr_response = ast.literal_eval(flickr_response.content.decode('utf-8').replace("jsonFlickrFeed",""))

    try: 

        ## Make a random selection from the list of available items
        random_selection_of_photos = random.choices(converted_flickr_response["items"], k = int(number_request))

        ## Convert this to html text with the intention of returning back to flask template iframe as is
        media = " ".join([f"<img src = {selection['media']['m']}></img>" for selection in random_selection_of_photos])

    except IndexError: 

        return "Converted flickr response is likely empty or does not contain the number of images you want to see - please change your search query and try again",422

    else:

        return render_template("flickr_return.html", media=media)

if __name__ == "__main__":

    app.run(debug=True)
