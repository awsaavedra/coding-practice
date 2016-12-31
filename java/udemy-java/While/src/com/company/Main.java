package com.company;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
	// write your code here
//        int count = 6;
//        do{
//            System.out.println("Count val : " + count);
//            count++;
//            if( count > 100){
//                break;
//            }
//        }while( count != 6);
        int number = 5;
        //answered a more interesting question...
        ArrayList<Integer> evenNums = new ArrayList<Integer>();
        int finishNumber = 20;
        while( number <= finishNumber && evenNums.size() < 5){
            if(!isEvenNumber(number)){
                number++;
                continue;
            }
            if(isEvenNumber(number)){
                evenNums.add(number);
            }

            System.out.println("Even number " + number);
            number++;
        }
        System.out.println("first five even numbers..." + evenNums);
    }
    public static boolean isEvenNumber(int num){
        if( num % 2 == 0){
            return true;
        }else{
            return false;
        }
    }
}
