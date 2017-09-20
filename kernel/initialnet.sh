#!/bin/sh

sudo kvm -kernel $AC_KERNEL_PATH \
  -drive file=$AC_USERSPACE_PATH,if=virtio \
  -chardev stdio,id=virtiocon0,mux=on,signal=off \
  -device virtio-serial-pci \
  -device virtconsole,chardev=virtiocon0 \
  -mon chardev=virtiocon0 \
  -display none\
  -append "root=/dev/vda console=hvc0"\
