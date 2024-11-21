package zh.unideb;

import java.io.*;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Kolcsonzo {
    private List<Film> filmek = new LinkedList<Film>();

    public void feltolt() throws IOException {
        File allomany = new File("filmek.txt");
        BufferedReader be = new BufferedReader(new FileReader(allomany));
        String sor = null;
        while((sor = be.readLine()) != null) {
            StringTokenizer felbont = new StringTokenizer(sor, ",");
            String osztaly = felbont.nextToken();
            String cim = felbont.nextToken();
            String szereplo = felbont.nextToken();
            int hossz = Integer.parseInt(felbont.nextToken());
            double ar = Double.parseDouble(felbont.nextToken());
            int napok = Integer.parseInt(felbont.nextToken());
        }
    }

    public static void main(String[] args) throws IOException {
        Kolcsonzo sajat = new Kolcsonzo();
        sajat.feltolt();
    }
}
