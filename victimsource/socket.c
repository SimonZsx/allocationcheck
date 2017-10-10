#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sched.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/tcp.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <string.h>
#include <signal.h>
#include <sys/eventfd.h>
#include <sys/mman.h>
#define SOCKNUM 3
#define FDNUM 150


void *callrename( void *ptr );
void *openclose( void *ptr );
void *_socket( void *ptr);

//char *ctrl = (char *)malloc(16*sizeof(char)); 


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
/*     iret2 = pthread_create( &thread2, NULL, openclose, NULL);
     if(iret2)
     {
         fprintf(stderr,"Error - pthread_create() return code: %d\n",iret2);
         exit(EXIT_FAILURE);
     }*/

     iret3 = pthread_create( &thread3, NULL, openclose, NULL);
     if(iret3)
     {
         fprintf(stderr,"Error - pthread_create() return code: %d\n",iret3);
         exit(EXIT_FAILURE);
     }


     exit(EXIT_SUCCESS);
}


void *_socket (void *ptr){

//     socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
}


void *openclose( void *ptr )
{
    int j,fd,m,portno,sockfd[SOCKNUM];
    struct sockaddr_in serv_addr;
    for (j=0;j<10;j++)
    {
    //fd=open("test_dir/f",O_RDWR);
for (m=0;m<SOCKNUM;m++){
    if(sockfd[m]!=0)

    close(sockfd[m]);}
   // if (fd!=-1)
    //{
     //   close(fd);
        for (m=0;m<SOCKNUM;m++)
        {
        sockfd[m]=socket(AF_INET,SOCK_STREAM,0);
        }
        //sleep(0.1);
        for (m=0;m<SOCKNUM;m++)
        {
        bzero((char *) &serv_addr, sizeof(serv_addr));
       serv_addr.sin_family = AF_INET;
       serv_addr.sin_addr.s_addr = INADDR_ANY;
       serv_addr.sin_port = htons(5000+m);
       bind(sockfd[m], (struct sockaddr *) &serv_addr, sizeof(serv_addr));
        }
  //  }
    }
}
