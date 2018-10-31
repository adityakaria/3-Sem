public class hello
{
	int id;
	String name;
	int age;
	String naam = "Jack";

	void get_id(String hesaru)
	{
		name = hesaru;
		id = 1234;
		age = 69;
	}

	public static void main(String[] args)
	{
		System.out.println("Hello World");
		get_id(naam);
		System.out.println("Name: " + name + " " + age + " " + id);
	}
}