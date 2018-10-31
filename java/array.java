import java.util.ArrayList;

public class array
{
	public static void main(String[] args)
	{
		ArrayList<Integer> list = new ArrayList<Integer>();

		int a = 7;
		list.add(5);
		list.add(a);
		
		list.add(3);

		list.add(3);
		list.add(3);
		list.add(1,69);

		for (int i = 0; i < list.size(); i++)
		{
			System.out.println(list.get(i));
		}

		System.out.println("Result: " + (list.get(0) + list.get(1)));
	}
}