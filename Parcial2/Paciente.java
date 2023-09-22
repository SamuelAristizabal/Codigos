public class Paciente {
    protected String name;
    protected int numIdent;
    protected int Sintomas;

    public Paciente(String name, int numIdent, int sintomas) {
        this.name = name;
        this.numIdent = numIdent;
        Sintomas = sintomas;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getNumIdent() {
        return numIdent;
    }

    public void setNumIdent(int numIdent) {
        this.numIdent = numIdent;
    }

    public int getSintomas() {
        return Sintomas;
    }

    public void setSintomas(int sintomas) {
        Sintomas = sintomas;
    }

}