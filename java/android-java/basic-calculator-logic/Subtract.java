package mooc.vandy.java4android.calculator.logic;

/**
 * Perform the Subtract operation.
 */
public class Subtract {
    Arguments<Integer, Integer> arguments = new Arguments<>();

    public Subtract(int number1, int number2) {
        arguments.setNumber1(number1);
        arguments.setNumber2(number2);
    }

    public int getResult(){
        return arguments.getNumber1() - arguments.getNumber2();
    }
}
