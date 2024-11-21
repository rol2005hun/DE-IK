package a.b;

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Tombos {
    public static void main(String[] args) {
        int[] tomb = new int[10];
        tomb[5]=5;
        Random veletlen = new Random();
        Arrays.fill(tomb, veletlen.nextInt(20));
        Arrays.fill(tomb, 5,7,veletlen.nextInt(20));
        System.out.println(Arrays.toString(tomb));

        /*for (int i=0;i<10;i++){
            tomb[i]=veletlen.nextInt(20);
        }
        for (int i = 0; i < 10; i++) {
            System.out.println(tomb[i]+'\t');
        }
        Arrays.sort(tomb);
        for (int i = 0; i < 10; i++) {
            System.out.println(tomb[i]+'\t');
        }*/

        Scanner be = new Scanner(System.in);
        int szam = be.nextInt();
        System.out.println(Arrays.binarySearch(tomb, szam) == 1 ? "benne van" : "nincs benne");
    }
}
