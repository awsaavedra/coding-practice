package com.company;

import java.util.ArrayList;

/**
 * Created by awsaavedra on 12/31/16.
 */
public class GroceryList {
    private ArrayList<String> groceryList = new ArrayList<String>();
    private int[] myNumbers = new int[50];


    public void addGroceryItem(String item){
        groceryList.add(item);
    }

    public void printGroceryList(){
        System.out.println("You have " + groceryList.size() +  " items in your grocery list");
        for(int i = 0; i <groceryList.size(); i++){
            System.out.println(i + 1 + ", " + groceryList.get(i));
        }
    }

    public void modifyGroceryItem(int position, String newItem){
        groceryList.set(position);
        System.out.println("Grocery item " + (position + 1) + " has been modified.");
    }

    public void removeGroceryItem(int position){
        String theItem = groceryList.get(position);
        groceryList.remove(position);
        //milk, cheese, bread
    }
}
