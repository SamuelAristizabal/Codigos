import java.util.ArrayList;
import java.util.List;

class Main{

    public static void main(String[] args) {

        List<String[]> listaPaciente = new ArrayList<>();
        String[] a = new String[] { "Elena", "232", "11" };
        String[] b = new String[] { "Diego", "123", "9" };
        String[] c = new String[] { "Samuel", "567", "20"};
        

        listaPaciente.add(a);
        listaPaciente.add(b);
        listaPaciente.add(c);

        ControlDelHospital.enviarPacientes(listaPaciente);

    }
}