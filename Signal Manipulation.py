#A signal is represented in this program as an array of numbers when its first index is corresponding to a special index of the n variable in the signal. 
#For example, let's take signal x(n) that is defined like this:
#x[-2]=1, x[-1]=2, x[0]=0, x[1]=-1, and for every other n: x[n]=0
#The signal x[n] is represented in this code as a tuple in this form: ( [1,2,0,-1] , -2  ) (first object in tuple is array, second is integer)
#Note: You can tell that only specific signals can be written in this format (must be a finite amount of signal values that are non-zero)
import numpy as np
import matplotlib.pyplot as plt


def main():
     N=12
     choice=input("Please choose your wanted function:\n1- Compute Signal\n2- Flip Signal\n3- Scale Signal\n4-Add Signals\n5- Display Signal\n6- Decompose two Even and Odd Signals\n")
     if (choice=='1'):
        x=GetSignal()
        n=int(input("Please enter wanted n to get the x[n] value\n"))
        print("The wanted x["+str(n)+"] is "+str(computeSignal(x,n)))
        DisplaySignal(x,N)
     elif (choice=='2'):
        x=GetSignal()
        DisplaySignal(x,N)
        res=FlipSignal(x)
        print("The new signal is:\n")
        DisplaySignal(res,N)
     elif (choice=='3'):
          x=GetSignal()
          DisplaySignal(x,N)
          scalar=int(input("Please enter a scalar\n"))
          res=ScaleSignal(scalar,x)
          print("The new signal scaled by "+ str(scalar) + " is:\n")
          DisplaySignal(res,N)
     elif (choice=='4'):
         x1=GetSignal()
         x2=GetSignal()
         DisplaySignal(x1,N)
         DisplaySignal(x2,N)
         res=AddSignals(x1,x2)
         print("The signal (x1+x2)[n] is:\n")
         DisplaySignal(res,N)
     elif (choice=='5'):
         x=GetSignal()
         DisplaySignal(x,N)
     elif (choice=='6'):
         x=GetSignal()
         DisplaySignal(x,N)
         evenSignal,oddSignal=Decompose2EvenOdd(x)
         print("Even Signle:\n")
         DisplaySignal(evenSignal,N)
         print("Odd Signal:\n")
         DisplaySignal(oddSignal,N)

def GetSignal():
    value=input("Please type the signal values (terminate by 'E')\n")
    lst=[]
    while (value!='E'):
        lst.append(int(value))
        value=input()
    value=input("Please type the index of the first object in the array\n")
    return (lst,int(value))

def Decompose2EvenOdd(x):
    xOfNegativeN=FlipSignal(x)
    negativeXOfNegativeN=ScaleSignal(-1,xOfNegativeN)
    EvenSignal= AddSignals(x,xOfNegativeN)
    EvenSignal=ScaleSignal(0.5, EvenSignal)
    OddSignal=AddSignals(x,negativeXOfNegativeN)
    OddSignal=ScaleSignal(0.5, OddSignal)

    return EvenSignal,OddSignal



def DisplaySignal(x,N):
    arr, index = x
    x = range(index, index + len(arr))
    y = arr
    markerline, stemline, baseline = plt.stem(x, y, use_line_collection=True, linefmt='C0-', markerfmt='C3o', basefmt='k-')
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.setp(markerline, markersize=8)
    plt.setp(stemline, linewidth=1)
    plt.setp(baseline, linewidth=0.5)
    plt.xlim([-N, N])
    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.title('Signal Graph')
    plt.show()
    



def AddSignals(x1,x2):
     difference=x1[1]-x2[1]
     if (difference>0):
        minSignalArr=list(x2[0])
        maxSignalArr=list(x1[0])
        minIndex=x2[1]
     else:
        minSignalArr=list(x1[0])
        maxSignalArr=list(x2[0])
        minIndex=x1[1]
     startAbsDiff=abs(difference)
     for i in range(startAbsDiff):
         maxSignalArr.insert(0,0)
     endDiff=len(maxSignalArr)-len(minSignalArr)
     if (endDiff<0):
         temp=list(maxSignalArr)
         maxSignalArr=list(minSignalArr)
         minSignalArr=list(temp)
     endAbsDiff=abs(endDiff)
     for i in range(endAbsDiff):
        minSignalArr.append(0)

     return (sumTwoLists(minSignalArr,maxSignalArr),minIndex)

     
def sumTwoLists(lst1,lst2):
    resLst=[]
    for i in range(len(lst1)):
        resLst.append(lst1[i]+lst2[i])
    
    return resLst

 
            
    



def ScaleSignal(c,x):
    return (np.multiply(x[0],c).tolist(),x[1])


def FlipSignal(x):
    numList=x[0]
    countValsFromLeft=abs(x[1])
    countValsFromRight=len(numList)-countValsFromLeft-1
    difference=countValsFromLeft-countValsFromRight
    newFirstIndex=x[1]+difference
    flippedList=(np.flip(numList)).tolist()
    return (flippedList,newFirstIndex)


def computeSignal(x,n):
    #parametrs: x is a pair, x=(int array, int), n is an int
    #returns int
    stepsToMove=-x[1]+n
    if  (len(x[0])>stepsToMove and stepsToMove>=0):
         return (x[0][stepsToMove])
    else:
        return 0


if __name__ == "__main__":
    main()







