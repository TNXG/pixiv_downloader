import datetime
import os

now = datetime.datetime.now()
nowtime = now.strftime("%Y-%m-%d")
url = 'Pixiv日榜/' + nowtime
os.system('cd '+ url)
os.system('zip -q -r ../' + nowtime + '.zip /* && cd ../')
os.system('rm -r '+ nowtime)
os.system('cd ../ && python upload_ali.py')