package com.company;

/**
 * Created by awsaavedra on 12/29/16.
 */
public class BaseHamburger {

    private String name;
    private String meat;
    private double price;
    private String breadRollType;


    private String addition1Name;
    private double addition1Amount;

    private String addition2Name;
    private double addition2Amount;

    private String addition3Name;
    private double addition3Amount;

    private String addition4Name;
    private double addition4Amount;

    public BaseHamburger(String name, String meat, double price, String breadRollType) {
        this.name = name;
        this.meat = meat;
        this.price = price;
        this.breadRollType = breadRollType;
    }

    public void addHamburgerAddition1(String name, double price){
        this.addition1Name = name;
        this.addition1Amount = price;
    }

    public void addHamburgerAddition2(String name, double price){
        this.addition2Name = name;
        this.addition2Amount = price;
    }

    public void addHamburgerAddition3(String name, double price){
        this.addition3Name = name;
        this.addition3Amount = price;
    }

    public void addHamburgerAddition4(String name, double price){
        this.addition4Name = name;
        this.addition4Amount = price;
    }

    public double itemizeHamburger(){
        double hamburgerPrice = this.price;
        System.out.println(this.name + " hamburger " + " on a " + this.breadRollType + " roll "
                + "price is " + this.price);
        if(this.addition1Name != null){
            hamburgerPrice += this.addition1Amount;
            System.out.println("Added "+ this.addition1Name + " for an extra "+ this.addition1Amount);
        }
        if(this.addition2Name != null){
            hamburgerPrice += this.addition2Amount;
            System.out.println("Added "+ this.addition2Name + " for an extra "+ this.addition2Amount);
        }
        if(this.addition3Name != null){
            hamburgerPrice += this.addition3Amount;
            System.out.println("Added "+ this.addition3Name + " for an extra "+ this.addition3Amount);
        }
        if(this.addition4Name != null){
            hamburgerPrice += this.addition4Amount;
            System.out.println("Added "+ this.addition4Name + " for an extra "+ this.addition4Amount);
        }
        return hamburgerPrice;
    }
}
