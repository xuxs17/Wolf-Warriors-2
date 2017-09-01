# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:52:28 2017

@author: changjin
"""
#载入模块
from bs4 import BeautifulSoup

#创建类
class movieparser():   
    #获取豆瓣评论的方法
    def get_douban_comments(res):
        #评论列表
        comments_list = []  
        #使用BeautifulSoup解析Html
        soup = BeautifulSoup(res)
        #获取对应评论标签的内容
        comment_nodes = soup.select('.comment > p')
        #将评论内容逐条添加进评论列表
        for node in comment_nodes:           
            comments_list.append(node.get_text().strip().replace("\n", "") + u'\n')
        return comments_list
