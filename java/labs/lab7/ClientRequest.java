import java.rmi.*;

public class ClientRequest
{
	 public static void main(String args[]) 
    { 
        String answer,value="Aditya"; 
        try
        { 
            // lookup method to find reference of remote object 
            remote_interface access = 
                (remote_interface)Naming.lookup("rmi://localhost:1900"+ 
                                      "/geeksforgeeks"); 
            answer = access.Query(value); 
            System.out.println("Article on " + value + 
                            " " + answer+" at GeeksforGeeks"); 
        } 
        catch(Exception ae) 
        { 
            System.out.println(ae); 
        } 
    } 
}