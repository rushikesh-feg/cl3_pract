// File: ConcatenatorImpl.java

import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

// Implementation of the interface
public class ConcatenatorImpl extends UnicastRemoteObject implements Concatenator {

    protected ConcatenatorImpl() throws RemoteException {
        super();
    }

    @Override
    public String concatenate(String a, String b) throws RemoteException {
        return a + b;
    }
}
