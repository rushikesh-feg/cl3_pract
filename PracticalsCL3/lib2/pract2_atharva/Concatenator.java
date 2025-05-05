// File: Concatenator.java

import java.rmi.Remote;
import java.rmi.RemoteException;

// Remote interface
public interface Concatenator extends Remote {
    String concatenate(String a, String b) throws RemoteException;
}
