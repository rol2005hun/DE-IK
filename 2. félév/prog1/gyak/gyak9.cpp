#include <iostream>
using namespace std;

struct btree {
    int data;
    btree* left;
    btree* right;
};

btree* createLeaf(int data) {
    btree* uj = new btree;
    uj -> data = data;
    uj -> left = NULL;
    uj -> right = NULL;
    return uj;
}

btree* createBtree(int data, btree* left, btree* right) {
    btree* uj = new btree;
    uj -> data = data;
    uj -> left = left;
    uj -> right = right;
    return uj;
}

void preOrder(btree* tree) {
    cout << tree -> data << " ";
    if(tree -> left != NULL) {
        preOrder(tree -> left);
    }
    if(tree -> right != NULL) {
        preOrder(tree -> right);
    }
}

void inOrder(btree* tree) {
    if(tree -> left != NULL) {
        inOrder(tree -> left);
    }
    cout << tree -> data << " ";
    if(tree -> right != NULL) {
        inOrder(tree -> right);
    }
}

void postOrder(btree* tree) {
    if(tree -> left != NULL) {
        postOrder(tree -> left);
    }
    if(tree -> right != NULL) {
        postOrder(tree -> right);
    }
    cout << tree -> data << " ";
}

bool search(btree* tree, int data) {
    if(tree -> data == data) return true;
    if(tree -> data > data) return search(tree -> left, data);
    else return search(tree -> right, data);
}

int deep(btree* tree) {
    if(tree -> left == NULL) return 0;
    int right = deep(tree -> right) + 1;
    int left = deep(tree -> left) + 1;
    if(left > right) return left;
    else return right;
}

int main() {
    btree* tree1 = createBtree(5, createLeaf(3), createLeaf(7));
    btree* tree2 = createBtree(5, createLeaf(3), createBtree(8, createLeaf(6), createLeaf(12)));
    cout << "Pre order: ";
    preOrder(tree1);
    cout << endl;
    preOrder(tree2);
    cout << endl;
    cout << "In order: ";
    inOrder(tree1);
    cout << endl;
    inOrder(tree2);
    cout << endl;
    cout << "Post order: ";
    postOrder(tree1);
    cout << endl;
    postOrder(tree2);
    cout << endl;
    cout << "Benne van: " << search(tree2, 8);
    cout << endl;
    cout << "Melysege: " << deep(tree2);
    return 0;
}
