class Solution {
    public int[] twoSum(int[] nums, int target) {

        int[] arr = new int[2];

        Map<Integer,Integer> elementIndices = new HashMap<>();
        
        for(int i = 0; i < nums.length ; i++){

            int difference = target - nums[i];
            
            if(elementIndices.containsKey(difference)){
                arr[1] = i;
                arr[0] = elementIndices.get(difference);
                return arr;
            }
            else{
                elementIndices.put(nums[i],i);
            }
        }
        
        return null;
    }
        
    
}
