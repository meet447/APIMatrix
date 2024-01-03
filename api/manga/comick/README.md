# API Documentation - Comick Manga Service

## Introduction

The Comick Manga Service API provides access to manga-related information, including top manga, hot releases, new releases, manga search, manga details, and chapter details. This documentation outlines the available endpoints and provides example codes and response formats.

**Base URL:** `https://apimatrix.vercel.app/`

## Endpoints


    
## Endpoints

| Endpoint                                    | Description                                     |
|---------------------------------------------|-------------------------------------------------|
| `/api/manga/comick/top`                     | Get top mangas                                   |
| `/api/manga/comick/hot/<page>`              | Get hot mangas (paginated)                       |
| `/api/manga/comick/new/<page>`              | Get new mangas (paginated)                       |
| `/api/manga/comick/search/<query>`          | Search mangas by title                           |
| `/api/manga/comick/comic/details/<slug>`    | Get details of a specific manga                  |
| `/api/manga/comick/chapter/<hid>`           | Get chapters of a manga                          |
| `/api/manga/comick/chapter/details/<hid>`   | Get details and images of a specific chapter    |

### 1. Get Top Mangas

- **Endpoint:** `/api/manga/comick/top`
- **Description:** Get top mangas

#### Example Code

```python
import requests

url = "https://apimatrix.vercel.app/api/manga/comick/top"
response = requests.get(url)
result = response.json()
print(result)
```

#### Response Format

```json
#format:
[
  {
    "slug": "one-piece",
    "title": "One Piece",
    "demographic": "Shonen",
    "content_rating": "Teen",
    "genres": ["Action", "Adventure", "Fantasy"],
    "last_chapter": 1040,
    "md_covers": [
      {"w": 300, "h": 450, "b2key": "image_key"}
    ]
  },
  // ... additional manga entries
]
```

### 2. Get Hot Mangas (Paginated)

- **Endpoint:** `/api/manga/comick/hot/<page>`
- **Description:** Get hot mangas (paginated)

#### Example Code

```python
import requests

url = "https://apimatrix.vercel.app/api/manga/comick/hot/1"
response = requests.get(url)
result = response.json()
print(result)
```

#### Response Format

```json
#format:
[
  {
    "id": 123,
    "status": "ongoing",
    "chap": 15,
    "vol": 2,
    // ... additional manga details
    "md_comics": {
      "id": 456,
      "hid": "comic_hid",
      "title": "Manga Title",
      "slug": "manga-slug",
      // ... additional comic details
      "md_covers": [
        {"w": 300, "h": 450, "b2key": "image_key"}
      ]
    }
  },
  // ... additional manga entries
]
```

### 3. Get New Mangas (Paginated)

- **Endpoint:** `/api/manga/comick/new/<page>`
- **Description:** Get new mangas (paginated)

#### Example Code

```python
import requests

url = "https://apimatrix.vercel.app/api/manga/comick/new/1"
response = requests.get(url)
result = response.json()
print(result)
```

#### Response Format

```json
#format:
[
  {
    "id": 789,
    "status": "completed",
    "chap": 50,
    "vol": 5,
    // ... additional manga details
    "md_comics": {
      "id": 101,
      "hid": "comic_hid",
      "title": "Another Manga Title",
      "slug": "another-manga-slug",
      // ... additional comic details
      "md_covers": [
        {"w": 300, "h": 450, "b2key": "image_key"}
      ]
    }
  },
  // ... additional manga entries
]
```

### 4. Search Mangas

- **Endpoint:** `/api/manga/comick/search/<query>`
- **Description:** Search mangas by title

#### Example Code

```python
import requests

url = "https://apimatrix.vercel.app/api/manga/comick/search/one_piece"
response = requests.get(url)
result = response.json()
print(result)
```

#### Response Format

```json
#format:
[
  {
    "id": 456,
    "hid": "manga_hid",
    "slug": "one-piece",
    "title": "One Piece",
    // ... additional manga details
    "md_covers": [
      {"w": 300, "h": 450, "b2key": "image_key"}
    ],
    "highlight": "Highlighted text"
  },
  // ... additional manga entries
]
```

### 5. Get Manga Details

- **Endpoint:** `/api/manga/comick/comic/details/<slug>`
- **Description:** Get details of a specific manga

#### Example Code

```python
import requests

url = "https://apimatrix.vercel.app/api/manga/comick/comic/details/one-piece"
response = requests.get(url)
result = response.json()
print(result)
```

#### Response Format

```json
#format:
{
  "firstChap": {
    "chap": 1,
    "hid": "chapter_hid",
    "lang": "en",
    // ... additional chapter details
  },
  "comic": {
    "id": 123,
    "hid": "manga_hid",
    "title": "One Piece",
    "country": "Japan",
    // ... additional manga details
    "links": {
      "al": "anilist_url",
      "ap": "anime-planet_url",
      "bw": "baka-updates_url"
    },
    "mal": "myanimelist_url",
    "raw": "raw_url",
    "last_chapter": 1040,
    "desc": "Manga description"
  }
}
```

### 6. Get Chapter Details and Images

- **Endpoint:** `/api/manga/comick/chapter/<hid>`
- **Description:** Get details and images of a specific chapter

#### Example Code

```python
import requests

url = "https://apimatrix.vercel.app/api/manga/comick/chapter

/details/chapter_hid"
response = requests.get(url)
result = response.json()
print(result)
```

#### Response Format

```json
#format:
{
  "chapters": [
    {
      "id": 1,
      "chap": 1,
      "title": "Chapter 1",
      // ... additional chapter details
      "md_chapters_groups": {
        "md_groups": {
          "title": "Group Title",
          "slug": "group-slug"
        }
      }
    },
    // ... additional chapter entries
  ]
}
```

Feel free to explore and integrate these functionalities into your application to enhance your manga-related features using the Comick Manga Service API. If you encounter any issues or have questions, refer to the [Comick API Documentation](https://apimatrix.vercel.app/) for additional details and support.