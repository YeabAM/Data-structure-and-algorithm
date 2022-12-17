class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i=0
        ans=0
        st=[]
        for i in range(len(tokens)):
            #print(st)
            try:    # to find that the current is int or not
                x=int(tokens[i])
                st.append(x)
            except:   # not int then
                b=st.pop()
                a=st.pop()
                if tokens[i]=="/": st.append(int(a/b))
                elif(tokens[i]=="*"):st.append(a*b)
                elif(tokens[i]=="+"):st.append(a+b)
                else:st.append(a-b)
        return st.pop()