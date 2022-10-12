package Q1;

import java.util.Map.Entry;
import java.util.*;
import java.util.regex.*;

class Dist implements Comparable<Dist> {
    private String key;
    private int value;

    public Dist(String key, int value) {
        this.key = key;
        this.value = value;
    }

    public String getKey() {
        return key;
    }

    public int getValue() {
        return value;
    }

    @Override
    public int compareTo(Dist other) {
        if (this.getValue() < other.getValue()) {
            return 1;
        } else if (this.getValue() > other.getValue()) {
            return -1;
        }
        return 0;
    }
}

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
        return;
    }

    public Map<String, Integer> dijkstraAlgorithm(String source) {
        /*
         * TODO: Implement this method
         * Return a map of name of all the nodes
         * with the minimum distance from source node
         */
        // PriorityQueue<Node> pq;
        // pq = new PriorityQueue<Node>(nodeMap.size(), new Node());
        Map<String, Integer> dist = new HashMap<>();
        Map<String, Boolean> u = new HashMap<>();
        for (Map.Entry<String, Node> e : nodeMap.entrySet()) {
            dist.put(e.getKey(), INF);
            u.put(e.getKey(), false);
        }
        dist.put(source, 0);
        PriorityQueue<Dist> q;
        q = new PriorityQueue<Dist>(nodeMap.size());
        q.add(new Dist(source, dist.get(source)));
        while (!q.isEmpty()) {
            String v = q.peek().getKey();
            int d_v = q.peek().getValue();
            q.poll();
            if (dist.get(v) != d_v) {
                continue;
            }
            for (Map.Entry<Node, Integer> adj : nodeMap.get(v).adjacentNodes.entrySet()) {
                String adj_string = adj.getKey().getName();
                int len = adj.getValue();
                if (dist.get(v) + len < dist.get(adj_string)) {
                    dist.put(adj_string, dist.get(v) + len);
                    q.add(new Dist(adj_string, dist.get(adj_string)));
                }
            }
        }
        return dist;
    }

}
