import subprocess
from jplag import jplag_score_func

PATH1 = 'test/prog1.py'
PATH2 = 'test/prog2.py'

jplag_score = jplag_score_func(PATH1, PATH2 , 'python')
print('jplag:', jplag_score)

dolos_result = subprocess.run(["node", "dolos_score.js", PATH1, PATH2], stdout=subprocess.PIPE)
# print(dolos_result.stdout.decode())
dolos_score = dolos_result.stdout.decode().split("Similarity: ")[1].replace("\n", "")
print('dolos:', dolos_score)

"""
# Test for minimum program length
with open('test/prog2.py', 'r') as file:
    prog2 = file.read()
words2 = prog2.split(' ')

lo = 0
hi = 2000
while lo < hi:
    mid = (lo + hi) // 2
    with open('test/prog1.py', 'w') as file:
        file.write(' '.join(words2[:mid]))
    if jplag_score_func('test/prog1.py', 'test/prog2.py', 'python') > 0:
        hi = mid
    else:
        lo = mid + 1
print(lo)
"""
