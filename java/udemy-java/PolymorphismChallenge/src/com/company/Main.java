package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Car car = new Car(8, "Base car");
        System.out.println(car.startEngine());
        System.out.println(car.accelerate());
        System.out.println(car.brake());

        Mitsubishi car2 = new Mitsubishi(8, "Mitsubishi car");
        System.out.println(car2.startEngine());
        System.out.println(car2.accelerate());
        System.out.println(car2.brake());

        Holden holdUp = new Holden(5,"Commodor Holden");
        System.out.println(holdUp.startEngine());
        System.out.println(holdUp.accelerate());
        System.out.println(holdUp.brake());
    }

}

class Holden extends Car{
    public Holden(int cylinders, String nameOfCar) {
        super(cylinders, nameOfCar);
    }

    //Non-hard coded way, different from the other classes
    @Override
    public String startEngine() {
        return getClass().getSimpleName() + " -> startEngine()";
    }

    @Override
    public String accelerate() {
        return getClass().getSimpleName() + " -> accelerate()";
    }

    @Override
    public String brake() {
        return getClass().getSimpleName() + " -> break()";
    }
}

class Car{
    private int wheels;
    private boolean engine;
    private int cylinders;
    private String nameOfCar;

    public Car(int cylinders, String nameOfCar) {
        this.cylinders = cylinders;
        this.nameOfCar = nameOfCar;
        this.wheels = 4;
        this.engine = true;
    }

    public int getCylinders() {
        return cylinders;
    }

    public String getNameOfCar() {
        return nameOfCar;
    }

    public String startEngine(){
        return "Car -> startEngine()";
    }

    public String accelerate(){
        return "Car -> accelerate()";
    }

    public String brake(){
        return "Car - > Break()";
    }
}

class Mitsubishi extends Car{
    public Mitsubishi(int cylinders, String nameOfCar) {
        super(cylinders, nameOfCar);
    }

    @Override
    public String startEngine() {
        return "Mitsubishi -> startEngine()";
    }

    @Override
    public String accelerate() {
        return "Mitsubishi -> accelerate()";
    }

    @Override
    public String brake() {
        return "Mitsubishi -> break()";
    }
}

class Ford extends Car{
    public Ford(int cylinders, String nameOfCar) {
        super(cylinders, nameOfCar);
    }

    @Override
    public String startEngine() {
        return "Ford -> startEngine()";
    }

    @Override
    public String accelerate() {
        return "Ford -> accelerate()";
    }

    @Override
    public String brake() {
        return "Ford -> break()";
    }
}

class Camry extends Car{
    public Camry(int cylinders, String nameOfCar) {
        super(cylinders, nameOfCar);
    }

    @Override
    public String startEngine() {
        return "Camry -> startEngine()";
    }

    @Override
    public String accelerate() {
        return "Camry -> accelerate()";
    }

    @Override
    public String brake() {
        return "Camry -> break()";
    }
}

