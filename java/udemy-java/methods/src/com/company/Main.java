package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here
//        boolean gameOver = true;
//        int score = 800;
//        int levelCompleted = 5;
//        int bonus = 100;
//
//        int highScore = calculateScore(gameOver, score, levelCompleted, bonus);
//
//        score = 10_000;
//        levelCompleted = 8;
//        bonus = 200;
//
//        calculateScore(gameOver, score, levelCompleted, bonus);

        displayHighScorePosition("Tim", calculateHighScorePosition(1500));
        displayHighScorePosition("John", calculateHighScorePosition(900));
        displayHighScorePosition("Wendy", calculateHighScorePosition(400));
        displayHighScorePosition("Wendy", calculateHighScorePosition(50));
    }

    public static int calculateScore(boolean gameOver, int score, int levelCompleted, int bonus){
        if(gameOver){
            int finalScore = score + (levelCompleted * bonus);
            finalScore += 2_000;
            return finalScore;
        }
        else{
            return -1;
        }
    }

    public static void displayHighScorePosition(String playerName, int highScorePosition ){
        System.out.println(playerName + " managed to get into position " + highScorePosition + " on the high score table.");
    }

    public static int calculateHighScorePosition(int playerScore){
        if( playerScore >= 1000) {
            playerScore = 1;
        }else if(playerScore < 1_000 && playerScore >= 500){
            playerScore = 2;
        }else if( playerScore >= 100 && playerScore < 500){
            playerScore = 3;
        }else{
            playerScore = 4;
        }
        return playerScore;
    }
}
