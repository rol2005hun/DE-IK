package zh.unideb;

public class AkcioFilm extends Film implements AkcioFilmInterface {
    private int aldozatokszama;

    public AkcioFilm(String cim, String foszereplo, int hossz, double kolcsonzesiar, int napokszama, FilmTipus tipus, int aldozatokszama) {
        super(cim, foszereplo, hossz, kolcsonzesiar, napokszama, tipus);
        this.aldozatokszama = aldozatokszama;
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("AkcioFilm{");
        sb.append("aldozatokszama=").append(aldozatokszama);
        sb.append('}');
        return super.toString() + sb.toString();
    }

    public int getAldozatokszama() {
        return aldozatokszama;
    }

    public void setAldozatokszama(int aldozatokszama) {
        this.aldozatokszama = aldozatokszama;
    }

    @Override
    public double otpercenkent() {
        int hanyotperc = getHossz() / 5;
        return (double) aldozatokszama /hanyotperc;
    }

    @Override
    public Boolean hasonloanveres(AkcioFilm film) {
        return otpercenkent() == film.otpercenkent();
    }

    @Override
    public int besorolas() {
        double otperc =this.otpercenkent();
        if(otperc < 1) {
            return 8;
        } else if (otperc < 5){
            return 12;
        } else if (otperc < 10){
            return 16;
        }
        return 18;
    }
}
