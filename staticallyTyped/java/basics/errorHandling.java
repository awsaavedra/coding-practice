
//

public class errorHandling {
    public static void main(String[] args) {
        try{
					int[] arr = new int[10];
					System.out.println(arr[9001]);
				}catch(ArrayIndexOutOfBoundsException ex){
					System.out.println("array is out of bounds");
				}
		}
}
