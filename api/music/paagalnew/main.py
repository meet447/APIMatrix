import requests
from bs4 import BeautifulSoup

class PaagalNew:
    
    def search_songs(title):
        
        #format:
        #{href,name,artist,thumbnail}
        result_list = []
        url = f"https://pagalnew.com/search.php?find={title}"
        response = requests.get(url)
        result = response.text
        soup = BeautifulSoup(result, 'html.parser')
        song_containers = soup.find_all('div', class_='main_page_category_music_box')

        # Iterate through each song container and extract information
        for song in song_containers:
            title = song.find('b').text.strip()
            thumbnail = song.find('img')['src']
            artist_div = song.find_next('div')
            artist = artist_div.find_next('div').text.strip()
            href = song.find_parent('a')['href']

            # Create a dictionary with the extracted information
            song_info = {
                'title': title,
                'thumbnail': thumbnail,
                'artist': artist,
                'href': href
            }

            # Append the dictionary to the result list
            result_list.append(song_info)   
            
        return result_list            
    
    def details_song(href):
        #format:
        #{title,album,singers,starcast,composer,mp3}
        
        url = f"https://pagalnew.com/songs/{href}"
        response = requests.get(url)
        result = response.text
        
        soup = BeautifulSoup(result, 'html.parser')
        
        print(soup.prettify())

        # Extracting information
        title = soup.find('h1', class_='main_page_category_div').text.strip()

        # Checking if the element exists before calling find_next
        album_element = soup.find('b', string='Album:')
        album = album_element.get_text() if album_element else None

        singers_element = soup.find('b', string='Singer(s):')
        singers = singers_element.find_next('b').text.strip() if singers_element else None

        starcast_element = soup.find('b', string='Starcast:')
        starcast = starcast_element.find_next('b').text.strip() if starcast_element else None

        composer_element = soup.find('b', string='Composer:')
        composer = composer_element.find_next('b').text.strip() if composer_element else None

        mp3 = soup.find('audio')['src']
        
        thumbnail_element = soup.find('img', class_='b-lazy')
        thumbnail = thumbnail_element['data-src'] if thumbnail_element else None

        # Creating a dictionary with the extracted information
        song_details = {
            'title': title,
            'thumbnail':thumbnail,
            'album': album,
            'singers': singers,
            'starcast': starcast,
            'composer': composer,
            'mp3': mp3
        }

        return song_details
    
    def latest_songs():
        # format:
        # {title, starcast, artist, genre, href, thumbnail}
        latest_releases = []

        url = "https://pagalnew.com/"
        response = requests.get(url)
        result = response.text
        
        soup = BeautifulSoup(result, 'html.parser')
        latest_release_divs = soup.find_all('div', class_='col-lg-6 col-md-6 col-sm-12 col-xs-12 main_page_category_music')

        for release in latest_release_divs:
            latest_release_title_tag = release.find('h2')
            latest_release_title = latest_release_title_tag.text.strip() if latest_release_title_tag else ''

            starcast_tag = release.find_all('p')[0] if len(release.find_all('p')) > 0 else None
            starcast = starcast_tag.text.strip() if starcast_tag else ''

            artist_tag = release.find_all('p')[1] if len(release.find_all('p')) > 1 else None
            artist = artist_tag.text.strip() if artist_tag else ''

            genre_tag = release.find('p', style='color:#333; font-size:small;')
            genre = genre_tag.text.strip() if genre_tag else ''
            
            href_tag = release.find('a')
            href = href_tag.get('href') if href_tag else ''

            thumbnail_tag = release.find('img', class_='b-lazy')
            thumbnail = thumbnail_tag.get('data-src') if thumbnail_tag else ''

            latest_release_info = {
                'title': latest_release_title,
                'starcast': starcast,
                'artist': artist,
                'genre': genre,
                'thumbnail':thumbnail,
                'href':href,
            }

            latest_releases.append(latest_release_info)

        return latest_releases

    def bollywood_songs(page):
        # format:
        # {title, starcast, artist, genre, href, thumbnail}
        
        latest_releases = []

        url = f"https://pagalnew.com/category/bollywood-mp3-songs/{page}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return latest_releases

        soup = BeautifulSoup(response.text, 'html.parser')
        song_divs = soup.find_all('div', class_='main_page_category_music_box')
        
        for song_div in song_divs:
            title_info = song_div.find('div', style='color:#000000; font-weight:700;')
            title = title_info.text.strip() if title_info else ''

            starcast_info = song_div.find('div', style='font-weight:500;')
            starcast = starcast_info.text.strip() if starcast_info else ''

            # Assuming artist is the next div after starcast
            artist_info = starcast_info.find_next('div', style='font-weight:500;')
            artist = artist_info.text.strip() if artist_info else ''

            # Assuming you want the source attribute of the <img> tag for the thumbnail
            thumbnail_tag = song_div.find('img', src=True)
            thumbnail = thumbnail_tag['src'] if thumbnail_tag else ''

            # Extracting href from the parent div
            parent_div = song_div.find_parent('div', class_='col-lg-6 col-md-6 col-sm-12 col-xs-12 main_page_category_music')
            href_tag = parent_div.find('a', href=True)
            href = href_tag['href'] if href_tag and 'href' in href_tag.attrs else ''

            song_info = {
                'title': title,
                'starcast': starcast,
                'artist': artist,
                'thumbnail': thumbnail,
                'href': href,
            }

            latest_releases.append(song_info)

        return latest_releases

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
        
