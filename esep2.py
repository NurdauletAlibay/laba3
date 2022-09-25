A=int(input())
B=int(input())
 
if A<B:                             #A<B өсу бойынша көрсетіледі
    for i in range(A, B+1):
        print(i)
else:                               #B<A кему бойынша
    for i in reversed(range(B, A+1)):
        print(i)