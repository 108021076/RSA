import random as rand
import sys

class RSA:
    def __init__(self):
        print("q and p")
        print(self.radList())
        self.p,self.q = map(int,input().split())
        self.N = self.q * self.p
        self.N1 = (self.p - 1) * (self.q - 1)
        print("e :")
        print(self.repr(self.N1))
        self.e = int(input())
        print("d")
        print(self.findd(self.N1,self.e))
        self.d = int(input())
        print("M :")
        self.m = int(input())
        print("encrypt")
        self.c = self.encrypt(self.m,self.e, self.N)
        print(self.c)
        print("decrypt")
        print(self.decrypt(self.c,self.d , self.N))
        print("N :")
        print(self.N)
        print("N1 :")
        print(self.N1)
        print("e :")
        print(self.e)
        print("d :")
        print(self.d)
        print("p :")
        print(self.p)
        print("q :")
        print(self.q)
    def encrypt(self,msg , e , n):
        c = msg ** e % n   
        return c
    def decrypt(self,c,d,n):
        dd = c ** d % n
        return dd
    def radList(self):
        data = []
        while(True):
            n = rand.randint(2,1000)
            if self.isPrime(n):
                data.append(n)   
            if(len(data) == 5):
                break
        return data
    def isPrime(self,x):
        ipr = True
        i = 2 
        while i < x//2:
            if x%i == 0:
                ipr = False
                break
            i = i + 1
        return ipr
    def findd(self , N1, e):
        dataNE = []
        o = 0
        d = 2
        while(True):
            if (e * d) % N1 == 1 % N1:
                dataNE.append(d)
                o = o + 1
            if o == 5:
                break
            d = d+1
            print(d)
            print(dataNE)
        return dataNE
    def repr(self,N1):
        #rp = True
        #maxVal = max(N1,e)
        #minVal = min(N1,e)
        #i = 2
        #for i in range(maxVal/2):
        #    if(maxVal % i == 0):
        #        if(minVal % i == 0):
        #            rp = False
        #return rp
        dataT = []
        i = 0
        c = 2
        while i < 5:
            n = rand.randint(2,1000)
            maxVal = max(N1,n)
            minVal = min(N1,n)
            flag = True
            while c < maxVal/2:
                if maxVal % c == 0 and minVal % c == 0:
                    flag = False
                    break
                c = c + 1
            if flag == True:
                dataT.append(n)
                i = i+1
        return dataT
if __name__ == '__main__':
    rsa = RSA()
