class MultithreadingDemo extends Thread
{
    public void run()
    {
        try
        {
            System.out.println ("Thread " +
                  Thread.currentThread().getId() +
                  " is running");
            Thread.sleep(1000);
            System.out.println("----");

        }
        catch (Exception e)
        {
            System.out.println ("Exception caught");
        }
    }
}

public class mult1
{
    public static void main(String[] args)
    {
        int n = 3;
        for (int i=0; i<n; i++)
        {
            MultithreadingDemo object = new MultithreadingDemo();
            object.start();
        }
    }
}