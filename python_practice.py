# 这是一些关于PYTHON编程的练习，你可以直接在题目后面写出代码。

# 1. 找出下面两个数组的公共部分并打印出来
a = [1, 1, 2, 3, 5, 8, 15, 21, 34, 56, 86]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
same=[x for x in a if x in b]
print(same)
#
# 2. 将数组里重复的数字除去。打印出最后结果。
list1 = [1, 1, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14]
new=[]
for a in list1:
  i=0
  j=0
    for i in range(len(new)):
      if new[i]==a:
        j=1
          break
    if(j==0):
      new.append(a)
print(new)
#
# 3. 统计下面的数列，用MAP格式打印出各个水果有几个。

#
# 4. 在test项目目录中打开一个名为test.txt的文件，在已有文字后面，写入"hello world"。如果找不到文件，本地创建一个同名新文件。

#
# 5. 用户指定一个数列，可以将1-10内数字英文单词变换成相应数字， 例如 [one, three, two, five, six] -> [1, 3, 2, 5, 6]

# 6. 将给定数组里的数，分成奇数和偶数两个数列，分别打印出来。例如 [1,3,4,5,7,8,9,11,20] -> [1,3,5,7,9,11] [4,8,20]
def splitevenodd(A):
  even=[]
  odd=[]
  for i in A:
    if (i%2==0):
      even.append(i)
    else:
      odd.append(i)
   
  print(even)
  print(odd)
#
# 7. 给定一段话，找出最高频的那个单词。例子中的 music.
# 'I mean, think about music. Music is all about repetition and patterns. If you didn’t have repetition in music, it would all just be noise.'

# 8. 按照数字大小顺序排列 ["1","11","3","22","32","4","2","201"]
