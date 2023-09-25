public class PacienteCritico extends Paciente {
    
    public PacienteCritico(String name, String numIdent, String sintomas) {
        super(name, numIdent, sintomas);
    }
    
    
    public void atender() {
        System.out.println("Paciente Crítico");
        System.out.println("Operando a: " + name);
        System.out.println("Medicando a: " + name);
        System.out.println("Dando de Alta a: " + name);
        System.out.println();
    }
}
