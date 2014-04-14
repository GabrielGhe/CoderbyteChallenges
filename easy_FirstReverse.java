import java.util.Scanner;

public class Easy_FirstReverse {

	public static void main(String[] args) {
		String input = new Scanner(System.in).nextLine();
		input = new StringBuilder(input).reverse().toString();
		System.out.println(input);
	}
}
