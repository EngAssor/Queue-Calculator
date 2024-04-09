class DD:
    ti=0
    lamda=0.0
    meo=0.0
    k=0
    def get_big_ti(self,lamda,meo,k):
     ti =int(((lamda*k)+meo)/((lamda**2)-(lamda*meo)))
     return ti
    def littel_ti(self):
         big_ti=get_big_ti(self.lamda,self.meo,self.k)
         right_term= int(big_ti * lamda)
         left_term= int((self.meo*big_ti)-(self.meo*self.lamda))
         x= false
         while x is false:
             ti_try=right_term-left_term
                if ti_try == k:
                    x=false
                    big_ti=big_ti -(1/lamda)
                elif:
                    x true
                    return big_ti+(1/lamda)
    def Numbre_of_custemers(self,)





t=DD()
s=t.get_big_ti(0.25,0.1666667,5)
print(s)


