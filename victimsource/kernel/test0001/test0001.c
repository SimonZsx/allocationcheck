#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>


int main(){

    int fd;
    fd = socket(AF_INET,SOCK_STREAM,0);

    exit(0);


}
