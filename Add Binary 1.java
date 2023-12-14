Add Binary 1
Given two binary strings a and b, return their sum as a binary string.

Input Format
First line string s1
Second line string s2
  
Constraints
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
  
Output Format
addition of the strings
  
Sample Input 0
11
1
  
Sample Output 0
100
  
Sample Input 1
1010
1011
  
Sample Output 1
10101

Java Code:

import java.util.Scanner;
public class BinaryAddition {
    public static String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder();
        int carry = 0;
        int i = a.length() - 1;
        int j = b.length() - 1;
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (i >= 0) {
                sum += a.charAt(i--) - '0';
            }
            if (j >= 0) {
                sum += b.charAt(j--) - '0';
            }
            result.insert(0, sum % 2);
            carry = sum / 2;
        }
        if (carry > 0) {
            result.insert(0, carry);
        }
        return result.toString();
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s1 = scanner.nextLine();
        String s2 = scanner.nextLine();
        String sum = addBinary(s1, s2);
        System.out.println(sum);
    }
}
