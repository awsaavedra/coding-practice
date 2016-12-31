package com.company;

public class Main {

    public static void main(String[] args) {
	    // write your code here

        System.out.println(calculateScore(true, 800, 5, 100));
        System.out.println(calculateScore(true, 10_000, 8, 200));
    }

    public static int calculateScore(boolean gameOver, int score, int levelCompleted, int bonus){
        if(gameOver){
            int finalScore = score + (levelCompleted * bonus);
            finalScore += 1000;
            return finalScore;
        }else {
            return -1;
        }
    }
}
