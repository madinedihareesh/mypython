# sytanx: open('name of the file with exction','mode')
# properties:1.name2.mode3.closed
# r-read,w-write,a-append,r+-read+write,w+write+read,rb-readbinary,wb-witebinary

# file_handle=open('Demo.txt','r')
# str1=file_handle.readlines()
# for x in str1:
#     print(x,end='')

# file_handle.close()

# handle=open('Memo.txt','w')
# handle.write('Hi hello how are you') 
# str2=['\nare you doing good\n','i am doing grate\n','how is your life going on\n'] 
# handle.writelines(str2) 
# handle.close() 
# print(handle.name)
# print(handle.mode)
# print(handle.closed)

# readingfile=open('Memo.txt','r')
# str3=readingfile.read()
# print(str3)

file=open('python1.jpeg','rb')
data=file.read()
file.close()

file1=open('python2.jpeg','wb')
file1.write(data)
file1.close()

