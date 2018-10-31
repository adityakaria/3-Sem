import java.util.Scanner;

class strDupl
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);

		System.out.println("Enter a string: ");
		String str = in.nextLine();

		char [] str1 = str.toCharArray();
		boolean [] flag = new boolean[str.length()];
		for (int i = 0; i < str.length(); i++)
			flag[i] = false;

		for (int i = 0; i < str.length(); i++)
		{
			int count = 0;
			for (int j = i; j < str.length(); j++)
			{
				if (str1[i] == str1[j])
				{
					count++;
				}
			}
			if (count > 1 && flag[i] != true)
			{
				System.out.print(str1[i] + "(" + count  + ") ");
				flag[i] = true;
			}
		}
		System.out.println("");
	}
}