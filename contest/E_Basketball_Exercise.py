import sys, threading
def main():
    
    def selectTeam(team, index, flag):

            if index == len(team[flag]) - 1:
                return(team[flag][index], 0)

            if (index, flag) in memo:
                return memo[(index, flag)]

            team1 = selectTeam(team,index + 1, flag)
            team2 = selectTeam(team,index + 1, not flag)

            include_me = team[flag][index] + max(team1[1], team2[0], team2[1])
            exclude_me = max(team1[0], team1[1], team2[0], team2[1])

            state = (index, flag)
            memo[state] = (include_me, exclude_me)

            return memo[state]

    
    memo = {}
    sizeOfTeam = int(input())
    team = {}
    team[True] = list(map(int, input().split()))
    team[False] = list(map(int, input().split()))

    team_1 = selectTeam(team, 0, True)
    team_2 = selectTeam(team, 0, False)

    print(max(team_1[0],team_1[1],team_2[0], team_2[1]))

threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()


# from collections import defaultdict


# sizeOfTeam = int(input())
# team = defaultdict(int)
# team[] = list(map(int, input().split()))
# team[False] = list(map(int, input().split()))
# team1 = [[0,0] for _ in range(sizeOfTeam)]
# team2 = [[0,0] for _ in range(sizeOfTeam)]