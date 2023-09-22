import java.util.ArrayList;

public class ControlDelHospital {
    
    public static void enviarPacientes(Paciente paciente) {
        
        ZonadeUrgencias zonadeUrgencias = new ZonadeUrgencias();
        ArrayList<Paciente> pacientes = zonadeUrgencias.hacerTriaje(paciente);
        Hospital hospital = new Hospital();
        hospital.recibirPacientes(pacientes);
    
    }

}
