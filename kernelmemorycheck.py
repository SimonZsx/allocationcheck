import argparse
import logging
import re

import signal
import sys
import os 
import time

import paramiko

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
    
    ##setUpKernel(args)

    ##runKernel(args)

    ssh = setssh()

    
    report = fetchReport(args)

    data = m_parser.parseMemAllocationReport(report)

    saveData(report)

def setUpKernel(args):


def setkprobe(ssh):
    sin,sout,serr = ssh.exec_command("echo 'p:myprobe do_sys_open dfd=%ax filename=%dx flags=%cx mode=+4($stack)' > /sys/kernel/tracing/kprobe_events
")
    if serr not null:
        print("ERROR: "+serr)
        sys.exit(1)
    else:
        print("Successfully Enalbed Kprobe (SSH)")


def setkretprobe(ssh):
     sin,sout,serr = ssh.exec_command("echo 'r:myretprobe do_sys_open $retval' >> /sys/kernel/tracing/kprobe_events")

    if serr not null:
        print("ERROR: "+serr)
        sys.exit(1)
    else:
        print("Successfully Enalbed Kretprobe (SSH)")
     

def mount(ssh):
    sin,sout,serr = ssh.exec_command("mount -t tracefs nodev /sys/kernel/tracing")

    print("Successfully Mount (SSH)")

def connectssh():

    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect("localhost",port="10022",username="root",password="")
        return ssh
    except paramiko.AuthenticationException:
        print("SSH Authentication Failed")
        sys.exit(1)
    except:
        print("SSH Connection Timeout")
        sys.exit(1)

def closessh(ssh):
    ssh.close()
   
def runKernel(args):

def fetchReport(args):


def main()


if __name__ == "__main__":
	main()
