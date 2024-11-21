package zh.unideb;

public class Main {
    public static void main(String[] args) {
        Film karib = new Film("karib tenger", "jek sperow", 120, 1200, 5, FilmTipus.AKCIO);
        System.out.println(karib.toString());
    }
}
