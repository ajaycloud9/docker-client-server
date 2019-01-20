import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 60000))
s.listen()
conn, addr = s.accept()

##Calculator
rcvd11=conn.recv(1024)
a=rcvd11.decode('ascii')

###Calculator clasis
class Calculator:

    def __init__(self,problem):
        self.problem=problem
        if '+' in self.problem:
            a,b=map(int,self.problem.split('+'))
            self.value=self.add(a,b)
        elif '-' in self.problem:
            a,b=map(int,self.problem.split('-'))
            self.value=self.substract(a,b)
        elif '*' in self.problem:
            a,b=map(int,self.problem.split('*'))
            self.value=self.multiply(a,b)
            
        elif '/' in self.problem:
            a,b=map(int,self.problem.split('/'))
            self.value=self.divide(a,b)
            
            
    def add(self,a,b):
        return a+b
    def substract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

c=Calculator(a)
print(c.value)
