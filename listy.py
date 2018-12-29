Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> nums=[]
>>> #list operations
>>> nums=[10,20,3,0,25]
>>> nums
[10, 20, 3, 0, 25]
>>> names=["vikas","sachin","raju"]
>>> names
['vikas', 'sachin', 'raju']
>>> values=[25,"sachin Tendulakar",2.5]
>>> values
[25, 'sachin Tendulakar', 2.5]
>>> mils=["nums","names","values"]
>>> mils
['nums', 'names', 'values']
>>> mil=[nums,names,values]
>>> mil
[[10, 20, 3, 0, 25], ['vikas', 'sachin', 'raju'], [25, 'sachin Tendulakar', 2.5]]
>>> mil.append("kohali")
>>> mil
[[10, 20, 3, 0, 25], ['vikas', 'sachin', 'raju'], [25, 'sachin Tendulakar', 2.5], 'kohali']
>>> mil.insert(2,"anushka")
>>> mil
[[10, 20, 3, 0, 25], ['vikas', 'sachin', 'raju'], 'anushka', [25, 'sachin Tendulakar', 2.5], 'kohali']
>>> mil.remove(nums)
>>> mil
[['vikas', 'sachin', 'raju'], 'anushka', [25, 'sachin Tendulakar', 2.5], 'kohali']
>>> mil.pop()
'kohali'
>>> mil.pop(0)
['vikas', 'sachin', 'raju']
>>> del mil(3)
SyntaxError: can't delete function call
>>> del mil[1:1]
>>> mil'
SyntaxError: EOL while scanning string literal
>>> mil
['anushka', [25, 'sachin Tendulakar', 2.5]]
>>> mil
['anushka', [25, 'sachin Tendulakar', 2.5]]
>>> mil.extend(["sachinss",2.0,1200])
>>> mil
['anushka', [25, 'sachin Tendulakar', 2.5], 'sachinss', 2.0, 1200]
>>> min(mil)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    min(mil)
TypeError: '<' not supported between instances of 'list' and 'str'
>>> min(values)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    min(values)
TypeError: '<' not supported between instances of 'str' and 'int'
>>> min(nums)
0
>>> max(nums)
25
>>> sum(nums)
58
>>> mil.sort()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    mil.sort()
TypeError: '<' not supported between instances of 'list' and 'str'
>>> nums.sort()
>>> nums
[0, 3, 10, 20, 25]
>>> 
