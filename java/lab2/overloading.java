class Defn
{
   public void disp(char c, int num)
   {
       System.out.println("I’m the first definition of method disp");
       System.out.println(c +" " + num);
   }
   public void disp(int num, char c)
   {
       System.out.println("I’m the second definition of method disp" );
       System.out.println(num + " " + c);
   }
}
class overloading
{
   public static void main(String args[])
   {
       Defn obj = new Defn();
       obj.disp('x', 9 );
       obj.disp(6, 'y');
   }
}