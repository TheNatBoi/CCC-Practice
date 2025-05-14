'''N = int(input())
array = []
maxi = 0

for i in range(N):
    array += str(input())

tempArray = array
for k in range(len(array)):
    if array[k] == "P":
        tempArray[k] = "S"
        ans = 1
        temp = 1
        for k in range(1, len(array)):        
            if (array[k] == array[k - 1]):
                temp += 1
            else:
                ans = max(ans, temp)
                temp = 1
        tempArray[k] = "P"

        ans = max(ans, temp)
        if ans >= maxi:
            maxi = ans
    else:
        pass

print(maxi)
'''

def max_consecutive_sunshine():
    import sys
    # Read input from standard input
    N = int(sys.stdin.readline())  # Number of days
    weather = [sys.stdin.readline().strip() for _ in range(N)]  # Weather data

    left = 0  # Left pointer of the sliding window
    max_length = 0  # Maximum length of consecutive S days
    p_count = 0  # Count of P days in the current window

    # Iterate through the sequence using the right pointer
    for right in range(N):
        if weather[right] == 'P':
            p_count += 1

        # If there are more than one P in the window, move the left pointer
        while p_count > 1:
            if weather[left] == 'P':
                p_count -= 1
            left += 1

        # Update the maximum length
        max_length = max(max_length, right - left + 1)

    # Write the result to standard output
    print(max_length)

# Call the function
max_consecutive_sunshine()