S=list(input())
S1=list()

for i in range(1,len(S)+1):
        S1.append(  S[len(S)-i] )

print("".join(map(str, S1)))