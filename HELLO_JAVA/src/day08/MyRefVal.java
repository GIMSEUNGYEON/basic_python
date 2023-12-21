package day08;

public class MyRefVal {
	public static void main(String[] args) {
		int a = 1;
		int [] arr = {2};
		
		System.out.println("a : " + a);
		System.out.println("arr : " + arr[0]);

		change(a);
		change(arr);
		
		System.out.println("a : " + a); //value값이므로 변수에 저장된 값이 변경되지 않음
		System.out.println("arr : " + arr[0]); //reference값이므로 해당 배열의 0번째 자리가 변경된 것으로 간주함
	}
	
	static void change(int a) {
		a = 3;
	}
	static void change(int [] arr) {
		arr[0] = 4;
	}
}
