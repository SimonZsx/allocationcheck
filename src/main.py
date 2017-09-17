#!/usr/bin/python2.7

import argparse
import logging

import re
import signal
import sys 
import time





def DoKernelMemoryAllocation(args):



   if args.check == "alloconly":


      alloc_list = open(args.allocfile, "r")

   if args.check == "both":

      alloc_list = open(args.allocfile, "r")
      mem_list = open(args.memfile, "r")


   if args.check == "memonly":

      mem_list = open(args.memfile, "r")


def main(args):

   if args.mode == "kernel":
      DoKernelMemoryAllocation(args)

   if args.mode == "usermode":
      DoUsermodeMemoryAllocation(args)




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Allocation Checker')

    parser.add_argument('')

    Pargs = parser.parse_args()
    # Set up the signal handler
    signal.signal(signal.SIGINT, signal_handler)
    # Set up the logging system
    logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(levelname)s %(message)s',
            filename='parser.log',
            filemode='w')
    logging.debug("Script starts")
    main(args)


    

