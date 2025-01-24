import java.util.Scanner;
// add 3 numbers by inputting them by scanners and add them
public class SumThreeNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        System.out.println(a + b + c);
    }
}

