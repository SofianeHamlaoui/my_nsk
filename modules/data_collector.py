#!/usr/bin/env python
import os

#fiile = open(__file__, "w+")
def data_collector(file):
    collector = open("data_collector.txt","a+")
    file_list = []
    open_file = open(str(file), "w+")
    for x in open_file.readlines():
        values = x.split()
        print()
        
        file_list.append(x)
        print("ZZZ: " + str(file_list))
        open_file.close()
    
    for text in file_list:
        collector.write(text)
    read_file = collector.read()
    print("TEST:" + read_file)
    collector.close()


   
        

