import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
public static void main (String[] args) throws java.lang.Exception
{
Scanner sc = new Scanner(System.in);

int T = sc.nextInt();

while (T-- > 0)
{
String s = sc.next();

int n = s.length();
int mid = n / 2;

String left = s.substring(0, mid);
String right;

if (n % 2 == 0)
right = s.substring(mid);
else
right = s.substring(mid + 1);

char[] a = left.toCharArray();
char[] b = right.toCharArray();

Arrays.sort(a);
Arrays.sort(b);

if (Arrays.equals(a, b))
System.out.println("YES");
else
System.out.println("NO");
}

sc.close();
}
}
