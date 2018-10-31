public class hello1
{
	int id;
	String name;
	int age;

	public hello1(String name)
	{
		this.name = name;
		this.id = 1111;
		this.age =69;
	}

	public String get_name()
	{
		return name;
	}

	public int get_id()
	{
		return id;
	}
	
	public static void main(String[] args)
	{
		hello1 ins = new hello1("Aditya");

		System.out.println("Hello World");
		System.out.println("Name: " + ins.get_name() + " ID: " +ins.get_id());
	}
}














































