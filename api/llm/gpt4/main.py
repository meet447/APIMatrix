import requests

class gpt4:
    def bing(message):
        url = f"https://api.freegpt4.ddns.net/?text={message}"
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            return response.text
        else:
            return response.json()
            
            
            