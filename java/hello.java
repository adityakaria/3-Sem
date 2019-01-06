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
		hello h = new hello();
		h.get_id("naam");
		System.out.println("Name: " + h.name + " " + h.age + " " + h.id);
	}
}