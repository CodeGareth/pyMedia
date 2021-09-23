# pyMedia 🎥 📸

pyMedia is a developer test project, designed to utilise different APIs and show handling between both front end and back end requests. 

## Summary
Designed using Python 3.8.3 on Windows, this Flask based project features my own front-end page and utilises two forms of YouTube APIs, as well as the Flickr Public Feed Api. 

API References: 

1. [YouTube Search List API - Documentation](https://developers.google.com/youtube/v3/docs/search/list)
2. [YouTube iFrame Player API - Documentation](https://developers.google.com/youtube/iframe_api_reference)
3. [Flickr Public Feed API - Documentation](https://www.flickr.com/services/feeds/docs/photos_public/)
 
To help with front end design - [Bootstrap](https://getbootstrap.com/) was used to help structure and provide elements to interact with such as the drop down lists and submit button. 

My own custom javascript was written to add functionality such as hide and appear drop down boxes based on which mode is selected. 

## Installation

As this is designed to be ran locally, the recommended way to run this is to:

1. Download this repo to your own local machine - you can use this [link](https://github.com/CodeGareth/pyMedia/archive/refs/heads/main.zip) to download this repo as a zip file.
  * If using the zip download, ensure you unzip all files into a new folder - you should expect to see a folder called "pyMedia-main" be created containing the project repo
2. Open your preferred terminal of choice and change the working directory to the place you copied the repo to e.g the newly unzipped project folder
* If using Windows, you can click in the address bar of the folder, delete everything in there, type the letters cmd and hit enter. A useful trick to open up command prompt 
3. Create and activate a virtual environment so you can run the app from the project folder

*    ```bash
     python -m venv env
     "env/scripts/activate"
     ```
4. Once activated, use pip to install the same modules and versions I used to design this project

*    ```bash
     pip install -r requirements.txt
     ```
5. Once installed, you will now need to update the .env file with your own YouTube API Key. Follow these instructions [here](https://developers.google.com/youtube/v3/getting-started) to generate your own. The file will look something like this once updated:

*    ```bash
     YOUTUBE_API = "REALLYL0NGNuMBER"
     ```

6. Once complete, you should now be able to run the Flask app: 

*    ```bash
     python src/app.py
     ```

## License
[MIT](https://choosealicense.com/licenses/mit/)
