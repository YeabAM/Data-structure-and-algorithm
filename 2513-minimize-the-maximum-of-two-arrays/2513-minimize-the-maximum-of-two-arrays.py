class Solution:
    def possible(self, candidate,  d1, d2, cnt1, cnt2):
        cant_do_both = candidate // lcm(d1, d2)
        cant_do_first = candidate // d1
        cant_do_second = candidate // d2

        can_do_both = candidate - (cant_do_first + cant_do_second - cant_do_both)

        cnt1 = max(0, cnt1 - (cant_do_second - cant_do_both))
        cnt2 = max(0, cnt2 - (cant_do_first - cant_do_both))

        return can_do_both >= cnt1 + cnt2

    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        lo, hi = 0, 10**11
        
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if self.possible(mid,  divisor1, divisor2, uniqueCnt1, uniqueCnt2):  hi = mid                                    
            else: lo = mid                
        return hi