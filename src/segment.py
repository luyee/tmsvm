#!/usr/bin/python
#_*_ coding: utf-8 _*_
#author:张知临 zhzhl202@163.com
#Filename: segment.py
import sys
import os
depend_path = os.path.dirname(os.getcwd())+"/dependence"
sys.path.insert(0,depend_path)

import pymmseg as seg
seg.dict_load_defaults()

def term_seg(text,str_splitTag):
    line =  seg.Algorithm(text)
    seg_text =""
    for l in line:
        seg_text+=str(l)+str_splitTag
    return seg_text


def main():
    f = file("../data/test.txt")
    text =f.readline()
    print term_seg(text,"^")
    
main()