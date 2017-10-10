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




Set kprobe:

  echo 'p:myprobe __kmalloc filename=%cx input1=%di  input2=%si input3=%dx' > /sys/kernel/tracing/kprobe_events
  
  

Set kretprobe:
  echo 'r:myretprobe __kmalloc $retval' >> /sys/kernel/tracing/kprobe_events

See Format
  cat /sys/kernel/tracing/events/kprobes/myprobe/format

Clear Trace:
  echo > /sys/kernel/tracing/kprobe_events

Enable Trace:
  echo 1 > /sys/kernel/tracing/events/kprobes/myprobe/enable
  echo 1 > /sys/kernel/tracing/events/kprobes/myretprobe/enable

Disable Trace:
  echo 0 > /sys/kernel/tracing/events/kprobes/myprobe/enable
  echo 0 > /sys/kernel/tracing/events/kprobes/myretprobe/enable  


SCP:

scp -P 10022 root@localhost:/root .

'''
def CheckKernelMemoryAlloc(args):
    
    ##setUpKernel(args)

    ##runKernel(args)

    ssh = setssh()

    mount(ssh)


    setMemFuncList(ssh, mem_func_list)

    setOpFuncList(ssh, op_func_list)

    for file_path in test_list:
        runExec(ssh, file_path)
    
    report = fetchReport(args)

    data = m_parser.parseMemAllocationReport(report)

    saveData(report)

def setUpKernel(args):




def runExec(ssh, path):



def fetchReports(ssh):

    remote_path = "/sys/kernel/tracing/trace"
    local_path = "./tmpreport"
    sftp = ssh.open_sftp()
    sftp.get(remote_path, local_path)
    sftp.close()


def setKprobe(ssh, func, name):

    cmd = "echo \'p:"+name+" "+func+" filename=%%cx input1=%%di  input2=%%si input3=%%dx' > /sys/kernel/tracing/kprobe_events"
    sin,sout,serr = ssh.exec_command(cmd)
    if serr not null:
        print("ERROR: "+serr)
        sys.exit(1)
    else:
        print("Successfully Enalbed Kprobe (SSH)")


def setKretprobe(ssh, func, name):

    cmd = "echo \'r:"+name+" "+func+" retval=$retval\' >> /sys/kernel/tracing/kprobe_events"
    sin,sout,serr = ssh.exec_command(cmd)
    if serr.read() not null:
        print("ERROR: "+serr)
        sys.exit(1)
    else:
        print("Successfully Enalbed Kretprobe (SSH)")


def clearProbes(ssh):
    cmd = "echo > /sys/kernel/tracing/kprobe_events"
    sin,sout,serr = ssh.exec_command(cmd)
    print("Successfully Cleaned Probes")

def setMemFuncList(ssh, func_list):

    for func in func_list:
        setKprobe(ssh, func, func)
        setKretprobe(ssh, func, func)
def setOpFuncList(ssh, func_list):  
    for func in func_list:
        setKprobe(ssh, func, func)

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
    else:
        print("SSH Connected")


def closessh(ssh):
    ssh.close()
     
def runKernel(args):


def main():


if __name__ == "__main__":
    main()
