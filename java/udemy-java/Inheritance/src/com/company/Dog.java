package com.company;

/**
 * Created by awsaavedra on 12/18/16.
 */
public class Dog extends Animal{

    private int eyes;
    private int legs;
    private int tail;
    private int teeth;
    private String coat;


    //constructor from superClass animal
    public Dog(String name, int size, int weight, int eyes, int legs,
               int tail, int teeth, String coat) {
        super(name, 1, 1, size, weight); //calls constructor we are extending from
        this.eyes = eyes;
        this.legs = legs;
        this.tail = tail;
        this.teeth = teeth;
        this.coat = coat;
    }

    private void chew(){
        System.out.println("Dog.chew() called");
    }

    @Override
    public void eat() {
        System.out.println("Dog.eat() called");
        chew();
        super.eat();
    }
    public void walk(){
        System.out.println("Dog.walk() called");
        super.move(5);
    }
    public void run(){
        System.out.println("Dog.run() called");
        move(10);
    }

    private void moveLegs(int speed){
        System.out.println("Dog.moveLegs() called");
    }

    @Override
    public void move(int speed){
        System.out.println("Dog.move() called");
        moveLegs(speed);
        super.move(speed);
    }
}
