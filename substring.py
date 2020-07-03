
def count_substring(string, sub):
    # Append 1 to the list every time match is found
    count = [1 for i in range((len(string) - len(sub) + 1)) if ((string[i:i+len(sub)]) == sub)]
    count = sum(count) # Perform sum of the elements of the list
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
