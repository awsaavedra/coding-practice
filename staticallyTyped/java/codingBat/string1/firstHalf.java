//Given a string of even length, return the first half. 
//So the string "WooHoo" yields "Woo". 


public class firstHalf{
	public static void main(String[] args){
		System.out.println(firstHalf("WooHoo"));
		System.out.println(firstHalf("HelloThere"));
	}

	public static String firstHalf(String str){
		int l = str.length()/2;
		String half = str.substring(0,l);
		return half;	
	}
}
