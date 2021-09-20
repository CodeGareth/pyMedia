from flask import Flask, render_template
import requests
import ast
import random
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route("/")
def landing_page(): 

    return render_template("home.html")

## Ensure the end point matches the text casing in the js 
@app.route("/YouTube/<query>", methods = ['GET'])
def youtube_route(query):

    youtube_search = requests.get(f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q={query}&key={os.getenv('YOUTUBE_API')}")
    youtube_search_json_results = youtube_search.json()

    video_id = youtube_search_json_results["items"][0]["id"]["videoId"]
    print (video_id)

    return render_template("youtube_return.html", video_id = video_id)

## Ensure the end point matches the text casing in the js 
@app.route("/Flickr/<query>/<number_request>", methods = ['GET'])
def flickr_route(query, number_request):

    ## Flickr public api will return a bytes string which needs to be converted 
    ## Thankfully it at least has the structure of json
    flickr_response = requests.get(f"https://www.flickr.com/services/feeds/photos_public.gne?format=json&tags={query}")

    ## Note - Using literal eval vs eval as safer 
    ## ref: https://docs.python.org/3/library/ast.html - search or ast.literal_eval 
    converted_flickr_response = ast.literal_eval(flickr_response.content.decode('utf-8').replace("jsonFlickrFeed",""))

    ## Make a random selection from the list of available items
    random_selection_of_photos = random.choices(converted_flickr_response["items"], k = int(number_request))

    ## Convert this to html text with the intention of returning back to flask template iframe
    media = " ".join([f"<img src = {selection['media']['m']}></img>" for selection in random_selection_of_photos])

    #return jsonify({"search_term":query, "total_photos":number_request, "results":random_selection_of_photos})
    return render_template("flickr_return.html", media=media)

if __name__ == "__main__":

    app.run(debug=True)
