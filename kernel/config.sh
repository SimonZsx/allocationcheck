#!/bin/sh

echo "Starting config KERNEL env..."

export AC_KERNEL_PATH="$HOME/linux_kernel/obj/linux-x86-basic/arch/x86/boot/bzImage"
export AC_USERSPACE_PATH="$HOME/linux_kernel/wheezy.img"
export AC_MAC_ADDR="52:54:00:12:34:78"
export AC_SSH_PORT="10022"




echo "Config KERNEL finished."



