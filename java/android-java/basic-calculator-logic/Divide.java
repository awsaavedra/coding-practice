package mooc.vandy.java4android.calculator.logic;

/**
 * Perform the Divide operation.
 */
public class Divide {
    Arguments<Integer, Integer> arguments = new Arguments<>();

    public Divide(Integer number1, Integer number2) {
        arguments.setNumber1(number1);
        arguments.setNumber2(number2);
    }

    public String getResult(){
        return(result(arguments.getNumber1(),arguments.getNumber2()));
    }

    public String result(int numberOne, int numberTwo){
        int remainder = numberOne % numberTwo;
        int number = numberOne / numberTwo;
        return( number + " R: "+ remainder );
    }
}
