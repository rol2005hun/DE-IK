package a.b;

import java.io.File;
import java.io.IOException;

public class Allomanyos {
    public static void main(String[] args) {
        File allomany = new File("vmi¸.txt");
        //System.setProperty("user.dir", "jozsi");
        //System.out.println(System.getProperty("user.dir"));
        System.out.println(allomany.getAbsolutePath());
        try {
            System.out.println(allomany.getCanonicalPath());
            boolean letr=allomany.createNewFile();
            File temp=     File.createTempFile("orai",".tmp");;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            System.out.println(temp.getAbsolutePath());
            ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            temp.deleteOnExit();
            if(temp.exists()) {
                System.out.println(                 "letezi                    ");
                File regi=                    new File("regi.txt");
                regi.createNewFile();
                File uj =                             new File("uj.txt");

                regi.renameTo(uj);
            }


            File konyvtar=new File("c:\\");
            File[] gyoker=konyvtar.listFiles();
            for (File f:gyoker) {
                System.out.println(f);
            }
        } catch (IOException e) {
            System.out.println("hiba ");
            e.printStackTrace();
        }
    }
}
