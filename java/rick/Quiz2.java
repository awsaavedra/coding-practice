public class Quiz2
{
	 private int a; // Line 3
	 public void method1( int x ){
			 int a; // Line 7
			 int b = x;
			 a = b / 5;
			 this.a = b % 5;
			 System.out.println( "a = " + a );
			 System.out.println( "b = " + b );
			 System.out.println( "this.a = " + this.a );
			 System.out.println( "x = " + x );
			 System.out.println( "method2() result = " + method2( x ) );
			 System.out.println( "a = " + a );
			 System.out.println( "b = " + b );
			 System.out.println( "this.a = " + this.a );
			 System.out.println( "x = " + x );
	}
	public int method2( int x ){
			 int a = x;
			 int b = this.a;
			 x = 99;
			 System.out.println( "a = " + a );
			 System.out.println( "b = " + b );
			 System.out.println( "this.a = " + this.a );
			 System.out.println( "x = " + x );
			 this.a = 37;
			 b = b * 3;
			 return a - 3;
	}
	public static void main(String[] args){
			Quiz2 q2 = new Quiz2();
			q2.method1( 13 );
	}
} 
