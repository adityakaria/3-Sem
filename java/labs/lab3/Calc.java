import java.util.*;

class Calc
{
	int a;
	int b;
	public Calc(int a, int b)
	{
		this.a = a;
		this.b = b;
	}

	public int add()
	{
		return a+b;
	}

	public int subtract()
	{
		return a-b;
	}

	public int mult()
	{
		return a*b;
	}

	public void divide()
	{
		try
		{
			int c = a/b;
			System.out.println(c);
			System.out.println("This is inside try catch block");
		}
		catch(ArithmeticException e)
		{
			System.out.println("Warning: Cannot divide by zero");
		}
		catch(Exception e)
		{
			System.out.println("Error: Exception");
		}
		System.out.println("End of try-catch block");
	}

	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.println("Enter integers a and b:");
		int a = in.nextInt();
		int b = in.nextInt();
		Calc calc = new Calc(a, b);
		System.out.println(calc.add());
		System.out.println(calc.subtract());
		System.out.println(calc.mult());
		calc.divide();
		System.out.println("Done");
	}
}