import java.io.*;
import java.util.Scanner;

class eight{


	public static void main(String args[]){

		Scanner s = new Scanner(System.in);
		
		System.out.println("Enter a String");
		String str = s.nextLine();
		
		int count = 0;
		int word_count = 1;
		
		for(int i=0;i<str.length();i++)
		{	
			if(str.charAt(i)==' ')
			{
				System.out.println(word_count+" is "+count+" long");
				count = 0;
				word_count++;
			}

			else
			{
				count++;
			}			}

		}
		
	}
