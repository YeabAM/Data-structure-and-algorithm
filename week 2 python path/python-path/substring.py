def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if string.startswith(sub_string,i):
            count+=1
    return count

if __name__ == '__main__':
