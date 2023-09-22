import java.util.ArrayList;

public class PacientesOrden implements IAgregarPaciente {
    
    static ArrayList<Paciente> list0 = new ArrayList<>();

    public void agregarPaciente(Paciente paciente) {
        list0.add(paciente);
    }

    public ArrayList<Paciente> getList(){
        return list0;
    }
    
}
