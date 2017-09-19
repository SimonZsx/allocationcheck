#!/bin/sh

sudo kvm -kernel ~/linux_kernel/obj/linux-x86-basic/arch/x86/boot/bzImage \
  -drive file=$HOME/linux_kernel/wheezy.img,if=virtio \
  -initrd obj/initramfs-busybox-x86.cpio.gz \
  -nographic \
  -append "root=/dev/vda console=ttyS0"\
  -net nic,model=virtio,macaddr=52:54:00:12:34:56 \
  -net user,hostfwd=tcp:127.0.0.1:10022-:22
