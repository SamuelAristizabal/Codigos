public class PacienteCritico extends Paciente implements IOperar, IMedicar, IDarDeAlta {
    
    public PacienteCritico(String name, int numIdent, int sintomas) {
        super(name, numIdent, sintomas);
    }
    
    public void operar(String name) {
        System.out.println("Operando a " + name);

    }

    public void medicar(String name) {
        System.out.println("Medicando a " + name);
    }

    public void darDeAlta(String name) {
        System.out.println("Dando de Alta a " + name);
    }
}
