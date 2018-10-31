class MultithreadingDemo implements Runnable
{
    public void run()
    {
        try
        {
            for (int p = 0; p < 4; p++)
            {
                System.out.println ("Thread " +
                                Thread.currentThread().getId() +
                                " is running");
                Thread.sleep(1000);
            }

        }
        catch (Exception e)
        {
            System.out.println ("Exception is caught");
        }
    }
}

// Main Class
class mult2
{
    public static void main(String[] args)
    {
        int n = 10;
        for (int i=0; i<n; i++)
        {
            Thread object = new Thread(new MultithreadingDemo());
            object.start();
        }
    }
}