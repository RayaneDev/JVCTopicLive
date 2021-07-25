import urllib.request 
import bs4 as bs 
import vars 

def get_html(url) : 
    webUrl = urllib.request.urlopen(url)
    data = webUrl.read()
    return data.decode('utf-8')

def get_last_link() : 
    link = vars.soup.find_all('div', {'class': 'bloc-liste-num-page'})[0].find_all('span')[::-1]
    index = 1 if link[0].text == '»' else 0

    if len(link) > 1 and link[index].find('a') != None : 
        link = "https://www.jeuxvideo.com" + link[index].find('a')['href']
        return link 
    return None 

def get_new_posts():

  posts = []

  if vars.lastPost == False : 
    vars.lastPost = vars.soup.find_all('div', {'class' : 'bloc-message-forum'})[-1]['data-id']
  else : 
    
    messages = vars.soup.find_all('div', {'class' : 'bloc-message-forum'})
    record = False 
    for i in range (0, len(messages)) : 
        if record or vars.newPage : 
            post = []
            #post = messages[i].find_all('div', {'class' : 'txt-msg'})[0]
            post.append(messages[i].find('img', {'class' : 'user-avatar-msg'})['data-srcset'])
            post.append(messages[i].find('span', {'class' : 'bloc-pseudo-msg'}).text.rstrip().strip())
            post.append(messages[i].find('div', {'class' : 'bloc-date-msg'}).find('span').text)
            post.append(str(messages[i].find('div', {'class' : 'bloc-contenu'})))

            posts.append(post)
            vars.lastPost = messages[i]['data-id']
            

        if messages[i]['data-id'] == vars.lastPost : 
            record = True 
    vars.newPage = False 
    
    if len(messages) == 20 : 

        link = get_last_link() 

        if link != None : 
            vars.topax = link
            print(vars.topax)
            vars.newPage = True 

  vars.data = get_html(vars.topax)
  vars.soup = bs.BeautifulSoup(vars.data,'lxml')

  return posts




