package Q1;

import java.util.Map.Entry;
import java.util.*;
import java.util.regex.*;

public class Graph {

    // Assume maximum path length to be less than INF
    private static Integer INF = 1000 * 1000 * 1000;
    private Map<String, Node> nodeMap = new HashMap<>();

    public void addNode(String name) {
        /*
         * TODO: Implement this method
         */
        Node t = new Node(name);
        nodeMap.put(name, t);
    }

    public void addDirectedEdge(String nameA, String nameB, Integer distance) {
        /*
         * TODO: Implement this method
         * Check if nodes with nameA and nameB exist.
         */
        if (!nodeMap.containsKey(nameA) || !nodeMap.containsKey(nameB)) {
            return;
        }
        Node A = nodeMap.get(nameA);
        Node B = nodeMap.get(nameB);
        A.addNeighbour(B, distance);
    }

    public Map<String, Integer> dijkstraAlgorithm(String source) {
        /*
         * TODO: Implement this method
         * Return a map of name of all the nodes
         * with the minimum distance from source node
         */

    }
}