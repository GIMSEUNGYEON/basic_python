package day05;

public class MySplit {
	public static void main(String[] args) {
		String str = "3,4";
		
		String []strarr = str.split(",");
		
		int i = Integer.parseInt(strarr[0]);
		int ii = Integer.parseInt(strarr[1]);
	}
}
