package Q2 ;

public class Board {
    private int [][] board = new int[3][3];
    /* elements of board is either 0, 1 or 2 
     * 0 means empty
     * 1 means player 1's token  (say X)
     * 2 means player 2's token  (say O)
     */

    public void printBoard(){
        /*
         * Don't change this function
         */
        System.out.println("Board:");
        System.out.println("-------------");
        for(int i=0;i<3;i++){
            System.out.print("| ");
            for(int j=0;j<3;j++){
                if(board[i][j]==0){
                    System.out.print(" ");
                }
                else if(board[i][j]==1){
                    System.out.print("X");
                }
                else if(board[i][j]==2){
                    System.out.print("O");
                }
                System.out.print(" | ");
            }
            System.out.println("\n-------------");   
        }
    }

    public Boolean available(Integer x, Integer y){
        /*
         * TODO: Check if the position (x,y) is available
         * return true if available. 
         * Also return false if (x,y) is not a valid position
         */

    }


    public void updateBoard(Integer[] pos, Integer id){
        /*
         * TODO: Update the board 
         */


    }

    // create any helper functions you need

    

    public int checkBoard() {

        printBoard();
        /*
         * Don't remove the above line
         */

        // EDIT BELOW THIS LINE
        /*
         * TODO: Check the board and return the status of the game
         * -1 if Game has Not yet Ended
         * 0 if Game has Ended in a Draw
         * 1 if Player 1 has Won
         * 2 if Player 2 has Won
         */
        
    }
}
