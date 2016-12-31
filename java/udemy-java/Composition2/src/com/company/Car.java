package com.company;

/**
 * Created by awsaavedra on 12/18/16.
 */
public class Car extends Vehicle{
    private int doors;
    private int engineCapacity;

    public Car(String name, int doors, int engineCapacity){
        super(name);
        this.doors = doors;
        this.engineCapacity = engineCapacity;
    }
}
