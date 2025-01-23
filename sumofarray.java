import java.util.Scanner;

public class ArraySum {

    public static void main(String[] args) // sum of arrays in java 
	{
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int sum = 0;
	//iterating through the array and adding them to the sum and then printing it
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            sum += arr[i];
        }
        System.out.println(sum);
    }
}
