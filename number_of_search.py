# -*- coding: utf-8 -*-

"""
検索数比較用スクリプト
"""
__author__ = "Yuto Akagawa"

import os
import os.path
import csv
import shutil
import numpy as np
import sys
from time import sleep
from urllib import urlopen

class NumberOfSearch:
    def __init__(self, object_word):
        self.object_word = object_word

    def get_json(self, target_word):
        print self.object_word
        print target_word
        url = 'http://www.google.com/trends/fetchComponent?q=' + self.object_word + ',' + target_word + '&cid=TIMESERIES_GRAPH_0&export=3'
        print url
        sleep(60)
        src = urlopen(url).read()
        data = src.split("\"")
        object_num = []
        target_num = []
        object_flag = False
        target_flag = False
        year_flag = False
        for raw in data:
            if "2015" in raw or "2016" in raw or "2017" in raw:
                object_flag = False
                target_flag = False
                year_flag = True
            elif ":" in raw and "." in raw and year_flag == True:
                raw = raw.replace(":", "")
                raw = raw.replace(",", "")
                if not object_flag:
                    object_num.append(raw)
                    object_flag = True
                elif object_flag and not target_flag:
                    target_num.append(raw)
                    target_flag = True
                else:
                    print "error"
                    print raw
                    sys.exit()
        return object_num, target_num
    
    def calculate_average(self, data):
        count = 0.0
        num = 0.0
        for data in data:
            count += 1.0
            num += float(data)
        return int (num / count)

    def calculate_relative_number(self, obj, trg):
        if obj == 0:
            return -1
        else:
            return 45 / obj * trg 

