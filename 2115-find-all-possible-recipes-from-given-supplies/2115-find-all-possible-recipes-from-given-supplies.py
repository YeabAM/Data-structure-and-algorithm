class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recFor = defaultdict(list)
        amountOfRec = defaultdict(int)
        totalRec = set()
        
        for i in range(len(ingredients)):
            amountOfRec[recipes[i]] = len(ingredients[i])
            
        for j in range(len(recipes)):
            for ingr in ingredients[j]:
                recFor[ingr].append(recipes[j])
                
        # print(recFor)
        queue = deque(supplies)
        
        while queue:
            curr = queue.popleft()
            totalRec.add(curr) 
            # print(curr)
            for recipe in recFor[curr]:
                # print(recipe)
                amountOfRec[recipe] -= 1
            
                if amountOfRec[recipe] == 0:
                    queue.append(recipe)
                
        # print(totalRec)         
        return [rec for rec in recipes if rec in totalRec]
                
                
                
            
            
        