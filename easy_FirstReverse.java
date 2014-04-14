import java.util.Scanner;

public class Easy_FirstReverse {
	// all of this can be done on 1 line;however, it looks too complicated and cluttered
	public static void main(String[] args) {
		String input = new Scanner(System.in).nextLine();
		input = new StringBuilder(input).reverse().toString();
		System.out.println(input);
	}
}
