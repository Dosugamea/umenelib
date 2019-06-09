import requests,datetime,random,string,urllib

def ciplex(word):
    list = []
    r = ''
    for i in range (0, len(word)):
        if word[i].islower():
            list.insert(i, chr(219-ord(word[i])))
        else:
            list.insert(i, word[i])
    for ii in range (0, len(word)):
        r += list[ii]
    return r

def ozichat(name,emoji=3,punctiuation=1):
    payload = {'name': name, 'emoji_level': emoji, "punctiuation_level": punctiuation}
    r = requests.post("https://ojichat.appspot.com/post", data=payload)
    data = r.json()
    return data['message']

def bitly(token,url):
    token = token
    query = {
            'access_token': token,
            'longurl':url
            }
    r = requests.get('https://api-ssl.bitly.com/v3/shorten',params=query).json()['data']['url']
    return r

def tinyurl(url):
    post = requests.post("http://tinyurl.com/api-create.php?url=%s" % url)
    return post.text

def filesize(byte):
    if byte < 1024:
        return str(byte) + ' Bytes'
    elif byte < 1024 ** 2:
        return str(round((byte / 1024.0), 1)) + ' KB'
    elif byte < 1024 ** 3:
        return str(round((byte / 1024.0), 1)) + ' MB'
    elif byte < 1024 ** 4:
        return str(round((byte / 1024.0), 1)) + ' GB'
    elif byte < 1024 ** 5:
        return str(round((byte / 1024.0), 1)) + ' TB'
    else:
        return str(byte) + ' Bytes'
    
def Notify(to,message):
    token = to
    headers = {'Authorization' : 'Bearer ' + token}
    payload = {'message' : message}
    r = requests.post('https://notify-api.line.me/api/notify', headers=headers, params=payload)
    
def linetime(time):
    r = datetime.fromtimestamp(time / 1000).strftime("%Y/%m/%d %H:%M:%S")
    return r

def talk(key,title, message, path="./",speaker="1",style="1",rate="1",format="2"):
    if not os.path.isfile(path+title+".wav"): # 既に音声ファイルがあるかどうかを確認する
        try:
            url = 'https://api.apigw.smt.docomo.ne.jp/crayon/v1/textToSpeech?APIKEY=%s' % key
            params = {
                  "Command":"AP_Synth",
                  "SpeakerID":speaker,
                  "StyleID":style,
                  "SpeechRate":rate,
                  "AudioFileFormat":format,
                  "TextData":message
                }
            r = requests.post(url, data=json.dumps(params))
            if r.status_code == requests.codes.ok:
                wav = r.content
                with open(path+title+".wav","wb") as f:
                    f.write(wav)
                return path+title+".wav"
        except Exception as e:
            print(e)
            
def rancharacter(quantity=6):
    r = ''.join(random.choices(string.ascii_letters + string.digits, quantity))
    return r

def imgoogle(text):
    r = tinyurl('https://www.google.co.jp/search?hl=ja&tbm=isch&' + urllib.parse.quote(text))
    return r

def google(text):
    r = tinyurl('https://www.google.co.jp/search?' + urllib.parse.quote(text))
    return r

def youtube(text):
    r = tinyurl('https://www.youtube.com/results?search_query=' + urllib.parse.quote(text))
    return r

def yahoo(text):
    r = tinyurl('https://search.yahoo.co.jp/search?p=' + urllib.parse.quote(text))
    return r

def bing(text):
    r = tinyurl('https://www.bing.com/search?q=' + urllib.parse.quote(text))
    return r

def music(name,id="mb00000000016d2e75",artist="",imageurl="https://pixabay.com/images/id-3386570/",url="https://www.google.com/"):
    r = {
        "id": id,
        "name": name,
        "artistName":artist,
        "imageUrl":imageurl,
        "url": url,
        "type": "mt",
        "country": "JP"
    }
    return r

def fortuneslip():
    r = random.choice(["大吉","中吉","小吉","末吉","大凶","凶"])
    return r

def googletrans(word):
    headers = {
        "User-Agent": "GoogleTranslate/5.9.59004 (iPhone; iOS 10.2; ja; iPhone9,1)"
    }
    params = {
        "client": "it",
        "dt": ["t", "rmt", "bd", "rms", "qca", "ss", "md", "ld", "ex"],
        "dj": "1",
        "q": word,
        "tl": "ja"
    }
    r = requests.get(url="https://translate.google.com/translate_a/single", headers=headers, params=params)
    r = r.json()
    return r["sentences"][0]["trans"]
