/*
Given a string, return a new string made of 3 copies of the last 2 chars of 
the original string. The string length will be at least 2. 
*/

public class extraEnd{
	public static void main(String[] args){
		System.out.println(extraEnd("Hello"));
	}

	public static String extraEnd(String str){
		int l = str.length();
		String output = str.substring(l-2,l);
		return output+output+output;
	}
}
