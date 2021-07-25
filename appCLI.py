import urllib.request 
import bs4 as bs 
import threading

topax = "https://www.jeuxvideo.com/forums/42-51-67196854-1-0-1-0-direct-le-senat-examine-la-loi-pass-sanitaire.htm"

def get_html(url) : 
    webUrl = urllib.request.urlopen(topax)
    data = webUrl.read()
    return data.decode('utf-8')

def get_last_link() : 
    link = soup.find_all('div', {'class': 'bloc-liste-num-page'})[0].find_all('span')[::-1]
    index = 1 if link[0].text == '»' else 0

    if len(link) > 1 and link[index].find('a') != None : 
        link = "https://www.jeuxvideo.com" + link[index].find('a')['href']
        return link 
    return None 

data = get_html(topax)

# On va à la dernière page 

soup = bs.BeautifulSoup(data,'lxml')
link = get_last_link() 

if link != None : 
    topax = link 
    data = get_html(topax)

delay = 5.0 # Délai en secondes 
lastPost = False # ID du dernier post 
posts = []
newPage = False 

def get_new_posts():
  global lastPost, data, bs, soup, newPage, topax
  threading.Timer(delay, get_new_posts).start()

  if lastPost == False : 
    lastPost = soup.find_all('div', {'class' : 'bloc-message-forum'})[-1]['data-id']
  else : 
    
    messages = soup.find_all('div', {'class' : 'bloc-message-forum'})
    record = False 
    for i in range (0, len(messages)) : 
        if record or newPage : 
            post = messages[i].find_all('div', {'class' : 'txt-msg'})[0].find_all('p')[-1].text
            posts.append(post)
            lastPost = messages[i]['data-id']

            print (post, "\n===========================================================")
            

        if messages[i]['data-id'] == lastPost : 
            record = True 
    newPage = False 
    
    if len(messages) == 20 : 

        link = get_last_link() 

        if link != None : 
            topax = link
            print(topax)
            newPage = True 

  data = get_html(topax)
  soup = bs.BeautifulSoup(data,'lxml')

get_new_posts()




