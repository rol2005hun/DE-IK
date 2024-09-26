public class App {
    public static void main(String[] args) throws Exception {
        Triangle triangle = new Triangle();
        triangle.setFirst(1.5);
        triangle.setSecond(2.5);
        triangle.setThird(5.7);

        System.out.println(triangle.canBeTriangle());
        System.out.println(triangle.kerulet());
        System.out.println(triangle.terulet());
    }
}
