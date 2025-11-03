class Node{
    private int value;
    private int key;
    public Node(int value, int key){
        setValue(value);
        setKey(key);
    }
    public Node(){
        setValue(0);
        setKey(-1);
    }
    public void setValue(int value){
        this.value = value;
    }
    public void setKey(int key){
        this.key = key;
    }
    public int getValue(){
        return value;
    }
    public int getKey(){
        return key;
    }
}


class MyHashMap {

    ArrayList<Node>[] arr ;

    public MyHashMap() {
        arr = new ArrayList[1000];
        for(int i = 0 ; i < arr.length; i++){
            arr[i] = new ArrayList<Node>();
        }
    }
    
    public void put(int key, int value) {
        int index = key % arr.length;
        for(int i = 0; i < arr[index].size(); i++){
            if(key == arr[index].get(i).getKey()){
                arr[index].get(i).setValue(value);
                return;
            }
        }
        Node node = new Node(value, key);
        arr[index].add(node);
    }
    
    public int get(int key) {
        int index = key % arr.length;
        int value = 0;
        for(Node node : arr[index]){
            if(key == node.getKey()){
                return node.getValue();
            }
        }
        return -1;
    }
    
    public void remove(int key) {
        int index = key % arr.length;
        int value = 0;
        for(int i = 0 ; i < arr[index].size(); i++){
           if(key == arr[index].get(i).getKey()){
            arr[index].remove(i);
           }
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */