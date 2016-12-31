package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here
        BaseHamburger hamburger = new BaseHamburger("Basic", "Sausage", 3.56, "White");
        double price = hamburger.itemizeHamburger();
        hamburger.addHamburgerAddition1("Tomato", 0.27);
        hamburger.addHamburgerAddition2("Lettuce", 0.75);
        hamburger.addHamburgerAddition3("Cheese", 1.12);
        price = hamburger.itemizeHamburger();
        System.out.println("Total burger price is " + hamburger.itemizeHamburger());

        HealthyBurger healthyBurger = new HealthyBurger("Bacon", 5.67);
        healthyBurger.addHamburgerAddition1("Egg", 5.43);
        healthyBurger.addHamburgerAddition2("Lentils", 3.41);
        System.out.println("Total Healthy Burger price is " + healthyBurger.itemizeHamburger());

        System.out.println(" ");
        DeluxeHamburger db = new DeluxeHamburger();
        //prevent methods from being called in deluxe burger
        db.itemizeHamburger();
        db.addHamburgerAddition1("Test", 1.54);
    }
}
