public class Test
{
     int x = 11;
    private int y = 33;

    public void method1(int x)
    {
        Test t = new Test();
        this.x = 55;
        y = 44;
 
        System.out.println("t(inside).x: " + t.x);
        System.out.println("this.x: " + this.x);
        System.out.println("x: " + x);
        System.out.println("t.y: " + t.y);
        System.out.println("y: " + y);
    }
 
    public static void main(String args[])
    {
        Test t = new Test();
        t.method1(5);
        System.out.println("t(outside).x:"+t.x);
    }
}