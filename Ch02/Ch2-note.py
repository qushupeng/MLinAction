# -*- coding: utf-8 -*-
'''
python �ļ�����
open ����
'''

#���ļ�
'''
    file_name:�ļ�·��+�ļ���������"C:\abc.txt"��
    access_mode:�ļ�����ģʽ
                r:ֻ�����ļ�ָ��λ�ڿ�ͷ
                rb:������ֻ�����ļ�ָ��λ�ڿ�ͷ
                r+:��д���ļ�ָ��λ�ڿ�ͷ
                rb+:�����ƶ�д���ļ�ָ��λ�ڿ�ͷ
                w:д��������򸲸ǣ��粻�����򴴽��ļ�
                wb:������д��������򸲸ǣ��粻�����򴴽��ļ�
                w+:��д��������򸲸ǣ��粻�����򴴽��ļ�
                wb+:�����ƶ�д��������򸲸ǣ��粻�����򴴽��ļ�
                a:׷�ӣ��ļ�ָ��λ�ڽ�β����������ԭ����֮���粻�����򴴽��ļ�
                ab:������׷�ӣ��ļ�ָ��λ�ڽ�β����������ԭ����֮���粻�����򴴽��ļ�
                a+:��д���ļ�ָ��λ�ڽ�β����������ԭ����֮���粻�����򴴽��ļ�
                ab+:������׷�ӣ��ļ�ָ��λ�ڽ�β����������ԭ����֮���粻�����򴴽��ļ�
    buffering:��������С��buffering = 0 �޼Ĵ�
                          buffering = 1 �����ļ�ʱ��Ĵ���
                          buffering > 1 bufferingΪ�Ĵ����Ļ����С
                          buffering < 0 �Ĵ����Ļ����С��ΪϵͳĬ�ϣ�
'''
fo = open(file_name [, access_mode][, buffering])

#fo��������ԣ�
fo.name                 #�ļ���
fo.mode                 #�ļ�����ģʽ
fo.softspace            #ĩβ�Ƿ�ǿ�Ƽӿո�
fo.closed               #�ļ��Ƿ�ر�


#����
fo.close()              #�ر��ļ���֮������д��
#��with��ʽ�����Բ�дclose()����
with open(file_name,access_mode,buffering) as fo:
    print(fo.name)                 
    print(fo.mode)                 
    print(fo.softspace)            
    print(fo.closed)               

#write()���������ַ���д���ļ����÷����޷���ֵ
fo.write(str)

#read()��������size��С���ֽ�����������size�����ȫ��
fo.read([size])
fo.read()

#readline()��������ȡ���У����� "\n" �ַ�
fo.readline([size])

'''
�ļ� runoob.txt ���������£�
1:www.runoob.com
2:www.runoob.com
3:www.runoob.com
4:www.runoob.com
5:www.runoob.com
'''

# ���ļ�
fo = open("runoob.txt", "rw+")
print "�ļ���Ϊ: ", fo.name

line = fo.readline()
print "��ȡ��һ�� %s" % (line)

line = fo.readline(5)
print "��ȡ���ַ���Ϊ: %s" % (line)

# �ر��ļ�
fo.close()

'''
������Ϊ��
�ļ���Ϊ:  runoob.txt
��ȡ��һ�� 1:www.runoob.com

��ȡ���ַ���Ϊ: 2:www
'''


