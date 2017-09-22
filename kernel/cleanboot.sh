#!/bin/sh


sudo kvm -kernel $AC_KERNEL_PATH \
  -drive file=$AC_USERSPACE_PATH,if=virtio \
  -nographic\
  -append "root=/dev/vda"\
  -net nic,model=virtio,macaddr=$AC_MAC_ADDR \
  -net user,hostfwd="tcp:127.0.0.1:$AC_SSH_PORT-:22"\
