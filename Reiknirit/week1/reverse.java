import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class reverse {
  public static void main(String[] args) {
    int n, j, temp;

    Scanner scanner = new Scanner(System.in);
    n = scanner.nextInt();
    List<Integer> items = new ArrayList<>();

    for(int i = 0; i < n; i++){
      int b = scanner.nextInt();
      items.add(b);
    }

    for(int i = 0; i < n/2; i++){
      j = items.size() - i - 1; 

      temp = items.get(i);
      items.set(i, items.get(j));
      items.set(j, temp);
    }

    for(int i = 0; i < items.size(); i++){
      System.out.println(items.get(i));
    }

    scanner.close();
  }
}