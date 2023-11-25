# 1. counters

from collections import counter

cnt = counter()
for word in ["red","blue","green","red","yellow","blue"]:
    cnt[word]+=1
print(cnt)