public class conditionals{
	public static void main(String[] args){
		System.out.println("All conditionals: &&, ||, ==, !=, <, >, >=, <=");
		
		//using if else statements in java
		int a = 11;
		int b = 50;
		if(a == b){
			System.out.println("a and b are equal");
		}
		else{
			System.out.println("a and b are not equal");
		}
		
		System.out.println("----------------------== vs .equals()------------------------");

	  String c = new String("Wow");
		String d  = new String("Wow");
		String sameC = c;

		boolean r1 = c == d;      // This is false, since a and b are not the same object
		boolean r2 = c.equals(d); // This is true, since a and b are logically equals
		boolean r3 = c == sameC;  // This is true, since a and sameA are really the same object	
		System.out.println(r1);
		System.out.println(r2);
		System.out.println(r3);
	}
}
