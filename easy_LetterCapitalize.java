import java.util.Scanner;

public class Easy_LetterCapitalize {

	public static String function(String input){
		String[] words = input.split(" "); 		//split into words
		StringBuilder result = new StringBuilder(); 	//StringBuilder > String
		for(String w : words){
			String temp = w.toUpperCase(); 		//Make whole word uppercase
			result.append(temp.charAt(0) + w.substring(1) + " ");
		}
		return result.deleteCharAt(result.length() - 1).toString(); // removing the last " "
	}
	
	public static void main(String[] args) {
		System.out.println(function(new Scanner(System.in).nextLine()));//one line input + function
	}
}
