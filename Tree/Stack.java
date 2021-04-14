
//  stack using linked list
class Node {

    public int data;
    public Node next;

    public Node() {this.data = 0; this.next = null;}

    public Node(int data) {
        this.data = data;
        this.next = null;
    }

}


class StackClass {
    
    private Node top;
    private Node tailNode;

    public StackClass() {
        this.top = this.tailNode = null;
    }

    public void push(int data) {    
        try {
            Node new_node = new Node(data); //  memory is allocated here

            if(this.top == null){
                this.top = new_node;
                this.tailNode = new_node;
            }else{
                this.tailNode.next = new_node;
                this.tailNode = new_node;
            }

        } catch (Exception e) {
            System.out.print("No memory available to allocate a node (Overflow).");
        }
    }


    public int pop() {

        //  1. we will return -1 when underflow
        if(this.top == null) {
            return -1;
        }

        //  2. when there is only one node to be popped
        if(this.top.next == null) {
            int temp = this.top.data;
            this.top = null;
            this.tailNode = null;
            return temp;
        }

        Node ptr = this.top;
        while(ptr.next != this.tailNode) {
            ptr = ptr.next;
        }

        int temp = this.tailNode.data;
        this.tailNode = ptr;
        ptr.next = null;

        return temp;

    }

    public void traverse() {
        Node ptr = this.top;
        if(this.top==null){
            System.out.println("Stack underflow");
        }
        while(ptr!=null) {
            System.out.print(ptr.data+" ");
            ptr = ptr.next;
        }
    }

}


public class Stack {
    public static void main(String[] args) {
        StackClass stack = new StackClass();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(5);

        System.out.print(stack.pop());
        System.out.print(stack.pop());
        System.out.print(stack.pop());
        System.out.print(stack.pop());
        System.out.print(stack.pop());
        System.out.println("Elements left");
        stack.traverse();

        System.out.print(stack.pop());

    }
}
