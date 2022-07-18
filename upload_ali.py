from aligo import Aligo
import sys
import datetime
import os

now = datetime.datetime.now()
nowtime = now.strftime("%Y-%m-%d")

if __name__ == '__main__':
    ali = Aligo(refresh_token='cfda1a0578064e8e914b73618c21f7f8')
    ali.upload_file('./Pixiv日榜/' + nowtime + '.zip','62d5aa4a830983213e4b4ddcb8e18568ce067140')
