Development Log 
===============

19/09/2021
----------

Starting the technical test just after 3pm today.

Plan: 
    * Intend to scope out the challenge, 
    * Generate the necessary api keys for Flickr and Youtube
    * Maybe build the simple html structure

Scoping: 
    * User needs a search box, video returned, up to 3 pictures returned
    * End points need to return 1 video, 3 pictures
    * Idea: Text Entry + toggle + if photo, number entry appears?

Notes:
    * For Youtube API Key - don't have to go OAuth because I don't care about personal info - just providing a search function
    * API keys collected and stored in a env file kept outside of the git repository
    * Seems I don't actually need a key for Flickr! The public photo feed seems open for all - with further research it seems an api key just expands the search terms

    * Having now built up the template I was thinking about - I now need to think how to submit the information to Flask
    * I like the idea of having flask handle it with one api end point - but to satisfy the brief I'll expand it to YouTube or Flask 
    * I'm going to use the user submitted values to help drive the api request
    * One submission form -> multiple end points

20/09/2021
----------

Updating this a day after...

Made a lot of progress with the app, having connected the two apis together with the app - Youtube and flask. 

On initial read, I had utilised the Youtube embedded api to return one video as a lucky dip, on second read seemed I need to allow the user to browser. In lieu of having
someone to clarify - I'll add both modes in :)

21/09/2021
----------

Plan today: 
    * Add the YouTube mode option - use it as a switch to dictate what template you're sent
    * Fill out a readme section?

Nice to have:

    * Handle a 404 request? 
    * Look to lock down the submit button if the necessary details haven't been completed?
    * Tidy the javascript up