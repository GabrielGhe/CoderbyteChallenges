import java.util.Arrays;

public class Easy_SecondGreatLow {

	public static String function(int[] input){
		String result = "";
		if(input.length > 3){
			Arrays.sort(input);
			result = String.format("%s %s", input[1], input[input.length - 2] );
		}
		return result;
	}
	
	public static void main(String[] args) {
		System.out.println( function( new int[]{1,6,3,7,8,2,7,9,34,345,543} ) );
	}
}
