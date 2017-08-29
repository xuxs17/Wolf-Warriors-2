# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:44:16 2017

@author: changjin
"""

import random
import time

from downloader import download as dd
from zhanlangparser import  movieparser as ps
import codecs

if __name__ == '__main__':

    templateurl = 'https://movie.douban.com/subject/26363254/comments?start={}&limit=20&sort=new_score&status=P';
    with codecs.open('zl2_comment.txt', 'a', encoding='utf-8') as f:
        #5000
        for i in range(5000):
            print ('开始爬取{}页评论...', i)
            targeturl = templateurl.format(i * 20)
            res = dd.download_page(targeturl)
            f.writelines(ps.get_douban_comments(res))
            time.sleep(1 + float(random.randint(1, 20)) / 20)