# 01
from collections import Counter
text="banana"
count=Counter(text)
print(count)

# 02
from collections import deque
dq=deque([1,2,3,4])
dq.append(5)
dq.appendleft(0)
dq.append(6)
print(dq)
dq.pop()
dq.popleft()
print(dq)

# 03
from collections import defaultdict
stud=defaultdict(int)
print(stud["marks"])

# 04
from collections import namedtuple
student=namedtuple("student",["name","age"])
s1 = student("Mahek",21)

print(s1.name)
print(s1.age)