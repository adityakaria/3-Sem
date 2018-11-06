#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(void)
{
	
	pid_t pid1, pid2, pid3;
	/* process id */
	// printf("just one process before the fork()\n");
	pid1 = fork();
	// pid2 = fork();
	// pid3 = fork();
	
	if(pid1 == 0)
	{	
		sleep(2);
		printf("Process1 ID  %d\n", getpid());
	}
	else
	{
		pid2 = fork();

		if(pid2 == 0)
		{	
			sleep(3);
			printf("Process2 ID  %d\n", getpid());
		}
		else
		{
			
			pid3 = fork();
			
			if(pid3 == 0)
			{	
				sleep(4);
				printf("Process3 ID  %d\n", getpid());
			}
			else
			{	
				sleep(1);
				printf("\nParent Process: \n");
				printf("PPID: %d\n", getpid());
				printf("\nChild Processes: \n");
			}
		}
	}

	// else if(pid > 0)
	// 	printf("I am the parent process\n");
	// else
	// 	printf("The fork() has failed\n");
	// printf("Process 1: %d\nProcess 2: %d\n", pid1, pid2);
	// printf("Process1: %d\n", pid1);
	sleep(5);
	return 0;
}