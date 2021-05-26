class PlayWithList:
    
    
    def __init__(self, lst=[0,5,7,6,4,8,9,10,-4,-1,-11]):
        self.lst = lst
    
    
    def return_max(self):
        return max(self.lst)
    
    def return_min(self):
        return min(self.lst)
    
    def return_max_sequared(self):
        return max(self.lst)**2
    
    def return_length(self):
        return len(self.lst)
    
    def return_positive_sum(self):
        lst = self.lst
        sum=0
        for i in lst:
            if i > 0:
                sum +=i
                  
        return sum
    
    def return_negative_count(self):
        lst = self.lst
        count=0
        for i in lst:
            if i < 0:
                count +=1
        return count
    
    def reverse(self):
        rev = []
        lst = self.lst

        lenth = len(self.lst)
        y = lenth/2
        for i in range(lenth-1,-1,-1):
            rev.append(lst[i])
                
        msg1 = f"The oraginal list : {lst}"
        msg2 = f"The reverse list  : {rev}"
        return f"{msg1}\n{msg2}" 
    
    def multiply(self,num=1):
        lst = self.lst
        mult = []
        
        for i in range(0,len(lst)):
            mult.append(lst[i]*num)

        return mult