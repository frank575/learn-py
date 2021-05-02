import p1
import sub_a.p3
import sub_a.p3 as p3
from sub_a.p3 import b
from sub_a import p3

print(p1.a) # 1
print(sub_a.p3.b) # 2
print(p3.b) # 2
print(b) # 2