package com.company;

public class Accumul {

    public static String accum(String s) {
        String[] newStr = s.split("");
        String result = s.charAt(0) + "";
        for(int i = 0; i < s.length(); i++){
            if( i > 0){
                result += "-";
                String temp = s.charAt(i) + "";
                String firstLeterUppercase = temp.toUpperCase();
                for(int k = 1; k < i; k++){
                    temp += s.charAt(i);
                }
                result += firstLeterUppercase + temp.toLowerCase();
            }
        }
        return result;
    }
}
