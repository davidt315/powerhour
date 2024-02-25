FROM python

RUN apt-get update && python -m ensurepip --upgrade && \
    pip install spotipy --upgrade

COPY config.py /config.py
COPY powerhour.py /powerhour.py
COPY spotify_data.py /spotify_data.py

ENTRYPOINT [ "python3", "powerhour.py" ]
