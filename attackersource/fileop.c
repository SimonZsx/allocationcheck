#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sched.h>
#include <string.h>
#include <sys/socket.h>

void *callrename( void *ptr );
void *openclose( void *ptr );
void *_socket( void *ptr);

char *ctrl = (char *)malloc(16*sizeof(char)); 


main()
{

     pthread_t thread1, thread2, thread3;
     int  iret1, iret2, iret3;
     //setvbuf(stdout,0,2,0);
     //iret1 = pthread_create( &thread1, &attr1, callrename, NULL);
    /* iret1 = pthread_create( &thread1, NULL, callrename, NULL);
     if(iret1)
     {
         fprintf(stderr,"Error - pthread_create() return code: %d\n",iret1);
         exit(EXIT_FAILURE);
     }
*/
     //iret2 = pthread_create( &thread2, &attr2, openclose, NULL);
     iret2 = pthread_create( &thread2, NULL, openclose, NULL);
     if(iret2)
     {
         fprintf(stderr,"Error - pthread_create() return code: %d\n",iret2);
         exit(EXIT_FAILURE);
     }

/*     iret3 = pthread_create( &thread3, NULL, _socket, NULL);
     if(iret3)
     {
         fprintf(stderr,"Error - pthread_create() return code: %d\n",iret3);
         exit(EXIT_FAILURE);
     }
*/

     exit(EXIT_SUCCESS);
}


void *_socket (void *ptr){

     socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
}


void *openclose( void *ptr )
{
    int j;
    for (j=0;j<1;j++)
    {
    int fd=open("test_dir/fortest",O_RDWR);

    if (fd!=-1)
    {
    close(fd);
    }
    }
}