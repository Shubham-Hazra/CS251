package Q1;

public class Test {

    public static Boolean check(Matrix m, Matrix1 m1) {
        if(m.getrows() != m1.getrows() || m.getcols() != m1.getcols()) {
            return false ;
        }
        for(int i=0;i<m.getrows();i++) {
            for(int j=0;j<m.getcols();j++) {
                if(m.getelem(i, j) != m1.getelem(i, j)) return false ;
            }
        }
        return true ;
    }
    public static void main(String [] args) {
        Double score = 0.0 ;
        String feedback = "" ;
        try {
            

            Matrix m = new Matrix(20, 10) ;
            Matrix1 m1 = new Matrix1(20, 10) ;
            if(check(m, m1)) {score += 2 ;
            // case 1
            feedback += "case 1: Passed, " ;
            }
            else{
                feedback += "case 1: Failed, " ;
            }

            m = new Matrix(10, 12, 5) ;
            m1 = new Matrix1(10, 12, 5) ;
            if(check(m, m1)) {score += 2 ;
            // case 2
            feedback += "case 2: Passed, " ;
            }
            else{
                feedback += "case 2: Failed, " ;
            }

            Matrix n = Matrix.add(m, m) ;
            Matrix1 n1 = Matrix1.add(m1, m1) ;
            if(check(n, n1)) {score += 3 ;
            // case 3
            feedback += "case 3: Passed, " ;
            }
            else{
                feedback += "case 3: Failed, " ;
            }

            Matrix p = new Matrix(11, 2, 3) ;
            Matrix1 p1 = new Matrix1(11, 2, 3) ;

            Matrix z = Matrix.add(n, p) ;
            Matrix1 z1 = Matrix1.add(n1, p1) ;
            if(check(z, z1)) {score += 2 ;
            // case 4
            feedback += "case 4: Passed, " ;}
            else{
                feedback += "case 4: Failed, " ;
            }

            n.scalarmul(5) ;
            n1.scalarmul(5);
            if(check(n, n1)) {score += 2 ;
            // case 5
            feedback += "case 5: Passed, " ;}
            else{
                feedback += "case 5: Failed, " ;
            }

            Matrix q = new Matrix(2, 3, 4) ;
            Matrix1 q1 = new Matrix1(2, 3, 4) ;

            for(int i=0;i<2;i++) {
                for(int j=0;j<3;j++) {
                    q.setelem(i, j, i+j);
                    q1.setelem(i, j, i+j);
                }
            }

            if(check(q, q1)) {score += 2 ;
            // case 6
            feedback += "case 6: Passed, " ;}
            else{
                feedback += "case 6: Failed, " ;
            }

            Matrix r = Matrix.matmul(p, q) ;
            Matrix1 r1 = Matrix1.matmul(p1, q1) ;
            if(check(r, r1)) {score += 4 ;
            // case 7
            feedback += "case 7: Passed, " ;}
            else{
                feedback += "case 7: Failed, " ;
            }

            Matrix s = Matrix.matmul(q, p) ;
            Matrix1 s1 = Matrix1.matmul(q1, p1) ;
            if(check(s, s1)) {score += 2 ;
            // case 8
            feedback += "case 8: Passed, " ;}
            else{
                feedback += "case 8: Failed, " ;
            }
            
            if(p.getelem(0, -1) == -1) score += 0.5 ;
            
            if(p.getelem(11, 2) == -1) {score += 0.5 ;
            // case 9
            feedback += "case 9: Passed, " ;}
            else{
                feedback += "case 9: Failed, " ;
            }

            feedback += " Score: " + score ;
            feedback += ", Total Case: 9 " ;

            System.out.println(score);
            System.out.print(feedback);
        } catch (Exception e) {
            // System.out.println("Exception!!");
            System.out.println(score);
            feedback += " Score: " + score ;
            feedback += ", Total Case: 9 " ;
            System.out.print(feedback);
        }
    }
}
