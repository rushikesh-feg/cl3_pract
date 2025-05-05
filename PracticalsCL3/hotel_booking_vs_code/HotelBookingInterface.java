
/**
 * Write a description of interface HotelBookingInterface here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface HotelBookingInterface extends Remote {
    String bookRoom(String guestName, int roomNumber) throws RemoteException;
    String cancelBooking(String guestName, int roomNumber) throws RemoteException;
    String viewBookings() throws RemoteException; // ✅ New method
}
