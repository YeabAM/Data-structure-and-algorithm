class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ing = defaultdict(list)
        incoming = defaultdict(int)
        queue = deque()
        ans = []
        for i in range(len(ingredients)):
            incoming[recipes[i]] = len(ingredients[i])
            for j in range(len(ingredients[i])):
                ing[ingredients[i][j]].append(recipes[i])
                
        for i in supplies:
            queue.append(i)
        
        recipes = set(recipes)
        
        while queue:
            # print(ing)
            curr = queue.popleft()
            # print(curr)
            if curr in recipes:
                ans.append(curr)
            for n in ing[curr]:
                incoming[n] -= 1
                if incoming[n] == 0:
                    queue.append(n)
        
        return ans
                    
            
                
        
        
                