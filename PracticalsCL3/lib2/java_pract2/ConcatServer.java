import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.rmi.registry.LocateRegistry;

public class ConcatServer implements Concatenate {
    public String concat(String a, String b){
        return a+b;
    }

    public static void main(String[] args){
        try{
            ConcatServer server = new ConcatServer();
        Concatenate stub = (Concatenate) UnicastRemoteObject.exportObject(server,0);
        Registry registry = LocateRegistry.createRegistry(1099);
        registry.rebind("ConcatService",stub);
        System.out.println("Concatenation Server started");
        }
        catch(Exception e){
            e.printStackTrace();
        }
    }
}
