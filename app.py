from flask import *
from api.music.paagalnew.main import PaagalNew
from api.manga.comick.main import Comick
from api.llm.gpt4.main import gpt4
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
    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path) as file:
            return file.read()
    else:
        return "README not found", 404

@app.route("/api/<route>")
def api_docs(route, ):
    readme_path = f"api/{route}/README.md"
    if os.path.exists(readme_path):
        with open(readme_path) as file:
            return file.read()
    else:
        return "README not found", 404

@app.route("/api/<route>/<name>")
def file_docs(route, name):
    readme_path = f"api/{route}/{name}/README.md"
    if os.path.exists(readme_path):
        with open(readme_path) as file:
            return file.read()
    else:
        return "README not found", 404

#Music API

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


#Comick.cc start


    
@app.route("/api/manga/comick/top", methods=['POST', 'GET'])
def comick_top():
    return Comick.top_mangas()
    
@app.route("/api/manga/comick/hot/<page>", methods=['POST', 'GET'])
def comick_hot(page):
    return Comick.hot_mangas(page)

@app.route("/api/manga/comick/new/<page>", methods=['POST', 'GET'])
def comick_new(page):
    return Comick.new_mangas(page)

@app.route("/api/manga/comick/search/<query>", methods=['POST', 'GET'])
def comick_search(query):
    return Comick.search_mangas(query)

@app.route("/api/manga/comick/comic/details/<slug>", methods=['POST', 'GET'])
def comick_details(slug):
    return Comick.details_mangas(slug)

@app.route("/api/manga/comick/chapter/<hid>", methods=['POST', 'GET'])
def comick_chapter(hid):
    return Comick.chapters_mangas(hid)

@app.route("/api/manga/comick/chapter/details/<hid>", methods=['POST', 'GET'])
def comick_images(hid):
    return Comick.chapter_images(hid)

#Comick.cc End

@app.route("/api/llm/gpt4/bing/<message>")
def gpt_bard(message):
    response = gpt4.bing(message)
    return jsonify({"response": response})

#Manga Api End

