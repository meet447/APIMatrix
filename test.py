import requests

url = "https://apimatrix.vercel.app/api/manga/comick/new/1"
rsponse = requests.get(url)
print(rsponse.json())