// File: Server.java

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class Server {
    public static void main(String[] args) {
        try {
            // Start the RMI registry
            LocateRegistry.createRegistry(1099);

            // Create and bind the remote object
            ConcatenatorImpl obj = new ConcatenatorImpl();
            Naming.rebind("Concatenator", obj);

            System.out.println("Server is ready. RMI Object bound as 'Concatenator'.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
