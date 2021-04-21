
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




# 變量
#