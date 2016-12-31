package com.company;

/**
 * Created by awsaavedra on 12/11/16.
 */
public class Car {
    //state component, aka characteristics
    //private variables means no class besides Car class can access this
    private int doors;
    private int wheels;
    private String model;
    private String engine;
    private String color;

    //setters
    public void setModel(String model){
        String validModel = model.toLowerCase();
        if(validModel.equals("carrera") || validModel.equals("commodore")){
            this.model = model; //updating model using a method, instead of accessing it (model)
            //directly, encapsulation
        }else{
            this.model = "Unknown";
        }
    }
    //getters
    public String getModel(){
        return this.model;
    }

    /*
        Purpose of getters and setters (data encapsulation):
            useful b.c validation
            key idea: the code CANNOT create invalid objects,
                AKA objects that are created are valid and correct
    * */
}
