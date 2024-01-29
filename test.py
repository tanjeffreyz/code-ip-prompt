from jplag import jplag_score_func

print(jplag_score_func('test/prog1.py', 'test/prog2.py', 'python'))


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
