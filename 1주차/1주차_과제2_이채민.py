import sys
input = sys.stdin.readline

word = input().rstrip()
suffixes = [word[w:] for w in range(len(word))]
print(*sorted(suffixes), sep="\n")
