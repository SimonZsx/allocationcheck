#!/bin/sh

sudo kvm -kernel ~/linux_kernel/obj/linux-x86-basic/arch/x86/boot/bzImage \
  -drive file=$HOME/linux_kernel/wheezy.img,if=virtio \
  -chardev stdio,id=virtiocon0,mux=on,signal=off \
  -device virtio-serial-pci \
  -device virtconsole,chardev=virtiocon0 \
  -mon chardev=virtiocon0 \
  -display none\
  -append "root=/dev/vda console=hvc0"\
  -net nic,model=virtio,macaddr=52:54:00:12:34:78 \
  -net user,hostfwd=tcp:127.0.0.1:10022-:22
