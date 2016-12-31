package com.company;

public class Main {

    public static void main(String[] args) {
        Car porsche = new Car(); //initialized a new object of type car
        Car holden = new Car();

        porsche.setModel("Carrera");

        System.out.println("Model is " + porsche.getModel());

        //don't forget, all objects inherit from the base java
        //class giving you a lot of methods
        //KEYWORDS: instantiation, encapsulation, class, inheritance, state
        //KEYWORDS 2: methods, static classes
        //null is the internal default state for a class AND string (which is a class)
            //string bends the rules b.c string is a class w/n a class
    }
}
