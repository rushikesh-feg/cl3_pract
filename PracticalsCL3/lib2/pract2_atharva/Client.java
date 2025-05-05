// File: Client.java

import java.rmi.Naming;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        try {
            Scanner scanner = new Scanner(System.in);

            // Lookup the remote object
            System.out.print("Enter the RMI URL (e.g., rmi://localhost/Concatenator): ");
            String url = scanner.nextLine();
            Concatenator concat = (Concatenator) Naming.lookup(url);

            System.out.print("Enter first string: ");
            String s1 = scanner.nextLine();

            System.out.print("Enter second string: ");
            String s2 = scanner.nextLine();

            String result = concat.concatenate(s1, s2);
            System.out.println("Concatenated string: " + result);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
