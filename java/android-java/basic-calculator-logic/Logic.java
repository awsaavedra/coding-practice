package mooc.vandy.java4android.calculator.logic;

import mooc.vandy.java4android.calculator.ui.ActivityInterface;

/**
 * Performs an operation selected by the user.
 */
public class Logic implements LogicInterface {
    /**
     * Reference to the Activity output.
     */
    protected ActivityInterface mOut;
    /**
     * Constructor initializes the field.
     */
    public Logic(ActivityInterface out){ mOut = out; }
    /**
     * Perform the @a operation on @a argumentOne and @a argumentTwo.
     */
    public void process(int argumentOne,
                        int argumentTwo,
                        int operation){
        switch (operation){
            case 1:
                Add add = new Add(argumentOne, argumentTwo);
                mOut.print(Integer.toString(add.getResult()));
                break;
            case 2:
                Subtract subtract = new Subtract(argumentOne, argumentTwo);
                mOut.print(Integer.toString(subtract.getResult()));
                break;
            case 3:
                Multiply multiply = new Multiply(argumentOne, argumentTwo);
                mOut.print(Integer.toString(multiply.getResult()));
                break;
            case 4:
                if( argumentTwo != 0){
                    Divide division = new Divide(argumentOne, argumentTwo);
                    mOut.print(division.getResult());
                    break;
                }else{ mOut.print("You cannot divide by zero"); }
        }
    }
}
