import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.util.Scanner;


public class ConcatClient {
    public static void main(String[] args){
        try{

            Registry registry = LocateRegistry.getRegistry();
            Concatenate stub = (Concatenate) registry.lookup("ConcatService");

            Scanner sc = new Scanner(System.in);
            System.out.println("Enter first string : ");
            String a = sc.nextLine();
            System.out.println("Enter second string : ");
            String b = sc.nextLine();
            
            String result = stub.concat(a,b);
            System.out.println("Concatenation result : "+result);
            sc.close();
        }
        catch(Exception e){
            e.printStackTrace();
        }
    }
}
