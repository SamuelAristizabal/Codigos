import java.util.ArrayList;
import java.util.List;

public class ZonadeUrgencias implements ITriaje {
    
    public ArrayList<Paciente> hacerTriaje(List<Paciente> ListadePacientes) {
        PacientesOrden orden = new PacientesOrden();
        
        for(Paciente paciente: ListadePacientes){
            if (paciente.getSintomas() > 10) {
            
                PacienteCritico a = new PacienteCritico(paciente.getName(), paciente.getNumIdent(), paciente.getSintomas());

                
                orden.agregarPaciente(a);
            } else {
                PacienteUrgente b = new PacienteUrgente(paciente.getName(), paciente.getNumIdent(), paciente.getSintomas());

                orden.agregarPaciente(b);
            }
        }
        

        ArrayList<Paciente> list0 = orden.getList();

        return list0;
    }
    
}
