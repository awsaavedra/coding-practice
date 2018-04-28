package mooc.vandy.java4android.calculator.logic;

/**
 * Perform the Multiply operation.
 */
public class Multiply {
    Arguments<Integer, Integer> arguments = new Arguments<>();

    public Multiply(int number1, int number2) {
        arguments.setNumber1(number1);
        arguments.setNumber2(number2);
    }

    public int getResult(){
        return arguments.getNumber1() * arguments.getNumber2();
    }
}
