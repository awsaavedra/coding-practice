package com.company;

/**
 * Created by awsaavedra on 12/19/16.
 */
public class roomHeater {
    private String temperature;

    public roomHeater(String temperature) {
        this.temperature = temperature;
    }

    public void heaterOn(){
        System.out.println("Room is heated to : " + temperature);
    }
}
