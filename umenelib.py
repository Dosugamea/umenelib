from urllib.parse import quote
from datetime import datetime
import requests
import random
import string
import json

class UmeneLib(object):
    def drawFortune(self):
        '''おみくじをひく'''
        r = random.choice(["大吉","中吉","小吉","末吉","大凶","凶"])
        return r
    
    def convertFilesize(self,byte):
        '''ファイルサイズの単位を変換して文字列にする'''
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
        
    def generateRandCharacter(self,quantity=6):
        '''指定した字数のランダムな文字列を作る'''
        r = ''.join(random.choices(string.ascii_letters + string.digits, k=quantity))
        return r
    
    def convertCiplex(self,word):
        '''簡易暗号化/複合化'''
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

    def convertLineTime(self,time):
        '''Line Time を 日付文字列にする'''
        r = datetime.fromtimestamp(time / 1000).strftime("%Y/%m/%d %H:%M:%S")
        return r
    
    def generateMusicMeta(self,name,id="mb00000000016d2e75",artist="",imageurl="https://pixabay.com/images/id-3386570/",url="https://www.google.com/"):
        '''音楽型のMetadataを作る'''
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

    def shortenWithBitly(self,token,url):
        '''URL短縮(要トークン)'''
        token = token
        query = {
                'access_token': token,
                'longurl':url
                }
        r = requests.get('https://api-ssl.bitly.com/v3/shorten',params=query).json()['data']['url']
        return r

    def shortenWithTinyurl(self,url):
        '''URL短縮(トークン不要)'''
        r = requests.post("http://tinyurl.com/api-create.php?url=%s" % url)
        return r.text
    
    def generateLinkWithImgGoogle(self,text):
        '''Google画像検索リンクを作る'''
        r = self.shortenWithTinyurl('https://www.google.co.jp/search?hl=ja&tbm=isch&' + quote(text))
        return r

    def generateLinkWithGoogle(self,text):
        '''Google検索リンクを作る'''
        r = self.shortenWithTinyurl('https://www.google.co.jp/search?' + quote(text))
        return r

    def generateLinkWithYoutube(self,text):
        '''Youtube検索リンクを作る'''
        r = self.shortenWithTinyurl('https://www.youtube.com/results?search_query=' + quote(text))
        return r

    def generateLinkWithYahoo(self,text):
        '''Yahoo検索リンクを作る'''
        r = self.shortenWithTinyurl('https://search.yahoo.co.jp/search?p=' + quote(text))
        return r

    def generateLinkWithBing(self,text):
        '''Bing検索リンクを作る'''
        r = self.shortenWithTinyurl('https://www.bing.com/search?q=' + quote(text))
        return r

    def textToSpeech(self,apiKey,title, message, path="./",speaker="1",style="1",rate="1",format="2"):
        '''Docomo Text To Speech API で 読み上げを行う'''
        if not os.path.isfile(path+title+".wav"):
            try:
                url = 'https://api.apigw.smt.docomo.ne.jp/crayon/v1/textToSpeech?APIKEY=%s' % apiKey
                params = {
                      "Command":"AP_Synth",
                      "SpeakerID":speaker,
                      "StyleID":style,
                      "SpeechRate":rate,
                      "AudioFileFormat":format,
                      "TextData":message
                    }
                r = requests.post(url, data=json.dumps(params))
                if r.status_code == 200:
                    with open(path+title+".wav","wb") as f:
                        f.write(r.content)
                    return path+title+".wav"
            except Exception as e:
                print(e)
                
    def sendLineNotify(self,token,message):
        '''Line Notifyで通知する'''
        headers = {'Authorization' : 'Bearer ' + token}
        payload = {'message' : message}
        r = requests.post('https://notify-api.line.me/api/notify', headers=headers, params=payload)

    def translateWithGoogle(self,word):
        '''Google翻訳APIで翻訳する'''
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
    
    def ojichatify(self,name,emojiLevel=3,punctiuationLevel=1):
        '''文字列をおじさん風に'''
        payload = {'name': name, 'emoji_level': emojiLevel, "punctiuation_level": punctiuationLevel}
        r = requests.post("https://ojichat.appspot.com/post", data=payload)
        data = r.json()
        return data['message']

if __name__ == "__main__":
    lib = UmeneLib()
    print(lib.drawFortune())
    print(lib.convertFilesize(12041204))
    print(lib.generateRandCharacter(20))
    print(lib.convertCiplex("UmeneLib"))
    print(lib.convertCiplex(lib.convertCiplex("UmeneLib")))
    print(lib.convertLineTime(11100000))
    print(lib.generateMusicMeta("UmeneLib"))
    print(lib.shortenWithTinyurl("http://gochiusa.com"))
    print(lib.generateLinkWithImgGoogle("Kafuu chino"))
    print(lib.generateLinkWithGoogle("Kafuu chino"))
    print(lib.generateLinkWithYoutube("Kafuu chino"))
    print(lib.generateLinkWithYahoo("Kafuu chino"))
    print(lib.generateLinkWithBing("Kafuu chino"))
    print(lib.translateWithGoogle("Kafuu chino"))
    print(lib.ojichatify("香風智乃"))
