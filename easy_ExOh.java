package coderbyte;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Easy_ExOh {
	
	public static boolean function(String input){
		Map<String, Integer> map = new HashMap<String, Integer>();
		map.put("x", 0);//set initial values inside hashmap
		map.put("o", 0);
		for(char val : input.toCharArray()){//iterate through the string
			String x = String.valueOf(val).toLowerCase(); //converting each character to lower case
			map.put(x, map.get(x) + 1);//and incrementing its value inside the map
		}
		return map.get("x") == map.get("o");//find out if the x and o values are equal
	}

	public static void main(String[] args) {
		System.out.println( function( new Scanner(System.in).nextLine() ) );
	}

}
