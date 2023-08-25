from flask import Flask, jsonify, request
from os import name
import json
import json_merge_patch

app = Flask(__name__)

# Anilist
# {'id': '', 'titulo' : '', 'poster' : '', 'categoria' : '', 'rating' : '', 'reviews' : '', 'season' : '', 'tipo' : ''}
lista = [{"id": 1000, "titulo": "Shingeki no Kyojin", "poster": "https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx16498-C6FPmWm59CyP.jpg", "categoria": "Action", "rating": 9, "reviews": 4588, "season": "Spring 2013", "tipo": "TV"}, 
        {"id": 1001, "titulo": "Kimetsu no Yaiba", "poster": "https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx101922-PEn1CTc93blC.jpg", "categoria": "Adventure", "rating": 8, "reviews": 1234, "season": "Spring 2019", "tipo": "TV"}, 
        {"id": 1002, "titulo": "DEATH NOTE", "poster": "https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx1535-lawCwhzhi96X.jpg", "categoria": "Mystery", "rating": 7, "reviews": 4567, "season": "Fall 2006", "tipo": "TV"}, 
        {"id": 1003, "titulo": "Boku no Hero Academia", "poster": "https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx21459-DUKLgasrgeNO.jpg", "categoria": "Action", "rating": 6, "reviews": 7899, "season": "Spring 2016", "tipo": "TV"}]


# Get /
@app.route('/')
def get():
    return "Bienvenido a Anilist"

# Get /anime
@app.route('/anime')
def get_list():
    return lista

# Get /anime/id
@app.route('/anime/<int:id>')
def get_anime(id):
    for anime in lista:
        if (anime['id'] == id):
            return anime
    return "Anime no encontrado"

# Post /anime
@app.post('/anime')
def post_anime():
    reqAnime = request.get_json()
    addAnime = {'id': reqAnime['id'] , 'titulo' : reqAnime['titulo'], 'poster' : reqAnime['poster'], 'categoria' : reqAnime['categoria'], 'rating' : reqAnime['rating'], 'reviews' : reqAnime['reviews'], 'season' : reqAnime['season'], 'tipo' : reqAnime['tipo']}
    lista.append(addAnime)
    return lista

# Put /anime/id
@app.route('/anime/<int:id>', methods = ['PUT'])
def put_anime(id):
    reqAnime = request.get_json()
    putAnime = {'id': reqAnime['id'] , 'titulo' : reqAnime['titulo'], 'poster' : reqAnime['poster'], 'categoria' : reqAnime['categoria'], 'rating' : reqAnime['rating'], 'reviews' : reqAnime['reviews'], 'season' : reqAnime['season'], 'tipo' : reqAnime['tipo']}

    for i in range (len(lista)):
        if lista[i]['id'] == id:
            lista[i] = putAnime
            return lista[i]
    return "Anime no encontrado PUT"


# Patch /anime/id
@app.route('/anime/<int:id>', methods = ['PATCH'])
def patch_anime(id):
    reqAnime = request.get_json()
    for i in range (len(lista)):
        if lista[i]['id'] == id:
            lista[i] = json_merge_patch.merge(lista[i], reqAnime)
            return lista[i]
    return "Anime no encontrado PATCH"


# Delete /anime/id
@app.route('/anime/<int:id>', methods = ['DELETE'])
def delete_anime(id):
    for anime in lista:
        if anime['id'] == id:
            lista.remove(anime)
            return lista
    return "Anime no encontrado"


if __name__ == '__main__':
    app.run()
  