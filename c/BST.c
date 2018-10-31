#include <stdio.h>
#include <stdlib.h>

struct Node
{
	int data;
	struct Node *right;
	struct Node *left;
};

struct Node * new_node(int value)
{
	struct Node *new = (struct Node*)malloc(sizeof(struct Node));
	new->data = value;
	new->right = NULL;
	new->left = NULL;

	return new;
}

//why is this wrong? (no elements are being added)
/*
void insert(struct Node *root, int value)
{
	if (root == NULL)
	{
		root = new_node(value);
		return;
	}
	else if (value > root->data)
		insert(root->right, value);
	else if (value < root->data)
		insert(root->left, value);
}
*/

struct Node * insert(struct Node *root, int value)
{
	if (root == NULL)
	{
		return new_node(value);
	}
	else if (value > root->data)
		root->right = insert(root->right, value);
	else if (value < root->data)
		root->left = insert(root->left, value);

	return root;
}

void inorder(struct Node *root)
{
	if (root == NULL)
		return;
	else
	{
		inorder(root->left);
		printf("%d \n", root->data);
		inorder(root->right);
	}
}

void delete(struct Node *root, int value)
{
	int a;
	
	while (value != a)
	{
		a = root->data;
		
		if value > root->data
		{
			root = root->right;
		}
		if value < root->data
		{
			root = root->left;
		}
	}
}

int main(void)
{
	struct Node *base = new_node(5);

	insert(base, 8);
	insert(base, 6);
	insert(base, 9);
	insert(base, 1);
	insert(base, 3);
	insert(base, 2);
	insert(base, 4);

	
	inorder(base);

	return 0;
}
