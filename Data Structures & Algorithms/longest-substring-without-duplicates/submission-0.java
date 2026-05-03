class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0; int right = 0;
        Set<Character> window = new HashSet<>();

        char[] elements  = s.toCharArray();

        int maxWindowSize = 0;

        for(char c : elements){
            // keep growing the window unless a duplicate is found
            
            if(!window.contains(c)){
                window.add(c);
                right++;
                int currentSize = right - left;
                if(currentSize > maxWindowSize){
                    maxWindowSize = currentSize;
                }
            }

            //if duplicate is found
            else{

                int currentWindowSize = right - left;
                if(currentWindowSize > maxWindowSize){
                    maxWindowSize = currentWindowSize;
                }
                while(window.contains(c)){
                    window.remove(elements[left]);
                    left++;
                }

                window.add(c);
                right++;
            }
        }

        return maxWindowSize;
    }
}
