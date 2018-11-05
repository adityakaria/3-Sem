class MultithreadingDemo <T> extends Thread
{
    MultithreadingDemo(T id)
    {
        this.setName(id.toString());
    }
    public void run()
    {
        try
        {
            System.out.println ("Thread " +
                  this.getName() +
                  " is running");
            this.sleep(1000);
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
    public static void main(String[] args) throws InterruptedException
    {
        int n = 8;
        for (int i=0; i<n; i++)
        {
            MultithreadingDemo<String> object1 = new MultithreadingDemo<String>("ID1 " + i);
            object1.start();
            // object1.join();
            MultithreadingDemo<Integer> object2 = new MultithreadingDemo<Integer>(i);
            object2.start();
            try{Thread.sleep(1001);}catch(Exception e){}
        }
    }
}