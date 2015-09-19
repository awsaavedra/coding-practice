/*
Alexander Saavedra
Github: awsaavedra
Problem:
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
*/

public class Solution {
    public int climbStairs(int n) {
        int a = 0;
        int b = 1;
        int c = 2;
        if( n == 0)
            return 0;
        if( n == 1)
            return 1;
        if( n == 2)
            return 2;
        for( int i = 3; i <= n; i++){
            a = b;
            b = c;
            c= c+a;
        }
        return c;
    }
}
