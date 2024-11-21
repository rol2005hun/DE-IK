package a.b;

import java.text.DateFormat;
import java.util.Objects;

public abstract class Ember {
    private String nev;
    private int szev;
    private String nem;
    private int jovedelem;

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("Ember{");
        sb.append("nev='").append(nev).append('\'');
        sb.append(", szev=").append(szev);
        sb.append(", nem='").append(nem).append('\'');
        sb.append(", jovedelem=").append(jovedelem);
        sb.append('}');
        return sb.toString();
    }

    @Override
    public final boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Ember ember)) return false;

        return Objects.equals(getNev(), ember.getNev()) && Objects.equals(getSzev(), ember.getSzev());
    }

    @Override
    public int hashCode() {
        int result = Objects.hashCode(getNev());
        result = 31 * result + Objects.hashCode(getSzev());
        return result;
    }

    public Ember(String nev, int szev, String nem, int jovedelem) {
        this.nev = nev;
        this.szev = szev;
        this.nem = nem;
        this.jovedelem = jovedelem;
    }

    public Ember(){
        this.nev="yuy mara";
    }

    public String getNev() {
        return this.nev;
    }

    public void setNev(String nev) {
        this.nev = nev;
    }

    public int getSzev() {
        return szev;
    }

    public void setSzev(int szev) {
        this.szev = szev;
    }

    public String getNem() {
        return nem;
    }

    public void setNem(String nem) {
        this.nem = nem;
    }

    public int getJovedelem() {
        return jovedelem;
    }

    public void setJovedelem(int jovedelem) {
        this.jovedelem = jovedelem;
    }
}
