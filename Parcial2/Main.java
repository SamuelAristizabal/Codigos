import java.util.ArrayList;
import java.util.List;

class Main{

    public static void main(String[] args) {
        
        Paciente a = new Paciente("Elena", 232, 11);
        Paciente b = new Paciente("Diego", 123, 9);

        List<Paciente> listaPacientes = new ArrayList<>();
        listaPacientes.add(a);
        listaPacientes.add(b);
        

        ControlDelHospital.enviarPacientes(listaPacientes);
        

    }
}