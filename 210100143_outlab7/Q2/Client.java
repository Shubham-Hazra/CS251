package Q2;

import java.net.*;
import java.util.Scanner;
import java.io.*;

public class Client {

    private ServerSocket server = null;
    private Socket socket1 = null;
    private Socket socket2 = null;
    private BufferedReader in = null;
    private PrintWriter out = null;
    private Integer ID = null;
    private Board board = null;
    private Scanner sc = new Scanner(System.in);

    /*
     * server socket allows this player to accept connection from other player
     * socket1 is the accepted connection from server socket
     * socket2 is the socket that connects to the server of the other player
     * NOTE: Socket(HOST, port) throws ConnectException if no server is listening on
     * port
     * handle this while creating socket2
     * Since server.accept is blocking, so order in which sockets are initialised
     * must be considered appropriately.
     */

    /*
     * TODO: Add any variables you need
     */

    private void printResult(int winner, int ID) {
        /*
         * Don't change this function
         */
        if (winner == 0) {
            System.out.println("DRAW");
        } else if (winner == ID) {
            System.out.println("YOU WON");
        } else
            System.out.println("YOU LOSE");
    }

    private Integer[] takeInput() {
        /*
         * TODO: Take input from the user from STDIN and return the position as an array
         * 
         */
        System.out.print("Enter the position: ");

        /* take x and y as space separated integer */
        Integer move[] = new Integer[2];
        String line = sc.nextLine();
        String[] strList = line.split(" ");
        move[0] = Integer.parseInt(strList[0]);
        move[1] = Integer.parseInt(strList[1]);

        /*
         * check if the x and y position is valid and available on the board [x,y in
         * {0,1,2}X{0,1,2}]
         * if not valid or not available, print "INVALID INPUT! Enter again" (without
         * quotes) and ask for input again
         */
        while (true) {
            if (board.available(move[0], move[1])) {
                break;
            } else {
                System.out.println("INVALID INPUT! Enter again");
                System.out.print("Enter the position: ");
                line = sc.nextLine();
                strList = line.split(" ");
                move[0] = Integer.parseInt(strList[0]);
                move[1] = Integer.parseInt(strList[1]);
            }
        }
        return move;
    }

    private void sendMove(Integer[] pos) {
        /*
         * TODO: Send the move to other player by writing to the appropriate socket
         * sent string format: "x y" (space separated)
         */
        // 1st statement
        String s = pos[0] + " " + pos[1];
        out.println(s);
    }

    private Integer[] recieveMove() {
        /*
         * TODO: Recieve the move from the server by reading from the appropriate socket
         * return the move as an array of two integers
         * recieve format: "x y" (space separated)
         */
        Integer move[] = new Integer[2];
        String line = null;
        try {
            while ((line = in.readLine()) == null) {
                continue;
            }
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        // while (line == null || line == "") {
        // try {
        // line = in.readLine();
        // } catch (IOException e) {
        // continue;
        // }
        // }
        String[] strList = line.split(" ");
        move[0] = Integer.parseInt(strList[0]);
        move[1] = Integer.parseInt(strList[1]);
        return move;
    }

    public Client(Integer ID, Integer port1, Integer port2) {
        /*
         * port1 is the port on which server is running and
         * this player will accept connection from other player
         * 
         * port2 is the port on which the server of the other player is running
         */

        /*
         * TODO: Initialize ID
         * Also initialize the board
         */
        this.ID = ID;
        this.board = new Board();

        try {
            /*
             * INITIALIZE THE ServerSocket
             */
            try {
                server = new ServerSocket(port1);
            } catch (IOException e) {
                e.printStackTrace();
            }
            System.out.println("Server started");
            System.out.println("Waiting for a client ...");
            /* Don't chnage above print statements */
            /*
             * INITIALIZE both socket variables, one that connects to other player and other
             * accepting connection on server socket
             * NOTE: Socket(HOST, port) throws java.net.ConnectException if no server is
             * listening on port
             * this happens when the other player is not yet ready to play i.e. has not
             * started the server
             * 
             * handle this by trying to create the socket conneting to other player again
             * and again in a loop until it is created
             * incase of exception just continue the loop
             */
            while (true) {
                try {
                    socket2 = new Socket("localhost", port2);
                    break;
                } catch (java.net.ConnectException e) {
                    continue;
                }
            }
            socket1 = server.accept();
            /*
             * initialize the input and output streams appropriately
             */
            in = new BufferedReader(new InputStreamReader(socket2.getInputStream()));
            out = new PrintWriter(socket1.getOutputStream(), true);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void runClient() {
        Boolean myturn = (ID == 1);
        board.checkBoard();
        int result = -1;
        while (true) {
            /*
             * Here we would have the game logic
             * You can use the functions defined above
             * NOTE: for player with ID 1, it is your turn initially
             * for player with ID 2, it is the other player's turn initially
             * We have implemented the game using a logic which utilizes myturn bool. You
             * are welcome to try any other logic.
             */
            if (myturn) {
                /* your turn */
                Integer move[] = takeInput();
                sendMove(move);
                board.updateBoard(move, ID);
            } else {
                /* other player's turn */
                Integer move[] = recieveMove();
                int id = (ID == 1) ? (2) : (1);
                board.updateBoard(move, id);
            }
            myturn = !myturn;
            result = board.checkBoard();
            if (result != -1) {
                break;
            }
        }
        printResult(result, ID);
        return;
    }

    public static void main(String args[]) {
        /*
         * Don't change this function
         */
        Integer ID = Integer.parseInt(args[0]);
        System.out.println(ID);
        if (ID != 1 && ID != 2) {
            System.out.println("Incorrect Player ID\n");
            return;
        }
        Integer port1 = Integer.parseInt(args[1]);
        Integer port2 = Integer.parseInt(args[2]);
        try {
            Client client = new Client(ID, port1, port2);
            client.runClient();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
