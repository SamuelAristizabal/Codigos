public class PacienteUrgente extends Paciente implements IMedicar, IDarDeAlta {
    
    public PacienteUrgente(String name, int numIdent, int sintomas) {
        super(name, numIdent, sintomas);
    }
    
    public void medicar(String name) {
        System.out.println("Medicando a " + name);
    }

    public void darDeAlta(String name) {
        System.out.println("Dando de Alta a " + name);
    }
}
