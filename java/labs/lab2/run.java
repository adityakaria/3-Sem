import java.util.Scanner;

class car
{
	int number;
	String colour;
	float mileage;

	Scanner in = new Scanner(System.in);

	public car()
	{

	}

	public car(int no, float mil)
	{
		this.number = no;
		this.mileage = mil;
	}

	public car(int no)
	{
		this.number = no;
		this.mileage = 0;
	}

	public void display()
	{
		System.out.println("Car no: " + this.number + "\nmileage: " + mileage);
		System.out.println();
	}

	public void start()
	{
		System.out.println("Key inserted");
		System.out.println("Key Turned");
		System.out.println("Vroom! Vroom!");
		System.out.println();
	}

	public int check_seatbelt()
	{
		System.out.println("Did you wear the seatbelt? (y/n)");
		char check = in.next().charAt(0);

		switch (check)
		{
			case 'y': case 'Y':
				return 1;
			case 'n': case 'N':
				return 0;
			default:
				System.out.println("Invalid Input. Can't trust you. Are you drinking and driving?");
				return 9;
		}
	}

	public void stop()
	{
		System.out.println("Brake!!");
		System.out.println("Okay, stopped.");
		System.out.println();
	}
}

class old_car extends car
{
	int number;
	String colour;
	float mileage;
	int year;

	Scanner in = new Scanner(System.in);

	public old_car(int no, float mil, int y)
	{	
		super();
		this.number = no;
		this.mileage = mil;
		this.year = y;
	}

	public old_car(int no, int y)
	{
		super(no, 1.009f);
		this.number = no;
		this.mileage = -9.00f;
		year = y;
	}

	public void display()
	{
		System.out.println("Car no: " + this.number + "\nmileage: " + mileage + "\nyear: " + this.year);
		System.out.println();
	}

	public void start()
	{
		System.out.println("Key inserted");
		System.out.println("Key Turned");
		System.out.println("Ehehehehe Ehehehehe");
		System.out.println("Sorry, your car is old. It won't start");
		System.out.println();
	}

	public int check_seatbelt()
	{
		System.out.println("Did you wear the seatbelt? (y/n)");
		char check = in.next().charAt(0);

		switch (check)
		{
			case 'y': case 'Y':
				return 1;
			case 'n': case 'N':
				return 0;
			default:
				System.out.println("Invalid Input. Can't trust you. Are you drinking and driving?");
				return 9;
		}
	}

	public void check_year()
	{
		System.out.println("Year of make: " + this.year);
		System.out.println();
	}

	public void stop()
	{
		System.out.println("Brake!!");
		System.out.println("--__--, car doesnt run only!");
		System.out.println();
	}

}

class run
{
	public static void main(String[] args)
	{
		car car1 = new car(100, 20.60f);
		car car2 = new car(101);
		
		car1.display();
		System.out.println("Seatbelt: " + car1.check_seatbelt());
		car1.start();
		car1.stop();

		car2.display();

		old_car car3 = new old_car(9, 1.1f, 1999);
		old_car car4 = new old_car(20, 1990);

		car3.display();
		System.out.println("Seatbelt: " + car3.check_seatbelt());
		car3.start();
		car3.stop();
		car3.check_year();

		car4.display();
		car4.check_year();
	}
}
