import java.rmi.*;
import java.rmi.server.*;

public class remote_ask extends UnicastRemoteObject implements remote_interface
{
	public remote_ask() throws RemoteException {
		super();
	}

	public String Query(String s) throws RemoteException
	{
		if ((s.equals("Aditya")) || (s.equals("aditya")))
			return "Nice name";
		return "Thu! Useless name";
	}
}


// to make stub and skeleton objects using 'rmic': $ rmic remote_ask

// Start the registry service by issuing the following command at the command prompt: $ start rmiregistry