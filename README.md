# Running on your own:

1. Get setup as a developer with Spotify so that you can use their API following the instructions here: https://developer.spotify.com/documentation/web-api

2. Create a copy of "config_template.py" called "config.py" and fill in the credentials

3. Start playing the playlist you'd like to do a powerhour to

4. Docker build and run. With ubuntu command line:
    docker buildx build --tag powerhour . && docker run --rm -it powerhour 
