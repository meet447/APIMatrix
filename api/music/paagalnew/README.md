# PaagalNew API Documentation

Welcome to the PaagalNew API documentation! This guide provides details on the available endpoints for retrieving information about songs, albums, and the latest releases from the PaagalNew website.

## Routes

| Endpoint                         |                                                              Description | Status  |  
|----------------------------------|--------------------------------------------------------------------------|---------|
| /paagalnew/song/search/<title>   | Search for songs on PaagalNew by title.                                  | Working |   
| /paagalnew/album/details/<album> | Retrieve details of an album on PaagalNew by album name.                 | Working |   
| /paagalnew/song/details/<href>   | Get detailed information about a song on PaagalNew by its href.          | Working |   
| /paagalnew/bollywood/<page>	   | Fetch the latest Bollywood songs on PaagalNew, paginated by page number. | Working |   

## 1. Search Songs

### Endpoint:

- **GET /api/music/paagalnew/song/search/<title>**

### Example:

#### Request:

```python
import requests

# Replace <title> with the desired song title
title = "shape of you"
url = f"http://127.0.0.1:5000/api/music/paagalnew/song/search/{title}"

response = requests.get(url)
data = response.json()

print(data)
```

#### Response:

```json
[
  {"title": "Song Title 1", "thumbnail": "URL1", "artist": "Artist 1", "href": "URL1"},
  {"title": "Song Title 2", "thumbnail": "URL2", "artist": "Artist 2", "href": "URL2"},
  ...
]
```

## 2. Search Albums

### Endpoint:

- **GET /api/music/paagalnew/album/details/<album>**

### Example:

#### Request:

```python
import requests

# Replace <album> with the desired album name
album = "golden"
url = f"http://127.0.0.1:5000/api/music/paagalnew/album/details/{album}"

response = requests.get(url)
data = response.json()

print(data)
```

#### Response:

```json
[
  {
    "album": {
      "title": "Album Title",
      "artists": ["Artist 1", "Artist 2"],
      "starcast": ["Star 1", "Star 2"],
      "composed_by": ["Composer 1", "Composer 2"],
      "year": "2022"
    },
    "songs": [
      {"title": "Song Title 1", "href": "URL1", "thumbnail": "URL1"},
      {"title": "Song Title 2", "href": "URL2", "thumbnail": "URL2"},
      ...
    ]
  }
]
```

## 3. Song Details

### Endpoint:

- **GET /api/music/paagalnew/song/details/<href>**

### Example:

#### Request:

```python
import requests

# Replace <href> with the desired song href
href = "song_href"
url = f"http://127.0.0.1:5000/api/music/paagalnew/song/details/{href}"

response = requests.get(url)
data = response.json()

print(data)
```

#### Response:

```json
[
  {
    "title": "Song Title",
    "thumbnail": "URL",
    "album": "Album Title",
    "singers": "Singer 1, Singer 2",
    "starcast": "Star 1, Star 2",
    "composer": "Composer 1, Composer 2",
    "mp3": "URL"
  }
]
```

## 4. Bollywood Songs

### Endpoint:

- **GET /api/music/paagalnew/bollywood/<page>**

### Example:

#### Request:

```python
import requests

# Replace <page> with the desired page number
page = 1
url = f"http://127.0.0.1:5000/api/music/paagalnew/bollywood/{page}"

response = requests.get(url)
data = response.json()

print(data)
```

#### Response:

```json
[
  {"title": "Song Title 1", "starcast": "Star 1", "artist": "Artist 1", "thumbnail": "URL1", "href": "URL1"},
  {"title": "Song Title 2", "starcast": "Star 2", "artist": "Artist 2", "thumbnail": "URL2", "href": "URL2"},
  ...
]
```

## Important Notes

- Customize the provided routes as needed for your application.

- Handle errors gracefully and provide suitable responses.

- Consider implementing additional security measures in a production environment.

Feel free to integrate these endpoints into your website and enhance your user experience with PaagalNew data!