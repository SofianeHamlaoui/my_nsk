#!/usr/bin/env python
import requests

mac_info_list = []

class mac_info: 
    def __init__(self,company,address,country):
        self.company = company
        self.address = address
        self.country = country
def mac_lookup(mac_addr):
    class_list = []
    MAC_URL = "http://macvendors.co/api/%s"
    req = requests.get(MAC_URL % mac_addr)
    company = "COMPANY: " + req.json()["result"]["company"]
    address = "ADDRESS: " + req.json()["result"]["address"]
    country = "COUNTRY: " + req.json()["result"]["country"]
    
    print(company)
    print(address)
    print(country)

    #append to global list to get variables nested in function for output flag
    class_list.append(mac_info(company,address,country))
    for attr in class_list:
        mac_info_list.append(attr.company)
        mac_info_list.append(attr.address)
        mac_info_list.append(attr.country)
    
   





    

