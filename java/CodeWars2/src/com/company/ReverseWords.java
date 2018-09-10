package com.company;

import java.util.ArrayList;

public class ReverseWords {
    public static String reverseWords(final String original)
    {
        if( original == null || original.length() < 1){
            return "";
        }else{
            String[] words = original.split(" ");

            String reverseString = "";

            for (int i = 0; i < words.length; i++)
            {
                String word = words[i];

                String reverseWord = "";

                for (int k = word.length() - 1; k >= 0; k--)
                {
                    reverseWord = reverseWord + word.charAt(k);
                }

                reverseString = reverseString + " " + reverseWord ;

            }
            return reverseString;
        }
    }
}
