class MyHashSet {
    Set<Integer>[] arr;
    public MyHashSet() {
        arr = (HashSet<Integer>[]) new HashSet[1000];
        for (int i = 0 ; i < arr.length; i++){
            arr[i] = new HashSet<Integer>();
        }
    }
    
    public void add(int key) {
        int index = key % arr.length;
        arr[index].add(key);
    }
    
    public void remove(int key) {
        int index = key % arr.length;
        arr[index].remove(key);
    }
    
    public boolean contains(int key) {
        int index = key % arr.length;
        if(arr[index].contains(key)){
            return true;
        }
        return false;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */