package a.b;

import java.io.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Szoveges {
    public static void main(String[] args) throws IOException {
        File szoveges=new File("szoveg.txt");
        BufferedWriter ki = new BufferedWriter(new FileWriter(szoveges));
        BufferedReader bebe=new BufferedReader(new InputStreamReader(System.in));
        String sor=null;
        do{
            try {
                sor=bebe.readLine();
                ki.append(sor);
                ki.newLine();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }while(!sor.equals("vege"));
        ki.flush();
        bebe.close();
        ki.close();

        BufferedReader be =new BufferedReader(new FileReader(szoveges));
        sor=null;
        while((sor=be.readLine())!=null) {
            Pattern p = Pattern.compile("\\b[A-Z0-9._%-]+@[A-Z0-9.-]+\\.[A-Z]{2,4}\\b");
            Matcher m = p.matcher("foobar@gmail.com");

            if (m.find())
                System.out.println("Correct!");
            System.out.println(sor);
        }
        be.close();
    }
}
