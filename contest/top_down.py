import sys, threading

def main()








threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()