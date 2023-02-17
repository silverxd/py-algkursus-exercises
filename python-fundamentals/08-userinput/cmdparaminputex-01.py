import sys

dict = {}

# launch.json <--- "args": "a b c d e f"

for i in [1,2,3]:
    print(f'#{i}')
    counteutry = sys.argv[2*i-1]
    captiltalist = sys.argv[2*i]
    dict [counteutry] = captiltalist

print(dict)