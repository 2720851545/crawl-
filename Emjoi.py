import logging
import os
import re

import requests
from pyquery import PyQuery

class Emjoi:

    indexUrl = 'https://www.fabiaoqing.com/biaoqing/lists/page/%s.html'
    baseDirectory = r'D:\images'
    rstr = r"[\/\\\:\*\?\"\<\>\| ]"

    def __init__(self):
        if not os.path.exists(self.baseDirectory):
            os.makedirs(self.baseDirectory)

    def start(self):
        logging.basicConfig(level=logging.DEBUG)

        for i in range(1, 200):
            # htmlStr = requests.get(self.indexUrl % i).text
            pq=PyQuery(url="https://www.fabiaoqing.com/biaoqing/lists/page/%s.html" % i)
            images = pq("#container div.tagbqppdiv > a > img").items()
            for img in images:
                try:
                    imgUrl = img.attr('data-original')
                    imgSuffix = (imgUrl[imgUrl.rfind('.'):],'')[imgUrl.rfind('.')==-1]
                    fileName = re.sub(self.rstr, "_", img.attr('title')) + imgSuffix
                    file = self.baseDirectory + os.sep + fileName
                    if os.path.exists(file):
                        continue
                    open(file, 'wb').write(requests.get(img.attr('data-original')).content)
                except BaseException as e:
                    print(e)


if __name__ == "__main__":
    Emjoi().start()
