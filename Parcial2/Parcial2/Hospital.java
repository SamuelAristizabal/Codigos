import java.util.ArrayList;


public class Hospital {

    public void recibirPacientes(ArrayList<Paciente> pacientes) {

        for (Paciente paciente : pacientes) {
            paciente.atender();
        }
    }

    
}
