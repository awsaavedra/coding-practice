public class arrays{
	public static void main(String[] args){
		int[] arr = new int[10]; //created an array of length 10
		System.out.println(arr.length); //print the lengthof the array

    //accessing the array and setting values
		System.out.println("-----------------accessing the arrays syntax ------");
		for( int i =0; i < arr.length; i++){
			arr[i] = i+1;
			System.out.println("Array index: " + i + " Array element val: " + arr[i]);
		}
	}
}
