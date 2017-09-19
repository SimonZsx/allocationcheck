import argparse
import logging
import re

import signal
import sys 
import time

from .. import util.memoryAllocationParser as m_parser

'''

A memory check report format is like this:


<...>-1447  [001] 1038282.286875: myprobe: (malloc64+0x0/0xd6) dfd=3 filename=7fffd1ec4440 input1=... input2=... input3=...
<...>-1447  [001] 1038282.286878: myretprobe: (malloc+0xc/0xe <- malloc64) $retval=fffffffffffffffe

A usage check report format is like this

<...>-1447  [001] 1038282.286875: myprobe: (strcpy64+0x0/0xd6) dfd=3 filename=7fffd1ec4440 input1=... input2=... input3=...


parsed allocation data:

func     file       size  time            mem
malloc64 test0001.c 48    1038282.286875  fffffffffffffffe

'''
def CheckKernelMemoryAlloc(args):
    
    setUpKernel(args)

    runKernel(args)

    report = fetchReport(args)

    data = m_parser.parseMemAllocationReport(report)

    saveData(report)

def setUpKernel(args):

def runKernel(args):

def fetchReport(args):


def main()


if __name__ == "__main__":
	main()