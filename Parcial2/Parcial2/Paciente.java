public abstract class Paciente {
    protected String name;
    protected String numIdent;
    protected String Sintomas;

    public Paciente(String name, String numIdent, String sintomas) {
        this.name = name;
        this.numIdent = numIdent;
        Sintomas = sintomas;
    }

    public void atender() {
        System.out.println("Paciente Urgente");
        System.out.println("Medicando a: " + name);
        System.out.println("Dando de Alta a: " + name);
        System.out.println();
    }
        
    

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getNumIdent() {
        return numIdent;
    }

    public void setNumIdent(String numIdent) {
        this.numIdent = numIdent;
    }

    public String getSintomas() {
        return Sintomas;
    }

    public void setSintomas(String sintomas) {
        Sintomas = sintomas;
    }

}