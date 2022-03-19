class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
#         time
#           time[i] ... time taken by the ith bus to complete 1 trip
#         each bus can make multiple trips ,,, next trip can start immed after completing current trip
#         each bus operates indep
#         totalTrips - number of trips all buses can make in total
#         minimin time required for all buses to complete at least totaltrips

        def isValid (mid):
            sumi = 0
            for i in time:
                if i > mid:
                    sumi += 0
                
                else:
                    # if mid % i == 0:
                    #     sumi += mid // i
                    sumi += (mid // i)
                     
#                 else:
#                     sumi += mid
                
               
            if sumi >= totalTrips:
                return True
            else:
                return False
            
                
        left = 1
        right = 10 ** 17
        ans = 0
       
        
        while left <= right:
            mid = left + (right - left) // 2
         
            if isValid(mid):
                right = mid - 1
                ans = mid
                
            else:
                left = mid + 1
            print(left, right)    
        return ans