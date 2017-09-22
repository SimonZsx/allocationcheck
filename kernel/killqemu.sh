#!/bin/sh


sudo kill $(ps aux | grep '/home/shixiong/linux_kernel/obj/linux-x86-basic/arch/x86/boot/bzImage' | awk '{print $2}')
