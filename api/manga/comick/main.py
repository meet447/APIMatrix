import requests

class Comick:
    
    base_domain = "https://comick.cc/"
    api_domain = "https://api.comick.cc/"
    
    Headers = {
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'Referer': 'https://comick.cc/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    }   
    
    def top_mangas():
        
        #format:
        #{slug,title,demographic,content_rating,genres:[],last_chapter,md_covers:[{}]}
        
        url = Comick.api_domain + "top?accept_mature_content=true"
        response = requests.get(url, headers=Comick.Headers)
        result  = response.json()
        return result        
    
    def hot_mangas(page):
        
        #format:
        #{id,status,chap,vol,last_at,hid,created_at,group_name:[],updated_at,upcount,lang,down_count,md_comics:{id,hid,title,slug,content_rating,country,status,translation_completed,last_chapter,created_at,genres:[],demographic,md_covers:[{w,h,b2key}]}}
        
        url =f"{Comick.api_domain}chapter?lang=en&accept_erotic_content=true&page={page}&device-memory=4&order=hot"
        response = requests.get(url, headers=Comick.Headers)
        result  = response.json()
        return result  
        
    def new_mangas(page):
        
        #format:
        #{id,status,chap,vol,last_at,hid,created_at,group_name:[],updated_at,upcount,lang,down_count,md_comics:{id,hid,title,slug,content_rating,country,status,translation_completed,last_chapter,created_at,genres:[],demographic,md_covers:[{w,h,b2key}]}}
        
        url =f"{Comick.api_domain}chapter?lang=en&accept_erotic_content=true&page={page}&device-memory=4&order=new"
        response = requests.get(url, headers=Comick.Headers)
        result  = response.json()
        return result  
    
    def search_mangas(title):
        
        #format:
        #{id,hid,slug,title,md_titles:[{title}],md_covers:[{w,h,b2key}],highlight}
        
        url = f"{Comick.api_domain}v1.0/search?q={title}&t=true"
        response = requests.get(url, headers=Comick.Headers)
        result  = response.json()
        return result  
    
    def chapters_mangas(hid):
        
        #format:
        #{chapters:[{id,chap,title,vol,lang,created_at,updated_at,up_count,down_count,group_name:[],hid,identities:{id,traits:{username,getavatar}},md_chapters_groups:{md_groups:{title,slug}}}]}
        
        url = f"{Comick.api_domain}comic/{hid}/chapters?lang=en"
        response = requests.get(url, headers=Comick.Headers)
        result  = response.json()
        return result  
    
    def details_mangas(slug):
        
        #{firstChap:{chap,hid,lang,group_name:[],vol},comic:{id,hid,title,country,status,links:{al,ap,bw},mal,raw,last_chapter,desc}}
        url = f"https://api.comick.cc/comic/{slug}/?tachiyomi=false"
        response = requests.get(url, headers=Comick.Headers)
        result  = response.json()
        return result  
    
    def chapter_images(hid):
        url = f"https://api.comick.cc/chapter/{hid}/?tachiyomi=false"
        response = requests.get(url, headers=Comick.Headers)
        result  = response.json()
        return result  
    
