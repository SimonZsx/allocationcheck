#!/bin/sh


sudo kill $(ps aux | grep 'qemu-system-x86_64' | awk '{print $2}')
