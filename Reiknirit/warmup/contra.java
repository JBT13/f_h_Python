import java.util.Scanner;

public class contra {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    String s = scanner.nextLine();

    if (s.equals("a")){
      System.out.println("b");
    }
    else{
      System.out.println("a");
    }
    scanner.close();
  }
}