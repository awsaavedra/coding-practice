package com.company;

import java.lang.Math;

public class NextSquare {
    public static long findNextSquare(long sq) {
//        double squareRootOfInput =  Math.sqrt(sq);
//
//        if( Math.floor(squareRootOfInput) == squareRootOfInput){
//            double nextSquareRoot = squareRootOfInput + 1;
//            long nextSquare = (long) Math.pow(nextSquareRoot, 2);
//            return nextSquare;
//        }else{
//            return -1;
//        }
        long root = (long) Math.sqrt(sq);
        return root * root == sq ? (root + 1) * (root + 1) : -1;
    }
}
