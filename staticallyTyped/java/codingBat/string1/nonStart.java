/*
Given 2 strings, return their concatenation, except 
omit the first char of each. The strings will be at least length 1. 
*/

public class nonStart{
	public static void main(String[] args){
		System.out.println(nonStart("Hello", "There"));
	}
	
	public static String nonStart(String a, String b){
		String aNew = a.substring(1,a.length());
		String bNew = b.substring(1,b.length());
		return aNew + bNew;
	}
}
