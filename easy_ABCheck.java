package easy_ABCheck;

import java.util.Scanner;
import java.util.regex.Pattern;

public class easy_ABCheck {
	
	public static boolean method(String input){
		return Pattern.matches("(a.{3}b)|(b.{3}a)", input);
	}

	public static void main(String[] args) {
		System.out.println( method( new Scanner(System.in).nextLine() ) );
	}
}
