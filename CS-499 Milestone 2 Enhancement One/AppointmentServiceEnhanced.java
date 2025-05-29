import java.util.HashMap;
import java.util.Map;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

// Define custom exception
class AppointmentException extends RuntimeException {
    public AppointmentException(String message) {
        super(message);
    }
}

// Define interfaces
interface IAppointmentService {
    boolean createAppointment(Appointment appointment);
    boolean deleteAppointment(String appointmentID);
    Appointment getAppointment(String appointmentID);
}

interface IContactService {
    boolean createContact(Contact contact);
    boolean deleteContact(String contactID);
    Contact getContact(String contactID);
}

// Appointment service implementation
public class AppointmentService implements IAppointmentService, IContactService {
    private static final Logger logger = LoggerFactory.getLogger(AppointmentService.class);

    private final Map<String, Appointment> appointments = new HashMap<>();
    private final Map<String, Contact> contacts = new HashMap<>();

    // Appointment methods
    @Override
    public boolean createAppointment(Appointment appointment) {
        if (appointment == null || appointment.getAppointmentID() == null) {
            logger.error("Invalid appointment data.");
            throw new AppointmentException("Appointment data is null or missing ID.");
        }

        if (appointments.containsKey(appointment.getAppointmentID())) {
            logger.warn("Appointment with ID {} already exists.", appointment.getAppointmentID());
            return false;
        }

        appointments.put(appointment.getAppointmentID(), appointment);
        logger.info("Appointment with ID {} created successfully.", appointment.getAppointmentID());
        return true;
    }

    @Override
    public boolean deleteAppointment(String appointmentID) {
        if (appointments.remove(appointmentID) != null) {
            logger.info("Appointment with ID {} deleted successfully.", appointmentID);
            return true;
        }
        logger.warn("Attempted to delete non-existent appointment ID {}", appointmentID);
        return false;
    }

    @Override
    public Appointment getAppointment(String appointmentID) {
        return appointments.get(appointmentID);
    }

    // Contact methods
    @Override
    public boolean createContact(Contact contact) {
        if (contact == null || contact.getContactID() == null) {
            logger.error("Invalid contact data.");
            throw new AppointmentException("Contact data is null or missing ID.");
        }

        if (contacts.containsKey(contact.getContactID())) {
            logger.warn("Contact with ID {} already exists.", contact.getContactID());
            return false;
        }

        contacts.put(contact.getContactID(), contact);
        logger.info("Contact with ID {} created successfully.", contact.getContactID());
        return true;
    }

    @Override
    public boolean deleteContact(String contactID) {
        if (contacts.remove(contactID) != null) {
            logger.info("Contact with ID {} deleted successfully.", contactID);
            return true;
        }
        logger.warn("Attempted to delete non-existent contact ID {}", contactID);
        return false;
    }

    @Override
    public Contact getContact(String contactID) {
        return contacts.get(contactID);
    }
}