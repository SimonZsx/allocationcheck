This is a submodule of project owl.

The purpose of the module is to :

1. Get the memory allocation info of Linux Kernel
2. Get the memory operation dst of Linux Kernel
3. Match 1. and 2. to get property(where-which slab/stack and how-kalloc32/malloc) of the memory operation destination address 


Build

Usage

Kernel:


1. Specify kernel source directory.

  $ KERNEL_SOURCE_DIR = ./home/user/linux-4.0.1/

2. Specify race trigger C source

   $exploit.c


3. Specify race report + dangeroud memory function report


   write [<ffffffff8147cf97>] ipc_addid+0x217/0x260 ipc/util.c:257 

   read [<ffffffff8147d84d>] ipc_obtain_object_check+0x7d/0xd0 ipc/util.c:621 

   strcpy [<ffffffff8147d84d>] ipc_obtain_object_check+0x7d/0xd0 ipc/util.c:625 

4. Specify Crowdsource Benchmarks
