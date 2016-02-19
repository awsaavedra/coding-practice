/*
Given a string, return true if the first 2 chars in the 
string also appear at the end of the string, such as with "edited". 
*/

public class frontAgain{
	public static void main(String[] args){
		System.out.println(frontAgain("edited"));
	}
	
	public static boolean frontAgain(String str){
		if( str.length() <= 1)
			return false;
		String start = str.substring(0,2);
		int l = str.length();
		String end = str.substring(l-2,l);
		if( start.equals(end))
			return true;
		else{
			return false;
		}
	}
}
