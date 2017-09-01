# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:40:45 2017

@author: changjin
"""
# -*- coding:utf-8 -*-
#加载
import requests

#下载源代码
class download():   
    #生成请求头
    def download_page(url):        
        header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0','Cookie':'your cookie'}
        #cookie从帐号登陆豆瓣后的浏览器中获得
        html = requests.get(url,headers=header).content
        return html
