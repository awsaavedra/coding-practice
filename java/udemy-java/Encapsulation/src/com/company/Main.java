package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here
        //stopping outsiders (classes or code outside) from accessing
//        //data within a class

//        Player player = new Player(); //default constructor
//        player.name = "Tim";
//        player.health = 20;
//        player.weapon = "Sword";
//
//        int damage = 10;
//        player.loseHealth(damage);
//        System.out.println("Remaining health = " + player.healthRemaining());
//
//        damage = 11;
//        player.health = 200; //taking control out of player class...able to change fields directly
//        player.loseHealth(damage);
//        System.out.println("Remaining health = " + player.healthRemaining());

        EnhancedPlayer player2 = new EnhancedPlayer("Tim", 200, "Sword");
        System.out.println("Initial health is " + player2.getHealth());
    }
}
