import java.io.*;
import java.util.Scanner;

class fifth{


	public static void main(String args[]){
		Scanner s= new Scanner(System.in);

		System.out.println("Enter the array size");
		int n = s.nextInt();

		int A[] = new int[n];

		System.out.println("Enter the array elements");
		for(int i =0;i<n;i++)
			A[i]=s.nextInt();
		// reversing the array

		System.out.println("Reversed Array: ");

			for(int i = 0;i<n;i++)
				System.out.println(A[n - 1 - i]);

	}
}