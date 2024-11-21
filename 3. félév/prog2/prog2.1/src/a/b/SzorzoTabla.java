package a.b;

import java.util.Scanner;

public class SzorzoTabla {
    static int currentRow = 1;
    public static Scanner scanner = new Scanner(System.in).useDelimiter("\\n");

    public static void main(String[] args) {
        System.out.println("Add meg a sor számát: ");
        currentRow = Integer.parseInt(scanner.nextLine());
    }

    public int getCurrentRow() {
        return currentRow;
    }
}
