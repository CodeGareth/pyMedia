from flask import Flask, render_template, jsonify, request

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

    return jsonify({"search_term":query, "total_photos":number_request})

if __name__ == "__main__":

    app.run(debug=True)