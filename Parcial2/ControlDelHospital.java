import java.util.ArrayList;
import java.util.List;

public class ControlDelHospital {
    
    public static void enviarPacientes(List<Paciente> paciente) {
        
        ZonadeUrgencias zonadeUrgencias = new ZonadeUrgencias();
        ArrayList<Paciente> pacientes = zonadeUrgencias.hacerTriaje(paciente);
        Hospital hospital = new Hospital();
        hospital.recibirPacientes(pacientes);
    
    }

}
