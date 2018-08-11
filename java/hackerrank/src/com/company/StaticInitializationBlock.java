package com.company;

import java.util.Scanner;

public class StaticInitializationBlock {

    public static void main(String[] args) {
        static boolean flag = false;
        static int breadth = 0;
        static int heighth = 0;

        static{
            Scanner scanner = new Scanner(System.in);
            breadth = scanner.nextInt();
            heighth = scanner.nextInt();

            if(breadth, heighth > 0) {
                flag = true;
            }else{
                System.out.println();
            }
        }

    }
}
