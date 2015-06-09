/*
The parameter weekday is true if it is a weekday, and the parameter vacation 
is true if we are on vacation. We sleep in if it is not a weekday or 
we're on vacation. Return true if we sleep in. 
*/
public class sleepIn{
	public static void main(String[] args){
		System.out.println(sleepTest(false, false));
		System.out.println(sleepTest(true, false));
		System.out.println(sleepTest(false,true));	
	}

	public static boolean sleepTest(boolean weekday, boolean vacation){
		if( weekday == false || vacation == true){
			return true;
		}else{
			return false;
		}
	}
}
