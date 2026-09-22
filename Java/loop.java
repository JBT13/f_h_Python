public class loop {
    public static int loops(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += 3;
            for (int j = 1; j <= n; j++) {
                sum += 2;
                for (int k = 1; k <= n; k++) {
                    sum += 1;
                }
            }
        }
        return sum;
    }

    
    public static void main(String[] args){
        int sum = loops(10);
        System.out.println(sum);
    }
}

