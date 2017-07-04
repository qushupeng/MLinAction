# -*- coding: utf-8 -*-
'''
python 文件操作
open 函数
'''

#打开文件
'''
    file_name:文件路径+文件名（例："C:\abc.txt"）
    access_mode:文件访问模式
                r:只读，文件指针位于开头
                rb:二进制只读，文件指针位于开头
                r+:读写，文件指针位于开头
                rb+:二进制读写，文件指针位于开头
                w:写，如存在则覆盖，如不存在则创建文件
                wb:二进制写，如存在则覆盖，如不存在则创建文件
                w+:读写，如存在则覆盖，如不存在则创建文件
                wb+:二进制读写，如存在则覆盖，如不存在则创建文件
                a:追加，文件指针位于结尾，新内容在原内容之后，如不存在则创建文件
                ab:二进制追加，文件指针位于结尾，新内容在原内容之后，如不存在则创建文件
                a+:读写，文件指针位于结尾，新内容在原内容之后，如不存在则创建文件
                ab+:二进制追加，文件指针位于结尾，新内容在原内容之后，如不存在则创建文件
    buffering:缓冲区大小（buffering = 0 无寄存
                          buffering = 1 访问文件时会寄存行
                          buffering > 1 buffering为寄存区的缓冲大小
                          buffering < 0 寄存区的缓冲大小则为系统默认）
'''
fo = open(file_name [, access_mode][, buffering])

#fo对象的属性：
fo.name                 #文件名
fo.mode                 #文件访问模式
fo.softspace            #末尾是否强制加空格
fo.closed               #文件是否关闭


#方法
fo.close()              #关闭文件，之后不能再写入
#用with形式，可以不写close()方法
with open(file_name,access_mode,buffering) as fo:
    print(fo.name)                 
    print(fo.mode)                 
    print(fo.softspace)            
    print(fo.closed)               

#write()方法，将字符串写入文件，该方法无返回值
fo.write(str)

#read()方法，将size大小的字节数读出，无size则读出全部
fo.read([size])
fo.read()

#readline()方法，读取整行，包括 "\n" 字符
fo.readline([size])

'''
文件 runoob.txt 的内容如下：
1:www.runoob.com
2:www.runoob.com
3:www.runoob.com
4:www.runoob.com
5:www.runoob.com
'''

# 打开文件
fo = open("runoob.txt", "rw+")
print "文件名为: ", fo.name

line = fo.readline()
print "读取第一行 %s" % (line)

line = fo.readline(5)
print "读取的字符串为: %s" % (line)

# 关闭文件
fo.close()

'''
输出结果为：
文件名为:  runoob.txt
读取第一行 1:www.runoob.com

读取的字符串为: 2:www
'''


