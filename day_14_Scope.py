#first solution i could thought
 def computeDifference(self):
        maximumDifference=[]
        for i in self.__elements[:-1]:
            for j in self.__elements[self.__elements.index(i)+1:]:
                maximumDifference.append(abs(i-j))
        self.maximumDifference=max(maximumDifference)
        return(self.maximumDifference)
      
      
#second And third possible solution, either sort the element or find min and max value

    def computeDifference(self):
        l=self.__elements
        #l=sorted(l)
        #self.maximumDifference=(abs(l[-1]-l[0])) or
        minv,maxv=min(l),max(l)
        self.maximumDifference=abs(maxv-minv)
        return(self.maximumDifference)

#the third and best solution would be take min = 100,max =1  , iterate through the loop find min and max value
class Difference:
    def __init__(self, a):
        self.__elements = a


    def computeDifference(self):
        l=self.__elements
        minv,maxv=100,1
        for x in l:
            if x>maxv:
                maxv=x
            if x<minv:
                minv=x
        self.maximumDifference=abs(maxv-minv)
        return(self.maximumDifference)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
