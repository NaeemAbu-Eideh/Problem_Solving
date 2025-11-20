class Solution {
    public boolean isSame(String s ,int n1, int n2){

            if(n1 >= n2){
                return true;
            }

            if(s.charAt(n1) != s.charAt(n2)){
                return false;
            }
            return isSame(s ,++n1, --n2);
            
        }
    public boolean isPalindrome(String s) {
        String s2 = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int i = 0;
        int j = s2.length() -1;
    
        return isSame(s2 ,i, j);
    }
}
