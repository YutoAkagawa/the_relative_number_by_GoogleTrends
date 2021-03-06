# -*- coding: utf-8 -*-

"""
GoogleTrendsを使った検索数を吐き出すmainプログラム
"""
__author__ = "Yuto Akagawa"

import os
import os.path
import shutil
import sys
from number_of_search import NumberOfSearch
from csv_processing import CSVProcessing
from time import sleep

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "第一引数：基準となるキーワード，第二引数：入力ファイルパス，第三引数：出力ファイルパス"
        sys.exit()
    cp = CSVProcessing(sys.argv[2], sys.argv[3])
    ns = NumberOfSearch(sys.argv[1])    
    data = cp.read()
    ans_list = []
    for raw in data:
        obj_list, trg_list = ns.get_json(raw[1])
        print raw
        #obj_list = ['2.0', '5.0', '3.0']
        #trg_list = ['20.0', '2.0', '3.0']
        obj = ns.calculate_average(obj_list)
        trg = ns.calculate_average(trg_list)
        ans = ns.calculate_relative_number(obj, trg)
        print ans
        raw.append(ans)
        ans_list.append(raw)
        sleep(600)
    cp.write(ans_list)


