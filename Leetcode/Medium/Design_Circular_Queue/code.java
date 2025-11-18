

public class Node {
    private Node next;
    private int data;
    public Node(int data) {
        this.data = data;
        this.next = null;
    }

    public void setNext(Node next) {
        this.next = next;
    }
    public Node getNext() {
        return next;
    }
    public int getData() {
        return data;
    }
    public void setData(int data) {
        this.data = data;
    }
}

class MyCircularQueue {

    Node head;
    int size;
    int maxSize;

    public MyCircularQueue(int k) {
        head = null;
        size = 0;
        maxSize = k;
    }

    public boolean enQueue(int value) {
        if(isFull()){
            return false;
        }
        Node newNode = new Node(value);
        if(isEmpty()){
            head = newNode;
            newNode.setNext(head);
            size++;
            return true;
        }
        Node current = head;
        while(current.getNext() != head){
            current = current.getNext();
        }
        current.setNext(newNode);
        newNode.setNext(head);
        size++;
        return true;
    }

    public boolean deQueue() {
        if(isEmpty()){
            return false;
        }
        if( size == 1 ){
            head = null;
            size--;
            return true;
        }
        Node ptr = head;
        while(ptr.getNext() != head){
            ptr = ptr.getNext();
        }
        Node current = head;
        head = head.getNext();
        current.setNext(null);
        ptr.setNext(head);
        size--;
        return true;
    }

    public int Front() {
        if(isEmpty()){
            return -1;
        }
        return head.getData();
    }

    public int Rear() {
        if(isEmpty()){
            return -1;
        }
        Node current = head;
        while(current.getNext() != head){
            current = current.getNext();
        }
        return current.getData();
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == maxSize;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */