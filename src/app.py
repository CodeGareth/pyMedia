from flask import Flask, render_template, jsonify, request
import requests
import json
import ast
import random

app = Flask(__name__)

@app.route("/")
def landing_page(): 

    return render_template("home.html")

## Ensure the end point matches the text casing in the js 
@app.route("/YouTube/<query>", methods = ['GET'])
def youtube_route(query):

    return jsonify({"search_term":query})

## Ensure the end point matches the text casing in the js 
@app.route("/Flickr/<query>/<number_request>", methods = ['GET'])
def flickr_route(query, number_request):

    ## Flickr public api will return a bytes string which needs to be converted 
    ## Thankfully it at least has the structure of json
    flickr_response = requests.get(f"https://www.flickr.com/services/feeds/photos_public.gne?format=json&tags={query}")

    ## Note - Using literal eval vs eval as safer 
    ## ref: https://docs.python.org/3/library/ast.html - search or ast.literal_eval 
    ## "Safely evaluate an expression node or a string containing a Python literal or container display. 
    ## The string or node provided may only consist of the following Python literal structures: strings, bytes, numbers, tuples, lists, dicts, sets, booleans, and None."
    converted_flickr_response = ast.literal_eval(flickr_response.content.decode('utf-8').replace("jsonFlickrFeed",""))

    random_selection_of_photos = random.choices(converted_flickr_response["items"], k = 3)
    breakpoint()


    return jsonify({"search_term":query, "total_photos":number_request, "results":random_selection_of_photos})

if __name__ == "__main__":

    app.run(debug=True)