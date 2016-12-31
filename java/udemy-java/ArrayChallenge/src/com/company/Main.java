package com.company;
import java.util.Scanner;

public class Main {

    private static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
	// write your code here
        //Create a program using arrays that sorts a list of integers in descending order
        //methods: getIntegers, printArray, and sortIntegers
        int[] myIntegers = getIntegers(5);

        printArray(myIntegers);

        //sorting the integers
        sortIntegers(myIntegers);
        printArray(myIntegers);
    }

    public static int[] getIntegers(int number){
        int[] values = new int[number];
        System.out.println("Please type 5 integers");
        for(int i = 0; i < values.length; i++){
            values[i] = scanner.nextInt();
        }
        return values;
    }

    public static void printArray(int[] array){
        System.out.print("Array = "1);
        for(int i = 0; i < array.length; i++){
            System.out.print(" " + array[i]);
        }
        System.out.println("\n");
    }

    public static void sortIntegers(int[] unsortedArray){
        //bubbleSort, O(n^2) time complexity, O(0) time commitment
        for (int i = 0; i < unsortedArray.length; i++) {
            for (int j = i + 1; j < unsortedArray.length; j++) {
                int tmp = 0;
                if (unsortedArray[i] < unsortedArray[j]) {
                    tmp = unsortedArray[i];
                    unsortedArray[i] = unsortedArray[j];
                    unsortedArray[j] = tmp;
                }
            }
        }
    }
}
