from flask import *
import requests
from api.music.paagalnew.main import PaagalNew
import os

app = Flask(__name__)

@app.route("/")
def index_page():
    return "running!"

@app.route("/home")
def id_page():
    return render_template("home.html")

@app.route("/api")
def api_page():
    return "api working"

#Music API

@app.route("/api/music")
def music_page():
    return "under construction docs"

@app.route("/api/music/<name>")
def music_docs(name):
    readme_path = f"app/api/music/{name}/README.md"
    if os.path.exists(readme_path):
        with open(readme_path) as file:
            return file.read()
    else:
        return "README not found", 404

#paagalnew start

@app.route("/api/music/paagalnew/song/search/<title>", methods=['POST', 'GET'])
def paagalnew_search(title):
    return PaagalNew.search_songs(title)
  
@app.route("/api/music/paagalnew/album/details/<album>", methods=['POST', 'GET'])
def paagalnewalbum_search(album):
    return PaagalNew.search_albums(album)
    
@app.route("/api/music/paagalnew/song/details/<href>", methods=['POST', 'GET'])
def paagalnew_details(href):
    return PaagalNew.details_song(href)

    
@app.route("/api/music/paagalnew/bollywood/<page>", methods=['POST', 'GET'])
def paagalnew_bollywood(page):
    return PaagalNew.bollywood_songs(page)

#paagalnew end

#Music Api End

app.run(host="0.0.0.0", debug=True)