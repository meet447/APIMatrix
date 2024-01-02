import requests
from bs4 import BeautifulSoup

class PaagalNew:
    @staticmethod
    def search_albums(album):
        url = f"https://pagalnew.com/album/{album}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        data = {'album': {}, 'songs': []}

        # Extract album information
        album_title_tag = soup.find('h1', class_='main_page_category_div up')
        if album_title_tag:
            album_title = album_title_tag.text.strip()
        else:
            album_title = None

        artists_tag = soup.find('b', string='Artists:')
        artists = artists_tag.find_next('b').text.strip().split(' - ') if artists_tag else None

        starcast_tag = soup.find('b', string='Starcast:')
        starcast = starcast_tag.find_next('b').text.strip().split('    ') if starcast_tag else None

        composed_by_tag = soup.find('b', string='Composed by:')
        composed_by = composed_by_tag.find_next('b').text.strip().split('                      ') if composed_by_tag else None

        year_tag = soup.find('b', string='Year:')
        year = year_tag.find_next('b').text.strip() if year_tag else None

        data['album'] = {
            'title': album_title,
            'artists': artists,
            'starcast': starcast,
            'composed_by': composed_by,
            'year': year
        }

        # Extract song information
        song_divs = soup.find_all('div', class_='col-lg-6 col-md-6 col-sm-12 col-xs-12 main_page_category_music')
        
        for song_div in song_divs:
            song_info = {}

            title_tag = song_div.find('div', style='color:#000000; font-weight:700;')
            title = title_tag.text.strip() if title_tag else None

            href_tag = song_div.find('a')
            href = href_tag['href'] if href_tag and 'href' in href_tag.attrs else None

            thumbnail_tag = song_div.find('img', class_='b-lazy')
            thumbnail = thumbnail_tag['data-src'] if thumbnail_tag and 'data-src' in thumbnail_tag.attrs else None

            if title and href and thumbnail:
                song_info['title'] = title
                song_info['href'] = href
                song_info['thumbnail'] = thumbnail

                data['songs'].append(song_info)

        return data

# Example usage:
result = PaagalNew.search_albums("animal-2023.html")
if result:
    print(result)
else:
    print("Error retrieving album data.")
