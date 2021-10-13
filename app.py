from logging import debug
from flask.globals import request
from models.api import Genius
from flask import Flask, render_template, jsonify
from lyricsgenius import Genius
import requests
import json


app = Flask(__name__)
genius = Genius('7BMof8cpcWNDATaOXEuFD5M49Kd4qo4e_heopr0IPpgt0sSR5-L1gjH6d12803uL')

@app.route("/songs", methods = ["GET"])
def songs():
    results = genius.artist_songs(request.args.get('artist_id'),
                                sort='popularity',
                                per_page=10
                                )
    return jsonify(results['songs'])

@app.route("/artist", methods = ["GET"]) 
def artist():
    artist_name = request.args.get('name')
    artist = genius.search_artist(artist_name, max_songs=1)
    artist_dict = {
        'id':artist.id,
        'name':artist.name,
    }
    return jsonify(artist_dict)


if __name__ == "__main__":
    app.run(debug=True)