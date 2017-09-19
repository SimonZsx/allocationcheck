#!/bin/sh

cd ~/linux_kernel && \
sudo kvm \
    -kernel obj/linux-x86-basic/arch/x86_64/boot/bzImage \
    ##-initrd obj/initramfs-busybox-x86.cpio.gz \
    ##-enable-kvm\
    -drive file=$HOME/linux_kernel/wheezy.img,if=virtio \
    -append "root=/dev/vda"\
    -net nic,model=virtio,macaddr=52:54:00:12:34:56 \
    -net user,hostfwd=tcp:127.0.0.1:4444-:22


