# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 21:28:56 2017

@author: xu
"""
#加载模块
import codecs
from os import path
import jieba
from scipy.misc import imread
from wordcloud import WordCloud
import pandas as pd

#使用jieba分词
def save_jieba_result():
    # 设置多线程切割
    jieba.enable_parallel(4)
    #读取评论文本
    dirs = path.join(path.dirname(__file__), './zl2_comment.txt')
    with codecs.open(dirs, encoding='utf-8') as f:
        comment_text = f.read()
    #将jieba分词得到的关键词用空格连接成为字符串
    cut_text = " ".join(jieba.cut(comment_text))  
    with codecs.open('zl2_jieba.txt', 'a', encoding='utf-8') as f:
        f.write(cut_text)
        
#绘制词云
def draw_wordcloud2():
    #打开jieba分词后文本并读取
    dirs = path.join(path.dirname(__file__), 'zl2_jieba.txt')
    with codecs.open(dirs, encoding='utf-8') as f:
        comment_text = f.read()
    #读取背景图片
    color_mask = imread("background.jpg")  
    #设置停用词
    stopwords = [u'就是', u'电影', u'你们', u'这么', u'不过', u'但是', u'什么', u'没有', u'这个', u'那个', u'大家', u'比较', u'看到', u'真是',
                 u'除了', u'时候', u'已经', u'可以']
    #设置词云的参数
    cloud = WordCloud(font_path="msyh.ttc", background_color='white',max_words=2000, max_font_size=200, min_font_size=4, mask=color_mask, stopwords=stopwords)
    #产生词云
    word_cloud = cloud.generate(comment_text)  
    #保存成zl2_cloud.jpg
    word_cloud.to_file("zl2_cloud.jpg")
    
#调用jieba分词   
save_jieba_result()
#调用绘制词云
draw_wordcloud2()
