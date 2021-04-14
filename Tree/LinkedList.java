class Node {
    public int data;
    public Node next;

    public Node() {this.data = 0; this.next = null;}

    public Node(int data) {
        this.data = data;
        this.next = null;
    }

}

class LList {
    private Node headNode, tailNode;

    public LList() {
        this.headNode = null;
        this.tailNode = null;
    }

    public void insertNode(int data) {
        Node new_node = new Node(data);
        if(this.headNode == null){
            this.headNode = new_node;
            this.tailNode = new_node;
        }else{
            this.tailNode.next = new_node;
            this.tailNode = new_node;
        }
    }

    public void traverse() {
        Node ptr = this.headNode;
        while(ptr!=null){
            System.out.print(ptr.data+" ");
            ptr = ptr.next;
        }
    }


    //  deleting a node using the data (matching data)
    public void deleteUsingKey(int sk) {
        boolean found = false;

        //  if first node is the node to be deleted
        if (this.headNode.data == sk) {
            this.headNode = this.headNode.next;
            return;
        }

        Node curNode = this.headNode.next;  //  points to the second node
        Node prevNode = this.headNode;  //  points to the first node (headNode)

        while(curNode != null) {
            if(curNode.data == sk) {
                found = true;
                break;
            }
            prevNode = curNode;
            curNode = curNode.next;
        }

        if(found) {
            //  deleting the node if found
            prevNode.next = curNode.next;
        }else{
            //  nothing to do because element was not found
            return;
        }

    }

    //  deleting using the index (position)
    public void deleteUsingIndex(int index) {
        /**
         * Boundary test cases
         * 1. the position must not be greater than the length of the linked list
         * 
         */

        if(index == 0){
            this.headNode = this.headNode.next;
            return;
        }

        int i = 0;
        Node ptr = this.headNode;

        while(ptr!=null && i < index-1) {
            ptr = ptr.next;
            i++;
        }

        try {
            //  when the index is valid
            Node qprt = ptr.next;
            ptr.next = qprt.next;
        } catch (Exception e) {
            //  When the index is not valid
            System.out.println("Given index is greater than the length of the linked list");
        }

    }


}


public class LinkedList {
    public static void main(String[] args) {
        LList mylist = new LList();
        mylist.insertNode(1);
        mylist.insertNode(2);
        mylist.insertNode(3);
        mylist.insertNode(4);
        
        mylist.deleteUsingIndex(4);
        mylist.traverse();

    }
}
