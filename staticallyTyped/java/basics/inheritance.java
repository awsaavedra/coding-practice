/*
superclass
	-subclass, which inherits all members(???) from the superclass
	-The inherited fields can be used directly, just like any other fields (???)
	-note: A subclass does not inherit the private members of its parent class
	

	-methods inherited from the superclass can be overriden when you create a new
		instance of that method in the subclass

	REMEMBER: you can create new methods in the subclass that weren't in the 
		superclass, i.e. ducks can quack, but the superclass animal doesn't have a
			quack method
	
	Example of proper OOD inheritance:
		Superclass: Shape
			subclass: triangle
				instances of triangle (types of rectangle): equilateral, scalene, etc.
http://2.bp.blogspot.com/-67wc4x1iV5Y/VD_1AedRshI/AAAAAAAADCs/adoz5yB7mJQ/s1600/Polygon%2BFamily%2BTree.png

Java specific keywords: extends (inherits from) and implements (interface of)
*/

class Shape {
    public double area ()
    {
        return 0;     // Since this is just a generic "Shape" we will assume the area as zero.
                    // The actual area of a shape must be overridden by a subclass, as we see below.
                    // You will learn later that there is a way to force a subclass to override a method,
                    // but for this simple example we will ignore that.
    }
}

class Circle extends Shape {                    // class declaration
    Circle (double diameter) {                  // constructor
        this.diameter = diameter;
    }
    private static final double PI = Math.PI;   // constant
    private double diameter;                    // instance variable
    
    public double area () {                     // dynamic method
        double radius = diameter / 2.0;
        return PI * radius * radius;
    }

}

class Rectangle extends Shape {
		Rectangle(double length, double width){
			this.length = length;
			this.width = width;
		}
		private double length; //???
		private double width;

		public double area(){
				return length*width;
		}
}

public class inheritance{
    public static void main(String[] args) {
        Shape s1 = new Circle (2.5);
        Shape s2 = new Rectangle (5.0, 4.0);
        
        System.out.println (s1.area());
        System.out.println (s2.area());
    }
}
