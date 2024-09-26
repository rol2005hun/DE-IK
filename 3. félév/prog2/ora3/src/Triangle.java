
import static java.lang.Math.sqrt;

public class Triangle {
    private double first;
    private double second;
    private double third;
    private final double felkerulet = (first + second + third) / 2;

    public double getFirst() {
        return first;
    }

    public double getSecond() {
        return second;
    }

    public double getThird() {
        return third;
    }

    public double getFelkerulet() {
        return felkerulet;
    }

    public void setFirst(double first) {
        this.first = first;
    }

    public void setSecond(double second) {
        this.second = second;
    }

    public void setThird(double third) {
        this.third = third;
    }

    public boolean canBeTriangle() {
        return first + second > third || first + third > second || second + third > first;
    }

    public double kerulet() {
        return first + second + third;
    }

    public double terulet() {
        return sqrt(felkerulet * (felkerulet - first) * (felkerulet - second) * (felkerulet - third));
    }
}
