import datetime
import os

now = datetime.datetime.now()
nowtime = now.strftime("%Y-%m-%d")
url = 'Pixiv日榜/' + nowtime
os.system('echo \'cd '+url+' && zip -r ../' +nowtime+'.zip * && cd ../\' > other.sh')
os.system('echo \'rm -r ' + nowtime+'\' >> other.sh')
os.system('echo \'cd ../ && python upload_ali.py\' >> other.sh')
os.system('rm -r Pixiv日榜')
os.system('sh other.sh')
os.system('rm -r other.sh')
