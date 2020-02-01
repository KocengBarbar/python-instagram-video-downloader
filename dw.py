#instagram video downloader
#by : thoriqalmahdi

from requests import *
import re, os
import urllib.request

#fungsi untuk mengunduh video beserta nama.mp4
def dw(urlv,nama):
    urllib.request.urlretrieve(urlv,nama)


#input url dan nama video
url = input("Input Link : ")
nama = input("Nama File : ")
nama = nama + str(".mp4")

#mencari source video dengan regular expression
r = get(url)
urlv = re.search(r'\"(http[s]\:\/\/*\/.*mp.+\w)\"',r.text)



if urlv :
    urlv = urlv.group(1)
    print("Sedang mendownload...")
    dw(urlv,nama)
    print("download berhasil")
else :
    print("Video tidak ditemukan")