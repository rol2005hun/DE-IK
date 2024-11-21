package zh.unideb;

import java.util.Objects;

public class Film implements FilmInterface {
    private String cim;
    private String foszereplo;
    private int hossz;
    private double kolcsonzesiar;
    private int napokszama;
    private FilmTipus tipus;

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("Film{");
        sb.append("cim=").append(cim).append('\n');
        sb.append(", foszereplo=").append(foszereplo).append('\n');
        sb.append(", hossz=").append(oraPerc()).append('\n');
        sb.append(", kolcsonzesiar=").append(kolcsonzesiar).append('\n');
        sb.append(", napokszama=").append(napokszama).append('\n');
        sb.append(", tipus=").append(tipus).append('\n');
        sb.append('}');
        return sb.toString();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Film film = (Film) o;
        return getHossz() == film.getHossz() && Double.compare(getKolcsonzesiar(), film.getKolcsonzesiar()) == 0 && getNapokszama() == film.getNapokszama() && Objects.equals(getCim(), film.getCim()) && Objects.equals(getFoszereplo(), film.getFoszereplo()) && getTipus() == film.getTipus();
    }

    @Override
    public int hashCode() {
        int result = Objects.hashCode(getCim());
        result = 31 * result + Objects.hashCode(getFoszereplo());
        result = 31 * result + getHossz();
        result = 31 * result + Double.hashCode(getKolcsonzesiar());
        result = 31 * result + getNapokszama();
        result = 31 * result + Objects.hashCode(getTipus());
        return result;
    }

    public void setCim(String cim) {
        this.cim = cim;
    }

    public void setFoszereplo(String foszereplo) {
        this.foszereplo = foszereplo;
    }

    public void setHossz(int hossz) {
        this.hossz = hossz;
    }

    public void setKolcsonzesiar(double kolcsonzesiar) {
        this.kolcsonzesiar = kolcsonzesiar;
    }

    public void setNapokszama(int napokszama) {
        this.napokszama = napokszama;
    }

    public void setTipus(FilmTipus tipus) {
        this.tipus = tipus;
    }

    public String getCim() {
        return cim;
    }

    public String getFoszereplo() {
        return foszereplo;
    }

    public int getHossz() {
        return hossz;
    }

    public double getKolcsonzesiar() {
        return kolcsonzesiar;
    }

    public int getNapokszama() {
        return napokszama;
    }

    public FilmTipus getTipus() {
        return tipus;
    }

    public Film(String cim, String foszereplo, int hossz, double kolcsonzesiar, int napokszama, FilmTipus tipus) {
        this.cim = cim;
        this.foszereplo = foszereplo;
        this.hossz = hossz;
        this.kolcsonzesiar = kolcsonzesiar;
        this.napokszama = napokszama;
        this.tipus = tipus;
    }

    public String oraPerc() {
        int ora, perc;
        ora = hossz / 60;
        perc =hossz%60;
        return ora + " óra " + perc + " perc.";
    }

    @Override
    public int hanyszor() {
        return napokszama * 24 * 60 / hossz;
    }

    @Override
    public int osszbevetel(Boolean torzsvendeg) {
        double osszeg = kolcsonzesiar * napokszama;
        if (torzsvendeg) {
            osszeg = osszeg * 0.9;
        }
        return (int) osszeg;
    }
}
