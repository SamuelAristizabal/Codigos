import java.util.ArrayList;

public class ZonadeUrgencias implements ITriaje {
    
    public ArrayList<Paciente> hacerTriaje(Paciente paciente) {
        PacientesOrden orden = new PacientesOrden();
        
        if (paciente.getSintomas() > 10) {
            
            PacienteCritico a = new PacienteCritico(paciente.getName(), paciente.getNumIdent(), paciente.getSintomas());

            orden.agregarPaciente(a);
        } else {
            PacienteUrgente b = new PacienteUrgente(paciente.getName(), paciente.getNumIdent(), paciente.getSintomas());

            orden.agregarPaciente(b);
        }

        ArrayList<Paciente> list0 = orden.getList();

        return list0;
    }
    
}
