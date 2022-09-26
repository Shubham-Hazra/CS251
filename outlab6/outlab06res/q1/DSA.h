#include <bits/stdc++.h>
#define ll long long int
#define vi vector<int>
#define vll vector<ll>
using namespace std;

/**
 * @file DSA.h
 * This file contains 4 different types of data structures. Namely Singly Linked
 * lists, Doubly Linkd Lists, Binary search trees and Suffix tries. It contains their 
 * constructors and few of their member functions. Also some overloaded operators are
 * also given.
 * @author Shubham Hazra
 * @date 21 September 2022
 * @brief This file contains 4 different types of data structures
 * @version 1.0
 */

/* ------------------------------- Data Structures ---------------------------------- */

// ------------------------------- Singly Linked List -----------------------------

//!Node in a singly linked list
class SinglyLinkedListNode {

    public:

        ll data;///< Data stored in the node
        SinglyLinkedListNode* next;///< Pointer to the next node

        /**
        * @brief This is a constructor method to create a SinglyLinkedListNode.
        * Sets data to -1.
        * Sets next to NULL.
        * @param[in] NULL
        */  
        SinglyLinkedListNode ();
        
        /**
        * @brief This is a constructor method to create a SinglyLinkedListNode.
        * Sets data to val.
        * Sets next to NULL.
        * @param[in] ll val
        */  
        SinglyLinkedListNode (ll val);
};
        /**
        * @brief This is a function which operates on SinglyLinkedLists.
        * @param[in] ostream &out
        * @param[in] const SinglyLinkedListNode &node
        * @returns ostream object with the node info
        * 
        */  
ostream& operator<<(ostream &out, const SinglyLinkedListNode &node) {
    return out << node.data;
}

//!Class for a Singly Linked List
class SinglyLinkedList {

    public:
        
        SinglyLinkedListNode *head;///<Pointer to the head of the list
        SinglyLinkedListNode *tail;///<Pointer to the tail of the list
        
        /**
        * @brief This is a constructor method to create a SinglyLinkedList.
        * Sets head to NULL.
        * Sets tail to NULL.
        * @param[in] NULL
        */  
        SinglyLinkedList ();
        
        /**
        * @brief This is a member function to insert a new element.
        * Inserts a new node with data as the element in it.
        * @param[in] ll data
        */  
        void insert (ll data);
        
        /**
        * @brief This is a member function to find an element.
        * @param[in] ll data
        * @param[out] ll prev
        * @returns NULL if not found else returns pointer to the node containing the element
        * 
        */  
        SinglyLinkedListNode* find (ll data);
        
        /**
        * @brief This is a member function to delete an element.
        * @param[in] ll data
        * @param[out] bool
        * @returns true if successfully deleted else false
        * 
        */  
        bool deleteVal (ll data);
        
        /**
        * @brief This is a printer function to print the values in the list.
        * @param[in] NULL
        * @param[out] Prints the list
        * @returns NULL
        * 
        */  
        void printer (string sep);
        
        /**
        * @brief This is a member function to reverse the order of the list.
        * @param[in] NULL
        * @returns NULL
        * 
        */  
        void reverse ();

};

        /**
        * @brief This is a function which operates on SinglyLinkedLists to merge two lists together.
        * @param[in] SinglyLinkedList list1
        * @param[in] SinglyLinkedList list2
        * @param[out] SinglyLinkedList merged
        * @returns The merged list
        * 
        */  
SinglyLinkedList merge (SinglyLinkedList list1, SinglyLinkedList list2) {
    SinglyLinkedList merged;
    SinglyLinkedListNode *head1 = list1.head, *head2 = list2.head;
    while (head1 != NULL && head2 != NULL) {
        if (head1 -> data < head2 -> data) {
            merged.insert(head1 -> data);
            head1 = head1 -> next;
        }
        else {
            merged.insert(head2 -> data);
            head2 = head2 -> next;
        }
    }
    if (head1 == NULL && head2 != NULL) {
        merged.tail -> next = head2;
    }
    if (head2 == NULL && head1 != NULL) {
        merged.tail -> next = head1;
    }
    return merged;
}


// ------------------------------- Doubly Linked List -----------------------------


//!Node in a Doubly Linked List
class DoublyLinkedListNode {

    public:
        
        ll data; ///< Data in the node
        DoublyLinkedListNode *next;///<Pointer to next node 
        DoublyLinkedListNode *prev;///<Pointer to the previous node
        
        /**
        * @brief This is a constructor method to create a DoublyLinkedListNode.
        * Sets data to -1.
        * Sets next to NULL.
        * Sets prev to NULL.
        * @param[in] NULL
        */ 
        DoublyLinkedListNode ();
        
        /**
        * @brief This is a constructor method to create a DoublyLinkedListNode.
        * Sets data to val.
        * Sets next to NULL.
        * Sets prev to NULL.
        * @param[in] ll val
        */ 
        DoublyLinkedListNode (ll val);
};

        /**
        * @brief This is a function which operates on DoublyLinkedLists.
        * @param[in] ostream &out
        * @param[in] const DoublyLinkedListNode &node
        * @returns ostream object with the node data
        * 
        */  
ostream& operator<<(ostream &out, const DoublyLinkedListNode &node) {
    return out << node.data;
}

//!Class for a Doubly Linked List.
class DoublyLinkedList {

    public:
        
        DoublyLinkedListNode *head;///<Pointer to head of the list
        DoublyLinkedListNode *tail;///< Pointer to tail of the list
        
        /**
        * @brief This is a constructor method to create a SinglyLinkedList.
        * Sets head to NULL.
        * Sets tail to NULL.
        * @param[in] NULL
        */ 
        DoublyLinkedList ();
        
        /**
        * @brief This is a member function to insert a new element.
        * Inserts a new node with data as the element in it.
        * @param[in] ll data
        * @returns NULL
        */  
        void insert (ll data);
        
        /**
        * @brief This is a printer function to print the values in the list.
        * @param[in] NULL
        * @param[out] Prints the list
        * @returns NULL 
        * 
        */  
        void printer (string sep);
        
        /**
        * @brief This is a member function to reverse the order of the list.
        * @param[in] NULL
        * @returns NULL
        * 
        */  
        void reverse ();

};


// ------------------------------- Binary Search Tree -----------------------------

//!Node in a Binary Search tree
class BSTNode {

    public:

        ll info;///< Contains the element
        ll level;///< Contains level of the node in the tree
        BSTNode *left;///<Pointer to the left node
        BSTNode *right;///<Pointer to the right node
        

        /**
        * @brief This is a constructor method to create a DoublyLinkedListNode.
        * Sets info to val.
        * Sets level to 0.
        * Sets left to NULL.
        * Sets right to NULL.
        * @param[in] ll val
        */ 
        BSTNode (ll val);

};
        /**
        * @brief This is a function which operates on BSTs.
        * @param[in] ostream &out
        * @param[in] const BSTNode &node
        * @returns ostream object with the node info
        * 
        */  
ostream& operator<<(ostream &out, const BSTNode &node) {
    return out << node.info;
}

//!Class for a Binary Search Tree
class BinarySearchTree {

    public:
        
        BSTNode *root;///< Pointer to the root of the tree
        
        enum order {PRE, IN, POST};///< Enum defining the ways of traversal
        
        /**
        * @brief This is a constructor method to create a Binary search tree.
        * Sets root to NULL.
        * @param[in] ll val
        */ 
        BinarySearchTree ();
        /**
        * @brief This is a member function to insert a new element.
        * Inserts a new node with data as the element in it.
        * @param[in] ll data
        * @returns NULL
        */  
        void insert(ll val);
        /**
        * @brief This is a printer function to print the tree in the traversal order given.
        * @param[in] BSTNode* T
        * @param[in] order TT
        * @param[out] prints the binary search tree in the order given
        * @returns NULL
        * 
        */  
        void traverse (BSTNode* T, order tt);
        
        /**
        * @brief This is a member function to get the height of the node.
        * @param[in] BSTNode* T
        * @param[out] ll height
        * @returns height of the node
        * 
        */  
        ll height(BSTNode *T);

};

// ------------------------------- Suffix Trie -----------------------------

//!Class for a suffix trie
class Trie {

    public:
        
        ll count;///<Keeps count of nodes below it
        map<char,Trie*> nodes;///< Node in a suffix trie
        
        /**
        * This is a constructor method to create a Suffix Trie.
        * Sets count to 0.
        * Sets nodes to empty map.
        * @param[in] NULL
        */ 
        Trie ();
        
        /**
        * @brief This is a member function to find an element.
        * @param[in] Trie* T
        * @param[in] ll char c
        * @param[out] bool
        * @returns true if found else false
        * 
        */  
        bool find(Trie* T, char c);
        /**
        * @brief This is a member function to insert a new element.
        * Inserts a new node with data as the element in it.
        * @param[in] string s
        * @returns NULL
        */  
        void insert(string s);
        /**
        * @brief This is a member function to check if a prefix is present in the trie
        * @param[in] string s
        * @returns true if found else false
        * 
        */  
        bool checkPrefix(string s);
        /**
        * @brief This is a member function to get the number of count of matches of a prefix in the trie.
        * @param[in] string s
        * @param[out] ll countprefix
        * @returns number of matches
        * 
        */  
        ll countPrefix(string s);

};

// ------------------------------- Heap -----------------------------

//!Class for a binary heap
class Heap {

    private:
        int* arr;///<Array in which the heap is stored
        int n;///<The current number of elements in the heap

    public:
        
        int cap;///<Maximum number of elements in the heap
        
        /**
        * @brief This is a constructor method to create a Heap.
        * Initializes a new array with cap as the number of elements
        * Sets n to 0
        * @param[in] int cap
        */ 
        Heap (int cap);
        /**
        * @brief This is a member function to find the parent of a node.
        * @param[in] int i
        * @param[out] int (i-1)/2
        * @returns The index of the parent of element
        * 
        */  
        int parent(int i);

        /**
        * @brief This is a member function to find the left child of a node.
        * @param[in] int i
        * @param[out] int 2*i+1
        * @returns The index of the left child of element
        * 
        */  
        int left(ll i);

        /**
        * @brief This is a member function to find the right child of a node.
        * @param[in] int i
        * @param[out] int 2*(i+1)
        * @returns The index of the left child of element
        * 
        */  
        int right(ll i);

        /**
        * @brief This is a member function to insert a new element.
        * Inserts a new node with data as the element in it.
        * @param[in] int val
        * @returns NULL
        */  
        void insert(int val);
        /**
        * @brief This is a member function to find the minimum element in a heap.
        * @returns The element with the minimum value
        */  
        int min();
        /**
        * @brief This is to make it into a heap when both the left and right subheaps satisfy the heap property but not the whole heap.
        * @param[in] int root
        * @returns NULL
        */  
        void Heapify(int root);
        /**
        * @brief This is to delete the minimum element in a heap.
        * @returns NULL
        */  
        void deleteMin();
};
