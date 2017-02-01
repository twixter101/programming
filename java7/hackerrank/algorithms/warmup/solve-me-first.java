import java.util.Scanner;

public class Solution {
    static int addTwoInt(int a, int b) {
        return a + b;
    }
    
    public static void main(String[] args) throws java.io.IOException {
        int _a, _b, _total;
        Scanner in = new Scanner(System.in);
        
        _a = in.nextInt();
        _b = in.nextInt();
        _total = addTwoInt(_a, _b);
        System.out.print(_total);
        in.close();
    }
}