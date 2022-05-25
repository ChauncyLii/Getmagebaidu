import os.path
import time
import requests

class Download():
    # 如果本地此文件夹则创建
    def __init__(self):
        self.dir_name = "my_download_file"
        if not os.path.exists(self.dir_name):
            os.mkdir(self.dir_name)

    def download_img(self,pic_name,url):
        pic = requests.get(url)
        with open(self.dir_name+'/'+pic_name,'wb')as f:
            f.write(pic.content)
        time.sleep(1)

if __name__ == 'main':
    d = Download()
    url = 'https://img2.baidu.com/it/u=4178052557,1338892885&fm=253&fmt=auto&app=120&f=JPEG?w=640&h=445'
    d.download_img('hello.jpg',url)