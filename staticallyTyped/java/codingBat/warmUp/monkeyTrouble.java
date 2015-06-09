/*
We have two monkeys, a and b, and the parameters aSmile and 
bSmile indicate if each is smiling. We are in trouble if they are both 
smiling or if neither of them is smiling. Return true if we are in trouble. 
*/

public class monkeyTrouble{
	public static void main(String[] args){
		System.out.println(monkeyTrouble(true,true));		
	}
	public static boolean monkeyTrouble( boolean aSmile, boolean bSmile){
		if( aSmile == true && bSmile == true){
			return true;
		}else if( aSmile != true && bSmile != true){
			return true;
		}else{
			return false;
		}
	}
}
