package com.company;

/**
 * Created by awsaavedra on 12/29/16.
 */
public class DeluxeHamburger extends BaseHamburger{
    public DeluxeHamburger() {
        super("Deluxe", "Sausage and Bacon" , 14.54, "White");
        super.addHamburgerAddition1("Chips", 2.75);
        super.addHamburgerAddition2("Drink", 1.81);

    }

    @Override
    public void addHamburgerAddition1(String name, double price) {
        System.out.println("Cannot add additional items");
    }

    @Override
    public void addHamburgerAddition2(String name, double price) {
        System.out.println("Cannot add additional items");
    }

    @Override
    public void addHamburgerAddition3(String name, double price) {
        System.out.println("Cannot add additional items");
    }

    @Override
    public void addHamburgerAddition4(String name, double price) {
        System.out.println("Cannot add additional items");
    }
}
