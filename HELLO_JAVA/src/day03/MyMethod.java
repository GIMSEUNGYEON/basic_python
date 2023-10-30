package day03;

public class MyMethod {
	public static void main(String[] args) {
		
		MyMethod mm = new MyMethod();
		
		System.out.println("sum : " + mm.add(4, 2));
		System.out.println("min : " + mm.minus(4, 2));
		System.out.println("mul : " + mm.multiply(4, 2));
		System.out.println("div : " + mm.divide(4, 2));
	}

	public int add(int a, int b) {
		return a + b;
	}

	public int minus(int a, int b) {
		return a - b;
	}

	public int multiply(int a, int b) {
		return a * b;
	}

	public int divide(int a, int b) {
		return a / b;
	}

}
