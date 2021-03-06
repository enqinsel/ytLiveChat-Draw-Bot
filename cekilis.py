from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random 
import sys
import re 

ytLiveChatURL = input('''
* Sadece Chrome tarayıcısında çalışır.

Lütfen cekilisi yapacaginiz sohbet URL'yi giriniz: ''')

keyword = input("Lütfen cekilis kelimesini giriniz: ")
eligibleUsers = set()

if re.search("www.youtube.com",ytLiveChatURL):
    UrlYt=ytLiveChatURL
else:
    exit("Hatalı Link! Bu formatta giriniz: ('www.youtube.com')")


# start web browser
browser=webdriver.Chrome()

#Sayfanın HTML kodunu alan fonksiyon
def getHTML(url):

    # get source code
    browser.get(UrlYt)
    time.sleep(1)
    page_source = browser.page_source
    return page_source

#Sayfanın kodunu, parse edip soup objesine dönüştüren fonksiyon
def parseHTML(html_source):
    return BeautifulSoup(html_source, 'html.parser')

#Soup'dan mesajları alan fonksiyon
def getMessages(soup):
    return soup.find_all("yt-live-chat-text-message-renderer")

#Mesajları başka bir fonksiyona döndürerek, mesajlar üzerinden hak kazananların listesini alan fonksiyon
def updateEligibleUsers(messages):
    

    for message in messages:
        content = message.find("div", {"id": "content"})
        author = content.find("span", {"id": "author-name"}).text
        message_content = content.find("span", {"id": "message"}).text
        print("Adı: " , author , "\t", "Yorumu: " , message_content)
        if keyword in message_content.lower():
            print("eklendi")
            eligibleUsers.add(author)
        #else:
        #   print("eklenmedi") Sağlama...

#Seti listeye çevirip, çekilişi başlatan fonksiyon
def startDrawing(eligibleUsersList):
    if len(eligibleUsersList) == 0:
        print("Kayıt oluşturulmadı")
        sys.exit()
    print("Çekiliş Başlıyor...")

    time.sleep(3)
    for i in range(1,5):
        noktalar = i * "."
        print("Rastgele bir sayı çekiliyor" + noktalar)
        time.sleep(1)

    print("Hazır Mısınız?")
    time.sleep(1.5)
    print("Kontroller yapılıyor..")
    time.sleep(1.5)
    print("Bugün Nasılsın ?")
    time.sleep(1.5)
    print("Son kontrolleri yapıyorum..")
    time.sleep(1.5)
    print("Veee..")
    print(f"{len(eligibleUsersList)} kisi arasindan kazanan:{random.choice(eligibleUsersList)}") # try-expect yap!!

def main():
    for i in range(0,7):
        html_source = getHTML(UrlYt)
        soup = parseHTML(html_source)
        messages = getMessages(soup)
        updateEligibleUsers(messages)
        print("{count} kisi cekilise katilmis durumda".format(count=len(eligibleUsers)))
        time.sleep(10)
    
    eligibleUsersList = list(eligibleUsers)
    startDrawing(eligibleUsersList)
    browser.close()
main()