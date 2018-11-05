import java.io.*;
import java.util.Scanner;

class fourth{

	public static Scanner s = new Scanner(System.in);

	public static void main(String args[]){

		System.out.println("Enter choice: \n 1. Add arrays \n 2. Subtract arrays \n 3. Transpose of the array \n 4. Multiply arrays");
		int choice = s.nextInt();

		switch(choice){

			case(1):add();
			break;
			case(2):subtract();
			break;
			case(3):transpose();
			break;
			case(4):multiply();
			break;
			default:
			System.out.println("Invalid input");


		}		
		

	}





	static void add(){
		System.out.println("Enter the number of rows in the array");
		int r = s.nextInt();
		System.out.println("Enter the number of columns in the array");
		int c =s.nextInt();

		int A[][]=new int[r][c];
		int B[][]=new int[r][c];
		int C[][]=new int[r][c];

		System.out.println("Enter elements of A");


		for(int i = 0 ;i< r;i++)
			for(int j =0 ;j<c;j++)
				A[i][j]=s.nextInt();

			System.out.println("Enter elememts of B");

		for(int i = 0 ;i< r;i++)
			for(int j =0 ;j<c;j++)
				{B[i][j]=s.nextInt();
			     C[i][j]=A[i][j]+B[i][j];}

			     System.out.println("The elements of the new array are:");

		for(int i = 0 ;i< r;i++)
			{for(int j =0 ;j<c;j++)
				System.out.print(C[i][j]+"\t");
			System.out.println();}

		

	}



	static void subtract(){
		System.out.println("Enter number of rows of the array");
		int r = s.nextInt();
		System.out.println("Enter number of columns of the array");
		int c =s.nextInt();

		int A[][]=new int[r][c];
		int B[][]=new int[r][c];
		int C[][]=new int[r][c];

		System.out.println("Enter the elements of A");


		for(int i = 0 ;i< r;i++)
			for(int j =0 ;j<c;j++)
				A[i][j]=s.nextInt();

			System.out.println("Enter the elememts of B");

		for(int i = 0 ;i< r;i++)
			for(int j =0 ;j<c;j++)
				{B[i][j]=s.nextInt();
			     C[i][j]=A[i][j]-B[i][j];}

			     System.out.println("The elements of the new array are:");

		for(int i = 0 ;i< r;i++)
			{for(int j =0 ;j<c;j++)
				System.out.print(C[i][j]+"\t");
			System.out.println();}

		

	}



	public static void multiply(){

		System.out.println("Enter the rows of Matrix1");

		int m = s.nextInt();
		System.out.println("Enter the columns of Matrix1");
		int n = s.nextInt();
		System.out.println("Enter the rows of Matrix2");
		int o =s.nextInt();
		System.out.println("Enter the columns of Matrix2");
		int p =s.nextInt();

		int A[][]=new int[m][n];
		int B[][]=new int[o][p];
		int C[][]=new int[m][p];

		if(n != o )
			return;


		System.out.println("Enter elements of A");


		for(int i = 0 ;i< m;i++)
			for(int j =0 ;j<n;j++)
				A[i][j]=s.nextInt();

			System.out.println("Enter elememts of B");

		for(int i = 0 ;i<o;i++)
			for(int j =0 ;j<p;j++)
				B[i][j]=s.nextInt();
			     



		for(int i = 0 ;i< m;i++)
			{for(int j =0 ;j<p;j++)
				{for(int k =0 ;k<n;k++)
					C[i][j]+=A[i][k]*B[k][j];

					System.out.print(C[i][j]+"\t");
				}
				System.out.println();
			}




	}




	public static void transpose(){

		System.out.println("Enter the rows of the array");
		int r = s.nextInt();
		System.out.println("Enter the columns of the array");
		int c =s.nextInt();

		int A[][]=new int[r][c];
		int B[][]=new int[c][r];

		System.out.println("Enter the elements of A");


		for(int i = 0 ;i< r;i++)
			for(int j =0 ;j<c;j++)
				A[i][j]=s.nextInt();






		for(int i =0 ;i< r ;i++)
			for(int j =0 ;j<c ; j++)
				B[j][i]=A[i][j];

		for(int i = 0 ;i< c;i++)
			{for(int j =0 ;j<r;j++)
				System.out.print(B[i][j]+"\t");
			System.out.println();}



	}









}