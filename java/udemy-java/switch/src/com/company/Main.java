package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here

        int switchVal= 2;

        switch(switchVal){ //testing only the switchVal here
            case 1:
                System.out.println("Value was 1");
                break; //without a break, get unpredictable results

            case 2:
                System.out.println("Val was 2");
                break;

            case 3:case 4:case 5:
                System.out.println("Was a 3, or a 4, or a 5");
                System.out.println("Actually it was a..." + switchVal);
                break;

            default:
                System.out.println("val was something else");
                break;
        }

        //More code here

        char charVal = 'A';

        switch(charVal){
            case 'A':
                System.out.println("Test");
                break;
            case 'B':
                System.out.println("B");
                break;
            case 'C':
                System.out.println("C");
                break;
            case 'D':case 'E':
                System.out.println(charVal + " was found");
                break;
            default:
                System.out.println("not found :(");
        }

        String month = "JANUARY";
        switch(month.toLowerCase()){
            case "january":
                System.out.println("Jan");
                break;
            case "june":
                System.out.println("June");
                break;
            default:
                System.out.println("Not sure...");
        }
    }
}
