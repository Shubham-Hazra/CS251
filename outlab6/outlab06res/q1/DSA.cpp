#include "DSA.h"
using namespace std;



SinglyLinkedListNode::SinglyLinkedListNode (){
    data = -1; 
    next = NULL;
}

SinglyLinkedListNode::SinglyLinkedListNode (ll val) {
    data = val;
    next = NULL;
}

SinglyLinkedList::SinglyLinkedList () {
            head = NULL;
            tail = NULL;
        }


void SinglyLinkedList::insert (ll data) {
            SinglyLinkedListNode *node = new SinglyLinkedListNode(data);
            if (head == NULL) {
                head = node;
            }
            else {
                tail -> next = node;
            }
            tail = node;
        }
        

SinglyLinkedListNode* SinglyLinkedList::find (ll data) {
    SinglyLinkedListNode *ptr = head, *prev = NULL;
    while (ptr != NULL && ptr -> data != data) {
            prev = ptr;
            ptr = ptr -> next;
        }
        return prev;
}
        bool SinglyLinkedList::deleteVal (ll data) {
            SinglyLinkedListNode *prev = find(data);
            if (prev -> next == NULL) {
                return false;
            }
            prev -> next -> next = prev -> next;
            return true;
        }
        
        void SinglyLinkedList::printer (string sep = ", ") {
            SinglyLinkedListNode *ptr = head;
            cout << "[";
            while (ptr != NULL) {
                cout << *ptr;
                ptr = ptr -> next;
                if (ptr != NULL) {
                    cout << sep;
                }
            }
            cout << "]\n";
        }
        void SinglyLinkedList::reverse () {
            SinglyLinkedListNode *ptr = head, *prev = NULL;
            while (ptr != NULL) {
                SinglyLinkedListNode *ptr2 = ptr -> next;
                ptr -> next = prev;
                prev = ptr;
                ptr = ptr2;
            }
            tail = ptr;
            head = prev;
        }

// ------------------------------- Doubly Linked List -----------------------------


        DoublyLinkedListNode::DoublyLinkedListNode () {
            data = -1;
            next = NULL;
            prev = NULL;
        }

        DoublyLinkedListNode::DoublyLinkedListNode (ll val) {
            data = val;
            next = NULL;
            prev = NULL;
        }



        DoublyLinkedList::DoublyLinkedList () {
            head = NULL;
            tail = NULL;
        }

        void DoublyLinkedList::insert (ll data) {
            DoublyLinkedListNode *node = new DoublyLinkedListNode(data);
            if (head == NULL) {
                head = node;
            }
            else {
                tail -> next = node;
                node -> prev = tail;
            }
            tail = node;
        }
 
        void DoublyLinkedList::printer (string sep = ", ") {
            DoublyLinkedListNode *ptr = head;
            cout << "[";
            while (ptr != NULL) {
                cout << *ptr;
                ptr = ptr -> next;
                if (ptr != NULL) {
                    cout << sep;
                }
            }
            cout << "]\n";
        }
        

        void DoublyLinkedList::reverse () {
            DoublyLinkedListNode *ptr = head, *pr = NULL;
            while (ptr != NULL) {
                DoublyLinkedListNode *ptr2 = ptr -> next;
                if (ptr2 != NULL) {
                    ptr2 -> prev = ptr;
                }
                ptr -> next = pr;
                ptr -> prev - ptr2;
                pr = ptr;
                ptr = ptr2;
            }
            tail = ptr;
            head = pr;
        }


// ------------------------------- Binary Search Tree -----------------------------

//!Node in a Binary Search tree

        BSTNode::BSTNode (ll val) {
            info = val;
            level = 0;
            left = NULL;
            right = NULL;
        }


//!Class for a Binary Search Tree

        BinarySearchTree::BinarySearchTree () {
            root = NULL;
        }

        void BinarySearchTree::insert(ll val) {
            if (root == NULL) {
                root = new BSTNode(val);
            }
            else {
                BSTNode *ptr = root;
                while (true) {
                    if (val < ptr -> info) {
                        if (ptr -> left != NULL) {
                            ptr = ptr -> left;
                        }
                        else {
                            ptr -> left = new BSTNode(val);
                            break;
                        }
                    }
                    else if (val > ptr -> info) {
                        if (ptr -> right != NULL) {
                            ptr = ptr -> right;
                        }
                        else {
                            ptr -> right = new BSTNode(val);
                            break;
                        }
                    }
                    break;
                }
            }
        }

        void BinarySearchTree::traverse (BSTNode* T, order tt) {
            if (tt == PRE) {
                cout << T << endl;
                if (T -> left != NULL) {
                    traverse(T -> left,tt);
                }
                if (T -> right != NULL) {
                    traverse(T -> right,tt);
                }
            }
            else if (tt == IN) {
                if (T -> left != NULL) {
                    traverse(T -> left,tt);
                }
                cout << T << endl;
                if (T -> right != NULL) {
                    traverse(T -> right,tt);
                }
            }
            else if (tt == POST) {
                if (T -> left != NULL) {
                    traverse(T -> left,tt);
                }
                if (T -> right != NULL) {
                    traverse(T -> right,tt);
                }
                cout << T << endl;
            }
        }
 
        ll BinarySearchTree::height(BSTNode *T) {
            if (T -> left == NULL && T -> right == NULL) {
                return 0;
            }
            else if (T -> right == NULL) {
                return 1 + height(T -> left);
            }
            else if (T -> left == NULL) {
                return 1 + height(T -> right);
            }
            return max(1 + height(T -> left),1 + height(T -> right));
        }

// ------------------------------- Suffix Trie -----------------------------


        Trie::Trie () {
            count = 0;
            nodes = map<char,Trie*>();
        }
        

        bool Trie::find(Trie* T, char c) {
            return ((T -> nodes).find(c) != (T -> nodes).end());
        }

        void Trie::insert(string s) {
            Trie* ptr = this;
            for (auto c: s) {
                if (!find(ptr,c)) {
                    (ptr -> nodes)[c] = new Trie();
                }
                ptr = (ptr -> nodes)[c];
                (ptr -> count)++;
            }
        }

        bool Trie::checkPrefix(string s) {
            Trie* ptr = this;
            for (ll i = 0; i < s.length(); i++) {
                if (!find(ptr,s[i])) {
                    if (i == s.length() - 1) {
                        (ptr -> nodes)[s[i]] = NULL;
                    }
                    else {
                        (ptr -> nodes)[s[i]] = new Trie();
                    }
                }
                else if ((ptr -> nodes)[s[i]] == NULL or i == s.length() - 1) {
                    return true;
                }
                ptr = (ptr -> nodes)[s[i]];
            }
            return false;
        }
  
        ll Trie::countPrefix(string s) {
            bool found = true;
            Trie* ptr = this;
            for (auto c: s) {
                if (find(ptr,c)) {
                    ptr = (ptr -> nodes)[c];
                }
                else {
                    found = false;
                    break;
                }
            }
            if (found) {
                return ptr -> count;
            }
            return 0;
        }


// ------------------------------- Heap -----------------------------


        Heap::Heap (int cap) {
           arr = new int[cap];
           n = 0;
        }

        int Heap::parent(int i)
        {
            return (i-1)/2;
        }
 
        int Heap::left(ll i)
        {
            return (2*i) + 1;
        }

        int Heap::right(ll i)
        {
            return 2*(i+1);
        }
 
        void Heap::insert(int val){
            if(n != cap)
            {
                arr[n] = val;
                int i = n;
                n++;
                while(i !=0 && arr[parent(i)] > arr[i])
                {
                    int temp = arr[i];
                    arr[i] = arr[parent(i)];
                    arr[parent(i)]  = temp;
                }
            }
        }

        int Heap::min() {
            if(n!=0)
            {
                return arr[0];
            }
            return -1;
        }
 
        void Heap::Heapify(int root)
        {
            int l = left(root);
            int r = right(root);
            int s = root;
            if(l<n && arr[l]<arr[root])
            {
                s=l;
            }
            if(r<n && arr[r]<arr[s])
            {
                s=r;
            }
            if(s!=root)
            {
                int temp = arr[s];
                arr[s]=arr[root];
                arr[root]=temp;
                Heapify(s);
            }
        }
        
        void Heap::deleteMin()
        {
            if(n>0)
            {
                if(n==1)
                {
                    arr = new int[cap];
                    n = 0;
                }
                else
                {
                    n--;
                    arr[0]=arr[n];
                    Heapify(0);
                }
            }
        }
