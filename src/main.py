#!/usr/bin/python2.7

import argparse
import logging
import re

import signal
import sys 
import time

import checker.kernelmemorycheck as kmc


def DoKernelMemoryAllocation(args):



   if args.check == "alloconly":


      alloc_f = open(args.allocfile, "r")
      
      alloc_list = []

      for line in alloc_f:
          alloc_list.add(line)      
      kmc.CheckKernelMemoryAlloc(args, alloc_list)

   if args.check == "both":

      alloc_list = open(args.allocfile, "r")
      op_list = open(args.opfile, "r")

      kmc.CheckKernelMemoryAllocAndUsage(args, alloc_list, op_list)


   if args.check == "memonly":

      op_list = open(args.opfile, "r")

      kmc.CheckKernelMemoryUsage(args, op_list)


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


    

