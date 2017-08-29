# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:40:45 2017

@author: changjin
"""
# -*- coding:utf-8 -*-
import requests


class download():   
# 下载源代码
    def download_page(url):        
        header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0','Cookie':'ue'}
        html = requests.get(url,headers=header).content
        return html
