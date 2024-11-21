package a.b;
import java.text.DateFormat;
import java.util.Arrays;

class Tantargyak {

}
public class Hallgato extends Ember {
    public static final int ELEMEK_SZAMA = 10;
    private String neptunkod;
    private String szak;
    private String evfolyam;
    private int targyakszama = 0;
    private Tantargyak[] tantargyak = new Tantargyak[ELEMEK_SZAMA];

    public Hallgato() {

    }

    public Hallgato(String nev, int szev, String nem, int jovedelem, String neptunkod, String szak, int targyakszama, String evfolyam) {
        super(nev, szev, nem, jovedelem);
        this.neptunkod = neptunkod;
        this.szak = szak;
        this.targyakszama = targyakszama;
        this.evfolyam = evfolyam;
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("Hallgato{");
        sb.append("neptunkod='").append(neptunkod).append('\'');
        sb.append(", szak='").append(szak).append('\'');
        sb.append(", evfolyam='").append(evfolyam).append('\'');
        sb.append(", targyakszama=").append(targyakszama == 0 ? "nincs felvett" : targyakszama);
        sb.append(", tantargyak=").append(targyakszama == 0 ? "nincsen neki" : tantargyak);
        sb.append('}');
        return sb.toString();
    }
}
