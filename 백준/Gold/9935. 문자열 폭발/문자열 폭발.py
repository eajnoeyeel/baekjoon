import sys
input = sys.stdin.readline


def main():
    haystack = input().strip()
    needle = list(input().strip())
    needle_len = len(needle)
    stack = []

    for char in haystack:
        stack.append(char)

        if len(stack) >= needle_len and stack[-needle_len:] == needle:
            for _ in range(needle_len):
                stack.pop()
    
    result = "".join(stack)
    if result:
        print(result)
    else:
        print("FRULA")


if __name__ == "__main__":
    main()