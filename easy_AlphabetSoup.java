package coderbyte;

import java.util.Arrays;
import java.util.Scanner;

public class easy_AlphabetSoup {
	
	public static String function(String input){
		char[] sorted = input.toCharArray();
		Arrays.sort(sorted);
		return String.valueOf(sorted);
	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println( function(scan.nextLine() ) );
	}
}
