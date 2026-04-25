class Solution {
    public boolean isPalindrome(String s) {
       char[] stringChars  = s.toCharArray();
       StringBuilder sBuilder = new StringBuilder();
       for(char c : stringChars){
        if(Character.isLetterOrDigit(c)){
            sBuilder.append(c);
        }
       }

       System.out.println(sBuilder.toString());
    
       if(sBuilder.toString().equalsIgnoreCase(sBuilder.reverse().toString())){
            return true;
       }
        
        return false;
    }

}
