#include <iostream>
using namespace std;

struct Node {
	int data;
	Node* left;
	Node* right;
	Node(int d) : data(d), left(nullptr), right(nullptr) { }
	~Node() {
		left = right = nullptr;
	}
};

class BST {
	Node* root;
public:
	BST(Node* r = nullptr) : root(r) { }
	void insertNode(int data);
	Node* getRoot() {
		return root;
	}
};

void BST :: insertNode(int data) {
	if(root == nullptr) {
		root = new Node(data);
		return;
	}
	auto temp = root;
	do {
		if(temp->data <= data) {
			if(temp->right != nullptr) {
				temp = temp->right;
			}
			else {
				temp->right = new Node(data);
				return;
			}
		}
		else {
			if(temp->left != nullptr) {
				temp = temp->left;
			}
			else {
				temp->left = new Node(data);
				return;
			}
		}
	} while(temp->left != nullptr && temp->right != nullptr);
	if(temp->data <= data) {
		temp->right = new Node(data);
	}
	else {
		temp->left = new Node(data);
	}
}
const int COUNT = 10;
void print2DUtil(Node *root, int space)  
{
	if (root == nullptr)
		return;
	space += COUNT;
	print2DUtil(root->right, space);
	cout<<endl;
	for (int i = COUNT; i < space; i++)
		cout<<" ";
	cout<<root->data<<"\n";
	print2DUtil(root->left, space);  
}

int main() {
	BST* bst = new BST;
	bst->insertNode(10);
	bst->insertNode(7);
	bst->insertNode(18);
	bst->insertNode(15);
	bst->insertNode(21);
	bst->insertNode(30);
	bst->insertNode(3);
	bst->insertNode(8);
	bst->insertNode(9);

	print2DUtil(bst->getRoot(), 10);
	return 0;
}
