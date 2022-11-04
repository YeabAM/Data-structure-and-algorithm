class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingFor = defaultdict(list)
        amountOfIng = defaultdict(int)
        totalRec = set()
        
        #calculate incoming of each recipes
        for i in range(len(ingredients)):
            amountOfIng[recipes[i]] = len(ingredients[i])
        
        #build graph from ingredinet to recipe
        for j in range(len(recipes)):
            for ingr in ingredients[j]:
                ingFor[ingr].append(recipes[j])
                
        print(ingFor)
        queue = deque(supplies)
        
        while queue:
            curr = queue.popleft()
            totalRec.add(curr) 
            # print(curr)
            for recipe in ingFor[curr]:
                # print(recipe)
                amountOfIng[recipe] -= 1
            
                if amountOfIng[recipe] == 0:
                    queue.append(recipe)
                
        # print(totalRec)         
        return [rec for rec in recipes if rec in totalRec]
                
                
                
            
            
        