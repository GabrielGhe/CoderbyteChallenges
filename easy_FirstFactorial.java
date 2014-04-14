import java.util.Scanner;

public class Easy_FirstFactorial {

	public static int function(int input){
		int result = 1;
		for(int x = 1; x != (input + 1); ++x){
			result *= x;
		}
		return result;
	}
	
	public static void main(String[] args) {
		System.out.println(function(new Scanner(System.in).nextInt()));
	}
}
