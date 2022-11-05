from functools import lru_cache
import sys, threading

def main():
    letter = list(input())
    @lru_cache(None)
    def dp(idx, isDown):
        if idx == len(letter) - 1:
            if isDown:
                return int(letter[idx].isupper())
            else:
                return 0

        if isDown:
            if letter[idx].islower():
                return dp(idx+1, isDown)
            else:
                return 1 + dp(idx+1,isDown)

        else:
            if letter[idx].islower():
                opt1 = dp(idx+1, True)
                opt2 = 1 + dp(idx+1, isDown)

                return min(opt1, opt2)
            
            else:
                return dp(idx+1, isDown)


    minOps = dp(0, False)
    print(minOps)


threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()