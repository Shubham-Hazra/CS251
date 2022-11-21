package Q1 ;

public class Matrix1 {
    private int n,m ;
    private int mat[][] ;

    Matrix1(int n, int m, int v) {
        /* 
         * TODO: Complete this constructor
         * Initialize a Matrix1 of size n x m with all elements equal to v
         */ 
        this.n = n ;
        this.m = m ;
        mat = new int[n][m] ;
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                mat[i][j] = v ;
            }
        }
    }

    Matrix1(int n, int m) {
        /* 
         * TODO: Complete this constructor 
         * Initialize a Matrix1 of size n x m with all elements equal to 0
         */
        this.n = n ;
        this.m = m ;
        mat = new int[n][m] ;
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                mat[i][j] = 0 ;
            }
        }
    }

    static Matrix1 add(Matrix1 A, Matrix1 B) {
        /*
         * TODO: Complete this method
         * Add two matrices and return the result
         * If the matrices cannot be added, print "Matrices cannot be added" 
         * and return a zero Matrix1 of size 1 x 1
         */
        if(A.n==B.n && A.m==B.m) {
            Matrix1 res = new Matrix1(A.n,B.m) ;
            for(int i=0;i<A.n;i++) {
                for(int j=0;j<A.m;j++) {
                    res.mat[i][j] = A.mat[i][j] + B.mat[i][j] ;
                }
            }
            return res ;
        }
        else {
            return new Matrix1(1, 1) ;
        }
    
    }

    static Matrix1 matmul(Matrix1 A, Matrix1 B) {
        /*
         * TODO: Complete this method
         * Multiply two matrices and return the result
         * If the matrices cannot be multiplied, print "Matrices cannot be multiplied"
         * and return a zero Matrix1 of size 1 x 1
         */
        if(A.m==B.n) {
            Matrix1 res = new Matrix1(A.n,B.m) ;
            for(int i=0;i<A.n;i++) {
                for(int j=0;j<B.m;j++) {
                    res.mat[i][j] = 0 ;
                    for(int k=0;k<A.m;k++) {
                        res.mat[i][j] += A.mat[i][k]*B.mat[k][j] ; 
                    }
                }
            }
            return res ;
        }
        else {
            return new Matrix1(1, 1) ;
        }
    }

    void scalarmul(int k) {
        /*
         * TODO: Complete this method
         * Multiply all elements of the Matrix1 by k
         */
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                mat[i][j] *= k; 
            }
        }
    }

    int getrows() {
        /*
         * TODO: Complete this method
         * Return the number of rows in the Matrix1
         */
        return n ;
    }

    int getcols() {
        /*
         * TODO: Complete this method
         * Return the number of columns in the Matrix1
         */
        return m ;
    }

    int getelem(int i,int j) {
        /*
         * TODO: Complete this method
         * Return the element at row i and column j
         * If i or j is out of bounds, return -1
         */
        if(i>=n || i<0 || j>=m || j<0) return -1 ;
        return mat[i][j] ;
    }

    void setelem(int i,int j, int v) {
        /*
         * TODO: Complete this method
         * Set the element at row i and column j to v
         * If i or j is out of bounds, dont change anything
         */
        if(i>=n || i<0 || j>=m || j<0) return ;
        mat[i][j] = v ;
    }

    void printMatrix() {
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                if(j!=0) System.out.print(" ");
                System.out.print(mat[i][j]);
            }
            System.out.print("\n") ;
        }
    }
}

