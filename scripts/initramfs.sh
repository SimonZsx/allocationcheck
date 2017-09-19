#!/bin/sh


cd ~/linux_kernel/initramfs/x86-busybox/ && find . -print0 \
    | cpio --null -ov --format=newc \
    | gzip -9 > ~/linux_kernel/obj/initramfs-busybox-x86.cpio.gz 
