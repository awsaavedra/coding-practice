package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here

        for( int i = 2; i <= 8; i++){
            System.out.println("$10,000 at %" + i + " interest "  + calculateInterest(10_000.0, i));
        }
        System.out.println("/////////////////////////////////////");
        for( int i = 8; i >= 2; i--){
            System.out.println("$10,000 at %" + i + " interest "  + calculateInterest(10_000.0, i));
        }

        System.out.println("/////////////////////////////////////");
        int numOfPrimes = 0;
        for(int i = 10; i < 50; i++){
            if( isPrime(i) == true){
                numOfPrimes += 1;
                System.out.println( i + " is a prime number");
            }
            if(numOfPrimes == 3){
                break;
            }

        }
        System.out.println("number of primes " + numOfPrimes );

    }

    public static boolean isPrime(int n){
        if( n == 1){
            return false;
        }
        for(int i = 2; i <= n/2; i++){
            if( n % i == 0){
                return false;
            }
        }
        return true;
    }

    public static double calculateInterest(double amount, double interestRate){
        return (amount * interestRate) / 100;
    }
}
