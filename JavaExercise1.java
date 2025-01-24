import java.util.Random;
// so we import the java module and then add it
public class RandomSum {
    public static void main(String[] args) {
        Random random = new Random();
        int a = random.nextInt(100) + 1;
        int b = random.nextInt(100) + 1;
        System.out.println(a + b);
    }
}