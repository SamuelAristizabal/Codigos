import java.util.ArrayList;
import java.util.List;

public class ZonadeUrgencias implements ITriaje {
    
    @Override
    public ArrayList<Paciente> hacerTriaje(List<String[]> ListadePacientes) {
        
        ArrayList<Paciente> list = new ArrayList<>();
        int numeroDeSintomas = 0;

        for (String[] infoPaciente : ListadePacientes) {
            numeroDeSintomas = Integer.parseInt(infoPaciente[2]);
            
            if (numeroDeSintomas > 10) {
            
                PacienteCritico a = new PacienteCritico(infoPaciente[0], infoPaciente[1], infoPaciente[2]);

                
                list.add(a);

            } else {
                PacienteUrgente b = new PacienteUrgente(infoPaciente[0], infoPaciente[1], infoPaciente[2]);

                list.add(b);
            }
        }
        
        
        return list;
    }

    
    
}
