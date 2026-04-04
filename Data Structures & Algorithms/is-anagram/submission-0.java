class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length())
            return false;

        if(s.isEmpty() || t.isEmpty())
            return false;

        char[] str1Char = s.toCharArray();
        char[] str2Char = t.toCharArray();

        Arrays.sort(str1Char);
        Arrays.sort(str2Char);

        if(String.valueOf(str1Char).equalsIgnoreCase(String.valueOf(str2Char))){
            return true;
        }
        return false;


    }
}
