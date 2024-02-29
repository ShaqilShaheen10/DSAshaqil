import java.util.*;
//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        StringBuilder sb=new StringBuilder("Shaqil");
        for(int i=0;i<sb.length()/2;i++){
            int first=i;
            int last=sb.length()-1-i;
            char First=sb.charAt(first);
            char Last=sb.charAt(last);
            sb.setCharAt(first,Last);
            sb.setCharAt(last,First);
       }
        System.out.println(sb);
    }
}


import java.util.HashSet;
import java.util.Iterator;


public class Main {
    public static void main(String args[]) {
        HashSet<Integer> set = new HashSet<>();

        //Add
        set.add(1);
        set.add(2);
        set.add(3);
        set.add(1);


        //Size
        System.out.println("size of set is : " + set.size());


        //Search
        if(set.contains(1)) {
            System.out.println("present");
        }


        if(!set.contains(6)) {
            System.out.println("absent");
        }


        //Delete
        set.remove(1);
        if(!set.contains(1)) {
            System.out.println("absent");
        }


        //Print all elements
        System.out.println(set);


        //Iteration - HashSet does not have an order
        set.add(0);
        Iterator it = set.iterator();
        while (it.hasNext()) {
            System.out.print(it.next() + ", ");
        }
        System.out.println();


        //isEmpty
        if(!set.isEmpty()) {
            System.out.println("set is not empty");
        }
    }
}









import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter 1st String");
        String a=sc.nextLine();
        System.out.println("Enter 2nd String");
        String b=sc.nextLine();
        Main maininstance=new Main();
        boolean result=maininstance.isSubsequence(a,b);
        System.out.println(result?"True":"False");
    }
    public boolean isSubsequence(String a,String b){
        int m=a.length();
        int n=b.length();
        int i=0,j=0;
        while(i<m && j<n){
            if(a.charAt(i)==b.charAt(j)){
                i++;
            }
            j++;
        }
        return i==m;
    }
}





import java.util.*;
public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nums = {5,7,7,8,8,10};
        System.out.println("Enter the target:");
        int target = sc.nextInt();
        Main mainInstance = new Main();
        int[] result = mainInstance.Binary(nums, target);
        System.out.println("First and Last occurrences: " + result[0] + ", " + result[1]);
    }
    public int[] Binary(int[] nums, int target){
        int l=0,r=nums.length-1;
        int f=-1,L=-1;
        while(l<=r){
            int m=l+(r-l)/2;
            if(nums[m]==target){
                f=m;
                L=m;
                while(f>0 && nums[f-1]==target){
                    f--;
                }
                while(L<nums.length-1 && nums[L+1]==target){
                    L++;
                }break;
            }else if(nums[m]<target){
                l=m+1;
            }else{
                r=m-1;
            }
        }
        return new int[]{f,L};
    }
}



import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the no. of LEDs turnedOn:");
        int turnedOn= sc.nextInt();
        Main maininsteance=new Main();
        List<String> w=maininsteance.BinaryWatch(turnedOn);
        System.out.println(w);
    }
    public List<String> BinaryWatch(int turnedOn){
        ArrayList<String> r=new ArrayList<>();
        for(int h=0;h<12;h++){
            for(int m=0;m<60;m++){
                if(Integer.bitCount(h)+Integer.bitCount(m)==turnedOn){
                    if(m<10) r.add(String.format("%d:0%d",h,m));
                    else r.add(String.format("%d:%d",h,m));
                }
            }
        }
        return r;
    }
}



import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number:");
        int n=sc.nextInt();
        Main maininstance=new Main();
        int num=maininstance.numSquare(n);
        System.out.println("Perfect Square: "+num);
    }
    public int numSquare(int n){
        int sqrt=(int) Math.sqrt(n);
        if(sqrt*sqrt==n) return 1;
        while(n%4==0) n=n/4;
        if(n%8==7)return 4;
        for(int i=1;i*i<=n;i++){
            int s=i*i;
            int b=(int) Math.sqrt(n-s);
            if(b*b==n-s) return 2;
        }
        return 3;
    }
}


import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the pattern:");
        String pattern=sc.nextLine();
        System.out.println("Enter the word:");
        String s=sc.nextLine();
        Main maininstance=new Main();
        boolean result=maininstance.wordPattern(pattern,s);
        System.out.println("The sequence of word pattern is: "+(result?"true":"false"));
    }
    public boolean wordPattern(String pattern,String s){
        String[] word=s.split(" ");
        if(word.length!=pattern.length()) return false;
        HashMap<Character,String> map=new HashMap<>();
        for(int i=0;i<pattern.length();i++){
            char c=pattern.charAt(i);
            if(map.containsKey(c)){
                if(!map.get(c).equals(word[i])){
                    return false;
                }
            }
            else{
                if(map.containsValue(word[i])){
                    return false;
                }
                map.put(c,word[i]);
            }
        }
        return true;
    }
}


import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the dividend:");
        int dividend= sc.nextInt();
        System.out.println("Enter the divisor:");
        int divisor=sc.nextInt();
        Main m=new Main();
        int c=m.divide(dividend,divisor);
        System.out.println("The output is:\n"+c);
    }
    public int divide(int dividend,int divisor){
        if(dividend==-2147483648 && divisor==-1){
            return Integer.MAX_VALUE;
        }
        return dividend/divisor;
    }
}


import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of coins:");
        int n=sc.nextInt();
        Main m=new Main();
        int arrangeCoins=m.arrangeCoins(n);
        System.out.println("The Coins are:\n"+arrangeCoins);
    }
    public int arrangeCoins(int n){
        return (int)((Math.sqrt(1+8L*(long)n)-1)/2);
    }
}


import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the area of the rectangle:");
        int area= sc.nextInt();
        Main m=new Main();
        int[] constructRectangle=m.constructRectangle(area);
        System.out.println("The sides of the rectangle are:\n"+Arrays.toString(constructRectangle));
    }
    public int[] constructRectangle(int area){
        int i=(int)Math.sqrt(area);
        for(;i>=1;i--){
            if(area%i==0){
                return new int[]{area/i,i};
            }
        }
        return new int[]{area,1};
    }
}


import  java.util.*;

import java.util.List;

public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the numbers separated by commas:");
        String input=sc.nextLine();
        String[] numsString=input.split(",");
        int[] nums=new int[numsString.length];
        for(int i=0;i< numsString.length;i++){
            nums[i]=Integer.parseInt(numsString[i].trim());
        }
        Main m=new Main();
        List<String> a=m.summaryRanges(nums);
        System.out.println("The summary ranges are:\n"+a);
    }
    public List<String> summaryRanges(int[] nums){
        ArrayList<String> al=new ArrayList<>();
        for (int i=0;i<nums.length;i++){
            int start=nums[i];
            while(i+1<nums.length && nums[i]+1==nums[i+1]) i++;
            if(start!=nums[i]){
                al.add(""+start+"->"+nums[i]);
            }
            else{
                al.add(""+start);
            }
        }
        return al;
    }
}



import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the strings seperated by commas:");
        String input=sc.nextLine();
        String[] a=input.split(",");
        String[] w=new String[a.length];
        for(int i=0;i<a.length;i++){
            w[i]=a[i].trim();
        }
        Main m=new Main();
        String r= m.firstPalindrome(w);
        System.out.println("The first Palindrome in the given Strings is:\n"+r);
    }
    public String firstPalindrome(String[] words){
        for(String word:words){
            StringBuilder reversed=new StringBuilder(word).reverse();
            if(word.equals(reversed.toString())){
                return word;
            }
        }
        return "";
    }
}



import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number:");
        int a=sc.nextInt();
        Main m=new Main();
        List<String> w=m.FizzBuzz(a);
        System.out.println("The output is:\n"+w);
    }
    public List<String> FizzBuzz(int n){
        List<String> ans=new ArrayList<>();
        for(int i=1;i<=n;i++){
            if(i%3==0 && i%5==0){
                ans.add("FizzBuzz");
            }
            else if(i%3==0){
                ans.add("Fizz");
            }
            else if(i%5==0){
                ans.add("Buzz");
            }
            else{
                ans.add(""+i);
            }
        }
        return ans;
    }
}


import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number:");
        int a=sc.nextInt();
        Main m=new Main();
        boolean c=m.checkPerfectNum(a);
        System.out.println("The number is perfect:\n"+(c?"true":"false"));
    }
    public boolean checkPerfectNum(int num){
        int sum=0;
        if(num%2!=0){
            return false;
        }
        for(int i=1;i<=num/2;i++){
            if(num%i==0){
                sum+=i;
            }
        }
        return sum==num;
    }
}



import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the numbers separated by commas:");
        String input=sc.nextLine();
        String[] a=input.split(",");
        int[] b=new int[a.length];
        for(int i=0;i<a.length;i++){
            b[i]=Integer.parseInt(a[i].trim());
        }
        Main m=new Main();
        int[] r=m.rearrangeNums(b);
        System.out.println("The rearranged numbers are:\n"+Arrays.toString(r)) ;
    }
    public int[] rearrangeNums(int[] a){
        int n=a.length;
        int[] ans=new int[n];
        int pi=0,ni=1;
        for(int i=0;i<n;i++){
            if(a[i]>0){
                ans[pi]=a[i];
                pi+=2;
            }
            else{
                ans[ni]=a[i];
                ni+=2;
            }
        }
        return ans;
    }
}

import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the numbers separated by commas:");
        String input=sc.nextLine();
        String[] a=input.split(",");
        int[] b=new int[a.length];
        for(int i=0;i<a.length;i++){
            b[i]=Integer.parseInt(a[i].trim());
        }
        Main m=new Main();
        long r=m.largestPerimeter(b);
        System.out.println("The largest perimeter is:\n"+r);
    }
    public long largestPerimeter(int[] nums){
        long sum=0;
        Arrays.sort(nums);
        for(int num:nums){
            sum+=num;
        }
        int n=nums.length;
        for(int i=n-1;i>=2;i--){
            sum-=nums[i];
            if(sum>nums[i]){
                return sum+nums[i];
            }
        }
        return -1;
    }
}

import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the numbers separated by commas:");
        String input=sc.nextLine();
        String[] a=input.split(",");
        int[] b=new int[a.length];
        for(int i=0;i<a.length;i++){
            b[i]=Integer.parseInt(a[i].trim());
        }
        Main m=new Main();
        List<Integer> r=m.disappearedNumber(b);
        System.out.println("The disappeared number is:\n"+r);
    }
    public List<Integer> disappearedNumber(int[] nums){
        int m=nums.length;
        int[] map=new int[m+1];
        List<Integer> ans=new ArrayList<>();
        for(int e:nums){
            map[e]++;
        }
        for(int i=1;i<m+1;i++){
            if(map[i]==0){
                ans.add(i);
            }
        }
        return ans;
    }
}


import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the letters of the word separated by commas:");
        String input=sc.nextLine();
        String[] a=input.split(",");
        char[] b=new char[a.length];
        for(int i=0;i<a.length;i++){
            b[i]=a[i].trim().charAt(0);
        }
        Main m=new Main();
        m.reverseString(b);
        System.out.println("The reversed String is:\n"+Arrays.toString(b));
    }
    public void reverseString(char[] s){
        for(int i=0,j=s.length-1;i<s.length/2;i++,j--){
            char temp=s[i];
            s[i]=s[j];
            s[j]=temp;
        }
    }
}


import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number:");
        int num=sc.nextInt();
        Main m=new Main();
        String r=m.base7(num);
        System.out.println("The base of 7 of the given number is:\n"+r);
    }
    public String base7(int num){
        int base=1;
        int ans=0;
        while(num!=0){
            int rem=num%7;
            ans+=base*rem;
            base*=10;
            num/=7;
        }
        return Integer.toString(ans);
    }
}


import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number:");
        int n=sc.nextInt();
        Main m=new Main();
        int fib= m.fib(n);
        System.out.println("The fibonacci value of the entered numberr is:\n"+fib);
    }
    public int fib(int n){
        var dp=new int[n+2];
        dp[n+1]=1;
        for(int i=n-1;i>=0;i--){
            dp[i]=dp[i+1]+dp[i+2];
        }
        return dp[0];
    }
}


import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the Number:");
        int n=sc.nextInt();
        Main m=new Main();
        int c=m.numComplement(n);
        System.out.println("The complement of the number is:\n"+c);
    }
    public int numComplement(int num){
        int temp=num;
        String s="";
        while(temp!=0){
            if((temp&1)==1) s+="0";
            else s+="1";
            temp>>=1;
        }
        StringBuilder sb=new StringBuilder(s);
        sb.reverse();
        int ans=Integer.parseInt(new String(sb),2);
        return ans;
    }
}


import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the 1st number:");
        int a= sc.nextInt();
        System.out.println("Enter the 2nd number:");
        int b= sc.nextInt();
        Main m=new Main();
        int r=m.hammingDis(a,b);
        System.out.println("The hamming distance of the given numbers are:\n"+r);
    }
    public int hammingDis(int x,int y){
        int count=0;
        int a=x^y;
        String b=Integer.toBinaryString(a);
        for (int i=0;i<b.length();i++){
            if(b.charAt(i)=='1') count++;
        }
        return count;
    }
}

import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the 1st number:");
        int a=sc.nextInt();
        System.out.println("Enter the 2nd number:");
        int b=sc.nextInt();
        Main m=new Main();
        int r=m.boolOR(a,b);
        System.out.println("The result is:\n"+r);
    }
    public int boolOR(int left,int right){
        int c=0;
        while(left!=right){
            left>>=1;
            right>>=1;
            c++;
        }
        return(left<<c);
    }
}


import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of people:");
        int a= sc.nextInt();
        sc.nextLine();
        System.out.println("Enter the trust separated by commas:");
        String input=sc.nextLine();
        String[] b=input.split(",");
        int[][] c=new int[b.length][b.length];
        for(int i=0;i<b.length;i++){
            c[i][i]=Integer.parseInt(b[i].trim());
        }
        Main m=new Main();
        int r=m.getJudge(a,c);
        System.out.println("The trustworthy number of judges are:\n"+r);
    }
    public int getJudge(int n,int[][] trust){
        int[] t=new int[n+1];
        for(int[] r:trust){
            t[r[0]]--;
            t[r[1]]++;
        }
        for(int i=1;i<=n;++i){
            if(t[i]==n-1){
                return i;
            }
        }
        return -1;
    }
}

import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the string:");
        String a=sc.nextLine();
        Main m=new Main();
        int res=m.longestPalindrome(a);
        System.out.println("The Longest Palindrome is:\n"+res);
    }
    public int longestPalindrome(String s){
        int[] c=new int[128];
        for(char ch:s.toCharArray()){
            c[ch]++;
        }
        int r=0;
        for(int co:c){
            r+=co/2*2;
            if(r%2==0 && co%2==1)
                r+=1;
        }
        return r;
    }
}

import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the numbers separated by commas:");
        String input=sc.nextLine();
        String[] a=input.split(",");
        int[] b=new int[a.length];
        for(int i=0;i< a.length;i++){
            b[i]=Integer.parseInt(a[i].trim());
        }
        Main m=new Main();
        int r=m.findThird(b);
        System.out.println("The Third number is:\n"+r);
    }
    public int findThird(int[] nums){
        Arrays.sort(nums);
        int n=nums[nums.length-1];
        int t=1;
        int i=nums.length-1;
        while(t<3 && i>0){
            if(nums[i]!=nums[i-1]){
                t++;
                if(t==3)
                    return nums[i-1];
            }
            i--;
        }
        return n;
    }
}

import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number:");
        String input=sc.nextLine();
        String[] a=input.split(",");
        int[] b=new int[a.length];
        for(int i=0;i< a.length;i++){
            b[i]=Integer.parseInt(a[i].trim());
        }
        Main m=new Main();
        int r=m.maxOnes(b);
        System.out.println("The maximum number of 1's are:\n"+r);
    }
    public int maxOnes(int[] nums){
        int m=0,j=-1,i=0;
        for(;i< nums.length;i++){
            if(nums[i]==0){
                m=Math.max(m,i-j-1);
                j=i;
            }
        }
        return Math.max(m,i-j-1);
    }
}

import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the word:");
        String a=sc.nextLine();
        Main m=new Main();
        boolean r= m.detectCap(a);
        System.out.println("Capital:"+(r?"True":"False"));
    }
    public boolean detectCap(String word){
        int first=0,low=0,caps=0;
        for (char ch:word.toCharArray()){
            if(ch>=65 && ch<=90){
                caps++;
                if(first==0) first=1;
            }
            else{
                low++;
                if(first==0) first=2;
            }
        }
        if(caps==0 || low==0 || first==1 && caps==1) return true;
        else return false;
    }
}

import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the length and the breadth separated by commas:");
        String input=sc.nextLine();
        String[] a=input.split(",");
        int[][] b=new int[a.length][a.length];
        for(int i=0;i<a.length;i++){
            b[i][i]=Integer.parseInt(a[i].trim());
        }
        Main m=new Main();
        int r=m.islandPerimeter(b);
        System.out.println("The Island Perimeter is:\n"+r);
    }
    public int islandPerimeter(int[][]g){
        int c=0;
        for(int i=0;i<g.length;i++){
            for(int j=0;j<g[0].length;j++){
                if(g[i][j]==1){
                    if(i+1>=g.length || g[i+1][j]==0) c++;
                    if(j+1>=g[0].length || g[i][j+1]==0) c++;
                    if(i-1<0 || g[i-1][j]==0) c++;
                    if(j-1<0 || g[i][j-1]==0) c++;
                }
            }
        }
        return c;
    }
}

import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the time separated by commas:");
        String input=sc.nextLine();
        String[] a=input.split(",");
        int[] b=new int[a.length];
        for(int i=0;i<a.length;i++){
            b[i]=Integer.parseInt(a[i].trim());
        }
        System.out.println("Enter the duration:");
        int e=sc.nextInt();
        Main m=new Main();
        int r=m.teemoAtt(b,e);
        System.out.println("The Teemo attacking Ashe is:\n"+r);
    }
    public int teemoAtt(int[] t,int d){
        int sum=d;
        int temp=t[0]+d-1;
        for(int i=1;i<t.length;i++){
            if(t[i]>temp){
                sum+=d;
            }
            else{
                sum+=t[i]+d-1-temp;
            }
            temp=t[i]+d-1;
        }
        return sum;
    }
}
