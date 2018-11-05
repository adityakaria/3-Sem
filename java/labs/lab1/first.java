import java.util.Scanner;

class first
{
	public first()
	{

	}


	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);

		String choice = "";
		a:
		do
		{

			System.out.println("Enter Alphabet");
			char x = in.next().charAt(0);

			if ((x >= 97 && x <= 122) || (x >= 65 && x <= 90))
			{
				switch (x)
				{
					case 'a': case 'A':
					case 'e': case 'E':
					case 'i': case 'I':
					case 'o': case 'O':
					case 'u': case 'U':
						System.out.println("Vowel");
						break;
					default:
						System.out.println("Consonant");
						break;
				}
			}
			else
			{
				System.out.println("Error: Please Enter a valid Alphabet");
				continue a;
			}

			System.out.println("Do you wish to check another alphabet? (y/n)");
			in.nextLine();
			choice = in.nextLine();
		}
		while (choice.equals("y"));
	}
}
