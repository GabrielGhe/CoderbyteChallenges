package coderbyte;
import java.util.Scanner;

public class easy_DashInsert {

	public static String function(int input){
		//initialize variables
		StringBuilder s = new StringBuilder();
		boolean first = false, second = false;
		
		while(input != 0){ //go through the integer backwards creating the string
			int temp = input % 10;  //cache first digit
			input = input / 10;		//remove first digit
			second = (temp % 2 != 0);//find out if temp is odd
			
			if(first && second) s.insert(0, "-");
			first = second;
			s.insert(0, temp);
		}
		return s.toString();
	}
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println( function( scan.nextInt() ) );
	}
}
