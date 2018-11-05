import java.io.*;
import java.util.Scanner;

public class third
{

	public static void main(String args[])
	{
		Scanner in = new Scanner(System.in);
		System.out.println("Enter array size: ");
		int n = in.nextInt();
		int A[] = new int[n];

		for(int i = 0; i < n; i++)
		{
			System.out.println("Enter element" + i);
			A[i]=in.nextInt();
			A[i]=A[i]%2;
		}

		for(int i = 0 ;i<n;i++)
		{
			System.out.print(A[i] + " ");

		}
	}

}
