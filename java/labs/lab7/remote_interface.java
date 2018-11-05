import java.rmi.*;

public interface remote_interface extends Remote
{
	public String Query(String s) throws RemoteException;
}