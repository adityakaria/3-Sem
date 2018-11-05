import java.io.*;
import java.util.Scanner;


class ninth{


	public static void main(String args[]){

		Scanner s = new Scanner(System.in);
		System.out.println("Enter any String");
		String str = s.nextLine();

		String str2="";

		for( int i = 0 ; i < str.length();i++)
			str2+=str.charAt(i);


		System.out.println("Copied string: " + str2);

	}
}