package Q1;

public class Matrix {
    private int n,m ;
    private int mat[][] ;

    Matrix(int n, int m, int v) {
        /* 
         * TODO: Complete this constructor
         * Initialize a matrix of size n x m with all elements equal to v
         */ 
        this.n = n;
        this.m = m;
         mat = new int[n][m];
         for(int i=0;i<n;i++)
         {
            for(int j=0;j<m;j++)
            {
                mat[i][j]=v;
            }
         }

    }

    Matrix(int n, int m) {
        /* 
         * TODO: Complete this constructor 
         * Initialize a matrix of size n x m with all elements equal to 0
         */
        this.n = n;
        this.m = m;
         mat = new int[n][m];
         for(int i=0;i<n;i++)
         {
            for(int j=0;j<m;j++)
            {
                mat[i][j]=0;
            }
         }

    }

    static Matrix add(Matrix A, Matrix B) {
        /*
         * TODO: Complete this method
         * Add two matrices and return the result
         * and return a zero matrix of size 1 x 1
         */
        if((A.getcols() != B.getcols()) || (A.getrows()!= B.getrows()))
        {
            Matrix arr = new Matrix(1,1);
            return arr;
        }
        Matrix arr = new Matrix(A.getrows(),A.getcols());
        for(int i=0;i<A.getrows();i++)
         {
            for(int j=0;j<A.getcols();j++)
            {
                arr.setelem(i,j,A.getelem(i,j)+B.getelem(i,j));
            }
         }
         return arr;
    }

    static Matrix matmul(Matrix A, Matrix B) {
        /*
         * TODO: Complete this method
         * Multiply two matrices and return the result
         * and return a zero matrix of size 1 x 1
         */
         if(A.getcols() != B.getrows())
         {
            Matrix arr = new Matrix(1,1);
            return arr;
         }
         Matrix arr = new Matrix(A.getrows(),B.getcols());
         for(int i=0;i<arr.getrows();i++)
         {
            for(int j=0;j<arr.getcols();j++)
            {
                int sum =0;
                for(int k=0;k<A.getcols();k++)
                {
                    sum+=A.getelem(i,k)*B.getelem(k,j);
                }
                arr.setelem(i,j,sum);
            }
         }
         return arr;
    }

    void scalarmul(int k) {
        /*
         * TODO: Complete this method
         * Multiply all elements of the matrix by k
         */
         for(int i=0;i<n;i++)
         {
            for(int j=0;j<m;j++)
            {
                mat[i][j]*=k;
            }
         }

    }

    int getrows() {
        /*
         * TODO: Complete this method
         * Return the number of rows in the matrix
         */
         return n;
    }

    int getcols() {
        /*
         * TODO: Complete this method
         * Return the number of columns in the matrix
         */
         return m;
    }

    int getelem(int i,int j) {
        /*
         * TODO: Complete this method
         * Return the element at row i and column j
         * If i or j is out of bounds, return -1
         */
         return mat[i][j];
    }

    void setelem(int i,int j, int v) {
        /*
         * TODO: Complete this method
         * Set the element at row i and column j to v
         * If i or j is out of bounds, don't change anything
         */
         mat[i][j]=v;
    }

    void printmatrix() {
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                if(j!=0) System.out.print(" ");
                System.out.print(mat[i][j]);
            }
            System.out.print("\n") ;
        }
    }
}

