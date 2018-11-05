import java.util.*;

public class ll
{
	public class node
	{
		int value;
		node next;

		node(int data)
		{
			this.value = data;
			this.next = null;
		}
	}

	node head = new node(0);

	void insert_front(int x)
	{
		node temp = new node(x);
		temp.next = head.next;
		head.next = temp;
	}

	public void insert_at_index(int index, int x)
	{
		node temp = new node(x);

		node cur = head;
		
		for (int i = 0; i < index && cur.next != null; i++)
		{
			cur = cur.next;
		}

		temp.next = cur.next;
		cur.next = temp;
	}

	public void printlist()
	{
		node cur = head;

		while (cur.next != null)
		{
			cur = cur.next;
			System.out.println(cur.value);
		}
	}

	public static void main(String[] args)
	{
		ll mylist = new ll();
		
		int array[] = {1,2,3,4,5,6,7,8,9,69};

		for (int i: array)
		{
			mylist.insert_front(i);

		}
		mylist.printlist();

		mylist.insert_at_index(2, 21);
		mylist.printlist();
		/*mylist.printlist();
		mylist.insert(2);
		mylist.printlist();
		mylist.insert(5);
		mylist.printlist();
		mylist.insert(1);
		mylist.printlist();
		mylist.insert(69);
		mylist.printlist();
*/
	}
}