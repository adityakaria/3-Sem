import java.net.InetAddress;

public class IP
{
	public static void main(String[] args)
	{
		try
		{
			InetAddress ip = InetAddress.getLocalHost();
			System.out.println("Current IP Address:" + ip.getHostAddress());		}
		catch(Exception e)
		{
			System.out.println("Exception caught");
		}
	}
}