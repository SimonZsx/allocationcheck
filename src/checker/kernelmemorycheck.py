import argparse
import logging
import re

import signal
import sys 
import time

from .. import util.memoryAllocationParser as m_parser

'''

A memory check report format is like this:



'''
def CheckKernelMemoryAlloc(args):
    
    setUpKernel(args)

    runKernel(args)

    report = fetchReport(args)

    data = m_parser.parseMemAllocationReport(report)

    saveData(report)

def setUpKernel(args):



def main()


if __name__ == "__main__":
	main()