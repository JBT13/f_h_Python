import java.util.Scanner;
public class sith {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        Integer a = scanner.nextInt();
        Integer b = scanner.nextInt();
        Integer sum = scanner.nextInt();
        Integer abs = Math.abs(a-b);
        Integer real = a - b;
        
        if (real == abs){
            System.out.println("VEIT EKKI");
        }

        else if (sum > 0){
            System.out.println("JEDI");
        }

    }   
}
