class LFUCache:
    def __init__(self, capacity: int):
        self.freq=[] #(ordering,k)
        self.val=[] #(k,v,f,t)
        self.time=0
        self.cap=capacity
    def add_freq(self,idx,value):
        #update the (idx-1)th item in the ordering list 
        old_tf = self.val[idx-1][2]*1000000+self.val[idx-1][3]
        self.val[idx-1][1]=value
        self.val[idx-1][2]+=1
        self.val[idx-1][3] = self.time
        new_tf = self.val[idx-1][2]*1000000+self.val[idx-1][3]

        idx_tf = bisect.bisect(self.freq,-old_tf,key = lambda x:x[0])
        self.freq.pop(idx_tf-1)
        bisect.insort(self.freq,(-new_tf,self.val[idx-1][0]),key = lambda x:x[0])
    def get(self, key: int) -> int: 
        if self.cap ==0:
            return -1
        self.time+=1

        idx = bisect.bisect(self.val,key,key = lambda x:x[0])
        if idx > 0 and self.val[idx-1][0]==key:#exist
            self.add_freq(idx,self.val[idx-1][1])
            return self.val[idx-1][1] 
        return -1

    def put(self, key: int, value: int) -> None:
        if self.cap ==0:
            return
        self.time+=1

        idx = bisect.bisect(self.val,key,key = lambda x:x[0])
        if idx > 0 and self.val[idx-1][0]==key:#exist
            self.add_freq(idx,value)
        else:
            bisect.insort(self.val,[key,value,1,self.time],key = lambda x:x[0])
            new_tf = 1*1000000+self.time
            # remove last
            if len(self.freq)==self.cap:
                k = self.freq[-1][1]
                self.freq.pop(-1)
                idx = bisect.bisect(self.val,k,key = lambda x:x[0])
                self.val.pop(idx-1)
            bisect.insort(self.freq,(-new_tf,key),key = lambda x:x[0])