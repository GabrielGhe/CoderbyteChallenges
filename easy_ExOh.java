package coderbyte;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Easy_ExOh {
	
	public static boolean function(String input){
		Map<String, Integer> map = new HashMap<String, Integer>();
		map.put("x", 0);
		map.put("o", 0);
		for(char val : input.toCharArray()){
			String x = String.valueOf(val).toLowerCase();
			map.put(x, map.get(x) + 1);
		}
		return map.get("x") == map.get("o");
	}

	public static void main(String[] args) {
		System.out.println( function( new Scanner(System.in).nextLine() ) );
	}

}
