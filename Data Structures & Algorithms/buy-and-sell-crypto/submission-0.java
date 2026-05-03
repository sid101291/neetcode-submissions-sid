class Solution {
    public int maxProfit(int[] prices) {
         int costPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for(int price : prices){
            if(price < costPrice){
                costPrice = price;
            }
            else{

                int currentProfit = price - costPrice;
                if(currentProfit > maxProfit){
                    maxProfit = currentProfit;
                 }
            }
            
        }
        return maxProfit;
    }
}
