def main():
    logSize = int(input())
    room = set()
    capacity = 0
    for _ in range(logSize):
        stat, person = input().split()

        if stat == '+':
            room.add(person)

            if len(room) > capacity:
                capacity = len(room)

        else:
            if person in room:
                room.remove(person)

            else:
                capacity += 1

    print(capacity)

            
main()
















