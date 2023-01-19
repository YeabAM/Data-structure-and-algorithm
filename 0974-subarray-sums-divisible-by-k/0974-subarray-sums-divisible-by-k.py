class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        modulo_count = defaultdict(int)
        modulo_count[0] = 1
        count = 0
        cur_tot = 0
        # modulo_count[cur_tot % k] += 1
        
        for i in range(len(nums)):
            cur_tot += nums[i]
            remain_total = cur_tot % k
            count += modulo_count[remain_total]
            modulo_count[remain_total] += 1   
            
            
        return count
            
            
            
            
        