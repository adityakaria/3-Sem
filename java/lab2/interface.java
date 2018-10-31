interface MyInterface
{
   public void fn1();
   public void fn2();
}
class interface1 implements MyInterface
{
   public void fn1()
   {
	   System.out.println("implementation of method1");
   }

   public void fn2()
   {
	   System.out.println("implementation of method2");
   }

   public static void main(String arg[])
   {
	   MyInterface obj = new interface1();
	   obj.fn2();
     obj.fn1();
   }
}

// Output:
// implementation of method2
// implementation of method1