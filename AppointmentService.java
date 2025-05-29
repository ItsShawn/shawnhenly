import java.util.HashMap;
import java.util.Map;

public class AppointmentService {
    private Map<String, Appointment> appointments = new HashMap<>();
    private Map<String, Contact> contacts = new HashMap<>();

    // Appointment methods
    public boolean addAppointment(Appointment appointment) {
        if (appointments.containsKey(appointment.getAppointmentID())) {
            return false;
        }
        appointments.put(appointment.getAppointmentID(), appointment);
        return true;
    }

    public boolean deleteAppointment(String appointmentID) {
        if (appointments.containsKey(appointmentID)) {
            appointments.remove(appointmentID);
            return true;
        }
        return false;
    }

    public Appointment getAppointment(String appointmentID) {
        return appointments.get(appointmentID);
    }

    // Contact methods
    public boolean addContact(Contact contact) {
        if (contacts.containsKey(contact.getContactID())) {
            return false;
        }
        contacts.put(contact.getContactID(), contact);
        return true;
    }

    public boolean deleteContact(String contactID) {
        if (contacts.containsKey(contactID)) {
            contacts.remove(contactID);
            return true;
        }
        return false;
    }

    public Contact getContact(String contactID) {
        return contacts.get(contactID);
    }
}
