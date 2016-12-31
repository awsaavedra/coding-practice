package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here
        calcFeetAndInchesToCentimeters(100);
    }


    public static double calcFeetAndInchesToCentimeters(double feet, double inches){
        if( feet >= 0 && (inches >= 0 && inches <= 12)){
            double feetToCm = feet * 12 * 2.54;
            double inchesToCm = inches * 2.54;
            return inchesToCm + feetToCm;
        }else{
            return -1.0;
        }
    }

    public static double calcFeetAndInchesToCentimeters(double inches){
        if(inches >= 0.0){
            double cm = 0.0;

            double feet = (int)inches /12;
            double remainingInches = (int) inches % 12;
            System.out.println(inches + " inches is equal to " + feet +  " feet and " + remainingInches + " inches" );
            return calcFeetAndInchesToCentimeters(feet, remainingInches);
        }else {
            return -1.0;
        }
    }
}

