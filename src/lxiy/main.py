# type 基本數據類型
# 
# Number 數字
# int 整數(其他語言有分 short, int, long)
# float 浮點數(單精度 float, 雙精度 double, 不過 py 沒有分)
type(1) # <class 'int'>
type(1 + 1) # <class 'int'>
type(2 // 2) # <class 'int'> 雙 / 除法才會返回整數(1), 整除僅取整數位
type(1.1) # <class 'float'>
type(1.1111111111111111) # <class 'float'>
type(1 + 0.1) # <class 'float'>
type(1 + 1.0) # <class 'float'>
type(2 / 2) # <class 'float'> 除法返回是 float(1.0)
#
# 補充
# 10, 2, 8, 16 進制
# 10 滿 10 進 1, e.g. 0, 1, 2, ... 9, 10, 11, ...
# 2, e.g. 0, 1, 10, 11, 100, 101, ...
# 8, e.g. 0, 1, ..., 7, 10, ...
# 16, e.g. 0, 1, 2, ..., 9, A, B, C, D, E, F, ...
0b10 # 2 (0b 表示 2 進制)
0o10 # 8 (0o 表示 8 進制)
0x10 # 16 (0x 表示 16 進制)
bin(10) # '0b1010' X 進制轉 2 進制
oct(0b111) # '0o7' X 進制轉 8 進制
int(0b10) # 2 X 進制轉 10 進制
hex(888) # '0x378' X 進制轉 16 進制
#
# bool 布林(屬於數字分類的一種)
True
False
type(True) # <class 'bool'>
int(True) # 1
int(False) # 0
bool(1) # True (非空值(0, '', [], {}, None) 都是 True)
bool(0) # False
#
# complex 複數
36j # j 表示複數
#
# str 字符串
# 單引號, 雙引號, 三引號
'hello world!'
"hello world!"
type('1') # <class 'str'>
'let\'s go'
'''hello world!
love world!''' # ''', """ 多行字符串
r'c:\north\ng' # r'', R'' 原始字符串(無視轉義字浮，故所見及所得)
"hello" + "world" # helloworld
'hello' * 3 # hellohellohello
'hello'[1] # e
'hello'[-1] # o
'hello world'[0:5] # hello
'hello world'[0:-1] # hello worl
'hello'[0:20] # hello 超過長度取到最後
'hello'[2:] # llo 2 取到末
'hello world'[:-5] # hello
len('abc') # 3
max('hello world') # w 用 ascii 判斷
min('helloWorld') # d
ord('w') # 119(ascii)



# 組
# list 列表
type([1, 2, 3]) # <class 'list'>
type([1, True, [2, 4]]) # <class 'list'> list 內可以支持多類型
['hello', 'world', 'love', 'you'][0] # 'hello'
['hello', 'world', 'love', 'you'][0:2] # ['hello', 'world']
['hello', 'world', 'love', 'you'][-1:] # ['you']
# 如果用 : 取值的話返回的是 list 不是對應的類型
['hello'] + ['world'] # ['hello', 'world']
['hello'] * 3 # ['hello', 'hello', 'hello']
3 in [1, 3, 5] # True
3 not in [2, 4, 6] # True
len([1, 3, 5]) # 3
max([1, 3, 5]) # 5
min([1, 3, 5]) # 1
[1].append(2) # [1, 2]
#
# tuple 元組
type((1, 2, 3)) # <class 'tuple'>
(1, 2, 3)
(1, 'a', True)
(1, 2)[0] # 1
(1, 2, 3)[0:2] # (1, 2)
(1, 2) + (3, 4) # (1, 2, 3, 4)
(1) * 3 # (1, 1, 1)
type((1)) # <class 'int'> 元組沒有多值，括號將僅是運算符的括號
type((1,)) # <class 'tuple'>
type(())  # <class 'tuple'>
# tuple 與 list 的區別
# 補
# 
# [:] 這稱作 slice 切片
#
# Set 集合(去重的無序組)
# 序列是有序的 但集合是"無序"的
type({1, 3, 5}) # <class 'set'>
{1, 1, 2, 3} # {1, 2, 3}
len({1, 2, 3}) # 3
1 in {1, 2, 3} # True
1 not in {1, 2, 3} # False
{1, 3, 5} - {3} # {1, 5} "-" 求兩個集合的差集
{1, 3, 5} & {3} # {3} "&" 求兩個集合的交集
{1, 3, 5} | {3, 5, 7} # {1, 3, 5, 7} "|" 求兩個集合的合集
type({}) # <class 'dict'>
type(set()) # <class 'set'> 定義空集合要使用 set()
len(set()) # 0
#
# dict 字典
# key-value、"無序"
type({}) # <class 'dict'>
type({ 'name': 'frank' }) # <class 'dict'>
{ 'name': 'frank' }['name'] # frank
{ 1: 'frank', '1': 'jeff' } # { 1: 'frank', '1': 'jeff' } key 不只能是 str，只要是不可變類型即可




# 變量
A = [1, 3, 5]
hello_world = 'hello world' # python 命名規範採 _ 而不是小駝峰
id(hello_world) # 55399200 id() 撈取該變量地址
# 常量 constant
# py 只有意義上的常量, 規範是用大駝峰來申明
HELLO_WORLD = 'hello world constant'





# 運算符
# 算數運算符
# *, /, //, %, **
3 // 2 # 1 無條件捨去
2 ** 2 # 4 2 的 2 次方
#
# 賦值運算符
# =, +=, *=, /=, %=, **=, //=
# python 沒有自增自減運算符 ++, --
#
# 比較(關係)運算符
# ==, !=, >, <, >=, <=
# 不是只有數字能比較
'b' > 'a' # True 因為字碼較大 可以使用 ord() 查看
'abc' < 'abd' # True 會將每個值取出單獨比對, a < a, b < b, c < d
[1, 2, 3] < [2, 3, 4] # True 組也可以(list, tuple)
#
# 邏輯運算符
# and, or, not
# int float 非 0 被認為是 True
not 0.1 # False
not 0 # True
# str 空字符串被認為是 False
not '' # True
not '0' # False
# 組 空列表被認為是 False
not []
True and True # True
True and False # False
True or True # True
True or False # True
# 只有 not 返回的固定是 True/False
# 不一定要用 True/False 來比較
'a' and 'b' # 'b'
'' and 'b' # ''
'a' or '' # 'a'
'' or 'a' # 'a'
#
# 成員運算符
# in, not in
1 in [1, 2, 3] # True
4 not in [1, 2, 3] # True
'h' in 'hello' # True
1 in (1, 2) # True
1 in {1, 2} # True
'a' in {'a': 1} # True 字典由 key 存在與否來判斷
#
# 身分運算符
# is, is not
1 is 1 # True
'hello' is not 'hello' # False
# is 與 == 的區別
# 如同 js 的 == 與 === 的區別 精度有別
# == 比較值相等, is 比較地址值是否相等(可由 id() 查看)
is_a = 1
is_b = 1.0
is_a == is_b # True
is_a is is_b # False

is_c = {1, 2, 3}
is_d = {2, 1, 3}
is_c == is_d # True 集合無序 所以是 True
is_c is is_d # False

is_e = (1, 2, 3)
is_f = (2, 1, 3)
is_e == is_f # False 有序會取值計算
is_e == is_f # False
#
# 類型判斷
type('hello') == int # False
type('hello') == str # True
isinstance('hello', str) # True 推薦使用 isinstance 判斷
isinstance('hello', (int, str)) # True 可以多類型判斷
#
# 位運算符 都是把數字轉二進制數進行運算
# &(按位與) |(按位或) ^(按位異或) ~(按位取反) <<(左移) >>(右移)
2 & 3 # 2, 0b10 0b11 單獨取值比較，若兩值為 1 返回 1 否則為 0, 11 > 1, 01 > 0 > 0b10 故返回 2
2 | 3 # 3, 若兩值有 1 返回 1, 11 > 1, 01 > 1 > 0b11 故返回 3
# ...




# 表達式
# 表達式(expression)是運算符(operator)和操作數(operand)所構成的序列
# 優先級
# */ 比 +- 優先, and 比 or 優先
1 or 2 and 3 # 1 實際等於 1 or (2 and 3)
# 優先級圖表
# | 1  | **                              |
# | 2  | ~, +, -                         |
# | 3  | *, /, %, //                     |
# | 4  | +, -                            |
# | 5  | >>, <<                          |
# | 6  | &                               |
# | 7  | ^, \|                           |
# | 8  | <=, <, >, >=                    |
# | 9  | <>, ==, !=                      |
# | 10 | =, %=, /=, //=, -=, +=, *=, **= |
# | 11 | is, is not                      |
# | 12 | in, not in                      |
# | 13 | not, and, or                    |
# 記不起來的話建議聒聒號讓大家都能輕易識別，如下：
(not 1) or ((1 + 2) == 3)
#
# 流程控制語句
# 條件控制 condition
if [1]:
  print('good')
elif True:
  pass # 空語句/佔位符
else:
  print('bad')




# 循環
# while
i = 0
while i < 10:
  i += 1
  print(i)
else:
  print('while end')
#
# for, for-else
fruits = ['apple', 'orange', 'banana']
for e in fruits:
  print(e)
  # 一樣有 break, continue
else:
  print('frust is gone')
#
# for range
for i in range(0, 10):
  print(i) # 0, 1, 2..., 9
for i in range(0, 10, 2):
  print(i) # 0, 2, 4..., 8
# 以上等價於以下
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list[0:len(list):2]:
  print(i) # 0, 2, 4..., 8
for i in range(0, 10, -2):
  print(i) # 10, 8, 6..., 2
