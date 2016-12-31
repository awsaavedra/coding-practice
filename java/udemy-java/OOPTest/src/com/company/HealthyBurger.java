package com.company;

/**
 * Created by awsaavedra on 12/29/16.
 */
public class HealthyBurger extends BaseHamburger{
    private String healthyExtraName1;
    private double healthyExtraAmount1;

    private String healthyExtraName2;
    private double healthyExtraAmount2;

    public HealthyBurger(String meat, double price) {
        super("Healthy", meat, price, "Brown rye");
    }

    public void addHealthAddition1(String name, double price){
        this.healthyExtraName1 = name;
        this.healthyExtraAmount1 = price;
    }

    public void addHealthAddition2(String name, double price){
        this.healthyExtraName2 = name;
        this.healthyExtraAmount2 = price;
    }

    @Override
    public double itemizeHamburger() {
        double hamburgerPrice = super.itemizeHamburger(); //calls method in super class for
        //basic hamburger + 4 additions
        if(this.healthyExtraName1 != null){
            hamburgerPrice += this.healthyExtraAmount1;
            System.out.println("Added " + this.healthyExtraName1 + " for an extra " + this.healthyExtraAmount1);
        }
        if(this.healthyExtraName2 != null){
            hamburgerPrice += this.healthyExtraAmount2;
            System.out.println("Added " + this.healthyExtraName2 + " for an extra " + this.healthyExtraAmount2);
        }

        return hamburgerPrice;

    }
}
