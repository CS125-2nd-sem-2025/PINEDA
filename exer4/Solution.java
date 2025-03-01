public class Solution {
    public static void main(String[] args) {
        // Test cases
        System.out.println(solution(5, 5) == 25); // true
        System.out.println(solution(10, 5) == 50); // true
        System.out.println(solution(15, 12) == 180); // true
    }

    public static int solution(int a, int b) {
        if (b == 0) return 0;
        if (b % 2 == 0) {
            return solution(a << 1, b >> 1);
        } else {
            return a + solution(a, b - 1);
        }
    }
}
