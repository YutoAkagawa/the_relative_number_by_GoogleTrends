# -*- coding: utf-8 -*-

"""
csv読み込み，書き込み
"""
__author__ = "Yuto Akagawa"

import csv

class CSVProcessing:
    def __init__(self, ipath, opath):
        self.ipath = ipath
        self.opath = opath

    def read(self):
        f = open(self.ipath, 'r')
        reader = csv.reader(f)
        data = []
        for row in reader:
            data.append(row)
        f.close()
        return data

    def write(self, data):
        f = open(self.opath, 'w')
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(data)
        f.close()



