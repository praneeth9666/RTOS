import pexpect
import time
import threading
child_server = pexpect.spawn('./server1')
n=40
l=[]
for i in range(n):
    l.append(pexpect.spawn('./client1 8888 127.0.0.1'))
l[n-10].expect('connected')
start = time.time()
l[n-10].sendline('hello')
l[n-1].expect('hello')
end = time.time()
print((end - start)*1000)
