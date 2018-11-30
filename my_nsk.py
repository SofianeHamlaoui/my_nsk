#!/usr/bin/env python
import argparse
import os.path
import modules.mac_lookup as mac


def macLookup(args):
    #mac lookup functionality
    mac.mac_lookup(args.mac_address[0])
    
    #output flag functionality
    if os.path.isfile(str(args.output[0])):
        collector = open(str(args.output[0]), "a")
        collector.write(mac.mac_info_list[0] + "\n{}".format(mac.mac_info_list[1]) + "\n{}".format(mac.mac_info_list[2]))
        collector.write("\n============================================\n")
        collector.close()
    elif args.output[0] != "none":
        collector = open(str(args.output[0]), "w+")
        collector.write(mac.mac_info_list[0] + "\n{}".format(mac.mac_info_list[1]) + "\n{}".format(mac.mac_info_list[2]))
        collector.write("\n============================================\n")            
        collector.close()
    
    
       
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Network Redteam kit",
                                    description="Command Line Redteam Toolkit")
    
    subparsers = parser.add_subparsers(help = "Module specific utilities")
    
    #Maclookup Argument
    parser_macLookup = subparsers.add_parser("maclookup", help="info based on mac address")
    parser_macLookup.add_argument("mac_address", nargs=1, help="Target MAC address")
    parser_macLookup.add_argument("--output", "-o", nargs=1, default="none", help="File name to write results to")
    parser_macLookup.set_defaults(func=macLookup)

    
    args = parser.parse_args()
    args.func(args)
  
    