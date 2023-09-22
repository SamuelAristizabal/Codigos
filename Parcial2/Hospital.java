import java.util.ArrayList;


public class Hospital {

    public void recibirPacientes(ArrayList<Paciente> pacientes) {

        for (Paciente paciente : pacientes) {
            if (paciente instanceof PacienteCritico) {

                PacienteCritico pacienteCritico = (PacienteCritico) paciente;
                pacienteCritico.operar(pacienteCritico.getName());
                pacienteCritico.medicar(pacienteCritico.getName());
                pacienteCritico.darDeAlta(pacienteCritico.getName());
                
            } else if (paciente instanceof PacienteUrgente) {
                
                PacienteUrgente pacienteUrgente = (PacienteUrgente) paciente;

                pacienteUrgente.medicar(pacienteUrgente.getName());
                pacienteUrgente.darDeAlta(pacienteUrgente.getName());
                
            }
        }
    }

    
}
