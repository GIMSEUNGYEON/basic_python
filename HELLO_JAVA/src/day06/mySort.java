package day06;

import java.util.Arrays;

public class mySort {
	public static void main(String[] args) {
        int[] lotto = new int[6];

        for (int i = 0; i < lotto.length; i++) {
            int num = (int) (Math.random() * 45) + 1;
            lotto[i] = num;
            for (int j = 0; j < i; j++) {
                if (lotto[i] == lotto[j]) {
                    i--;
                    break;
                }
            }            
        }
        System.out.println("원래 배열");
        System.out.println(Arrays.toString(lotto));

        
        
        for(int i = 0; i < lotto.length; i++) {
        	for(int j = 0; j < i; j++) {
        		if(lotto[i] < lotto[j]) {
        			int tmp = lotto[i];
        			lotto[i] = lotto[j];
        			lotto[j] = tmp;
        		}
        	}
        }
        System.out.println("정렬 배열");
        System.out.println(Arrays.toString(lotto));
        
	}
}
