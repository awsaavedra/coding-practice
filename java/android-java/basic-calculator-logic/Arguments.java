package mooc.vandy.java4android.calculator.logic;

/**
 * Created by Alexander on 4/24/18.
 * Common numbers as arguments between all
 * operator classes: Add, Subtract, Multiply, Divide
 */

public class Arguments<Number1, Number2> {

    private Number1 mNumber1;
    private Number2 mNumber2;

    ///////GETTERS AND SETTERS\\\\\\\
    public Number1 getNumber1() { return mNumber1; }

    public Number2 getNumber2() { return mNumber2; }

    public void setNumber1(Number1 mNumber1) { this.mNumber1 = mNumber1; }

    public void setNumber2(Number2 mNumber2) { this.mNumber2 = mNumber2; }
}
