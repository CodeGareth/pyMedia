from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def landing_page(): 

    return render_template("home.html")

## Ensure the end point matches the text casing in the js 
@app.route("/YouTube", methods = ['GET'])
def youtube_route():

    return jsonify({"message":"awesome"})

if __name__ == "__main__":

    app.run(debug=True)