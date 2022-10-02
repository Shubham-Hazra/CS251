package Q2;
import java.util.Scanner;

public class Main {

    /*
     * NOTE: Create helper functions here if required
     */
    static int count_lines=0;
    static int num_test_cases=0;
    static int n=0;
    static int count = 0;
    static int sum = 0;
    static Scanner myObj = new Scanner(System.in);
    public static int square(int n)
    {
        if(count != n)
        {
            int num = myObj.nextInt();
            sum += num*num;
            count++;
            square(n);
        }
        return sum;
    }
    public static void main(String args[]) {
        /*
         * TODO: Complete this method
         * NOTE: Take input from STDIN and print the output to STDOUT
         */
        count_lines++;
        if(count_lines == 1)
        {
            num_test_cases = myObj.nextInt();
        }
        if(num_test_cases !=0 && (count_lines-1)%2 == 1)
        {
            n = myObj.nextInt();        
        }
        if(num_test_cases !=0 && (count_lines-1)%2 == 0 && count_lines != 1)
        {
            int sum1 = square(n);
            System.out.println(sum1);
            count = 0;
            sum = 0;
        }
        if(count_lines!=2*num_test_cases+1)
        {
            main(args);
        }
        myObj.close();
    }
}
