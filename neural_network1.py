import math
def LeakyReLU_Function(x,u):
    m = 0
    if x > 0:
        m = x
    else:
        m = u*x
    return m

def Softplus_Function(x):
    m = 0
    m = math.log((1+math.exp(x)) , 2.7182)
    return m

a = int(input("please enter a:\n"))
b = int(input("please enter b:\n"))
c = int(input("please enter c:\n"))
d = int(input("please enter d:\n"))

a1 = 0
b1 = 0
c1 = 0
d1 = 0
e1 = 0

a1 = LeakyReLU_Function(a,0.01)+LeakyReLU_Function(b,0.2)+LeakyReLU_Function(c,0.05)+LeakyReLU_Function(d,0.5)
b1 = LeakyReLU_Function(a,0.1)+LeakyReLU_Function(b,0.012)+LeakyReLU_Function(c,1.15)+LeakyReLU_Function(d,0.6)
c1 = LeakyReLU_Function(a,1.02)+LeakyReLU_Function(b,0.6)+LeakyReLU_Function(c,0.3)+LeakyReLU_Function(d,0.52)
d1 = LeakyReLU_Function(a,0.2)+LeakyReLU_Function(b,0.5)+LeakyReLU_Function(c,0.09)+LeakyReLU_Function(d,0.35)
e1 = LeakyReLU_Function(a,0.03)+LeakyReLU_Function(b,0.8)+LeakyReLU_Function(c,0.26)+LeakyReLU_Function(d,0.12)

a2 = 0
b2 = 0
c2 = 0

a2 = 5.68 * (Softplus_Function(a1)+Softplus_Function(b1)+Softplus_Function(c1)+Softplus_Function(d1)+Softplus_Function(e1))
b2 = 7.11 * (Softplus_Function(a1)+Softplus_Function(b1)+Softplus_Function(c1)+Softplus_Function(d1)+Softplus_Function(e1))
a2 = 9.85 * (Softplus_Function(a1)+Softplus_Function(b1)+Softplus_Function(c1)+Softplus_Function(d1)+Softplus_Function(e1))

output = 0
output = 2.03*a2 + 0.867*b2 + 1.75*c2
print('The output is:',output)



