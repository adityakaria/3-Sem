import java.rmi.*;
import java.rmi.server.*;

public class AskServer
{
	public static void main(String[] args)
	{
		try
        { 
            // Create an object of the interface 
            // implementation class 
            remote_interface obj = new remote_ask();

            // rmiregistry within the server JVM with 
            // port number 1900 
            LocateRegistry.createRegistry(1900); 
  
            // Binds the remote object by the name 
            // geeksforgeeks 
            Naming.rebind("rmi://localhost:1900"+ 
                          "/geeksforgeeks",obj); 
        } 
        catch(Exception ae) 
        { 
            System.out.println(ae); 
        } 
	}
}