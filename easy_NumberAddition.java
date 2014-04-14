import java.util.Scanner;

public class Easy_NumberAddition {

	public static int function(String input){
		char[] charInput = input.toCharArray(); //make string into char array
		String temp = "0";
		int result = 0;
		for(char x : charInput){
			if(Character.isDigit(x)){
				temp += x; //if character is digit save it
			} else {
				result += Integer.parseInt(temp);
				temp = "0"; //if it's not a digit, add saved digits to result
			}
		}
		if(temp != ""){
			result += Integer.parseInt(temp); //the last character could be a digit
		}
		return result;
	}
	
	public static void main(String[] args) {
		System.out.println( function( new Scanner(System.in).nextLine() ) );
	}
}
