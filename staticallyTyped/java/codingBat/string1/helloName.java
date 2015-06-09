/*
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!"
*/

public class helloName{
	public static void main(String[] args){
		System.out.println(helloName("steve"));
	}
	
	public static String helloName(String s){
		return "Hello " + s + "!";
	}
}
