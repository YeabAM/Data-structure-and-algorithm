class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # first populate an adjacency list
        links = defaultdict(list)
        for a, b in edges:
            links[a].append(b)
            links[b].append(a)

        # group the nodes by value
        by_value = defaultdict(list)
        for n, val in enumerate(vals): by_value[val].append(n)

        # shortcut if all values are the same or all different
        if len(by_value) == len(vals):
            return len(vals)
        elif len(by_value) == 1:
            return len(vals)*(len(vals)+1)//2
            
        # this will track our disjoint sets
        parent = list(range(len(vals)))

        # finds the 'ancestor' of n, optimising the paths as it goes
        def ancestor(n):
            while parent[n] != n:
                n, parent[n] = parent[n], parent[parent[n]]
            return n

        # merges two sets together
        def merge(a, b):
            aa, ab = ancestor(a), ancestor(b)
            parent[max(aa, ab)] = min(aa, ab)

        # now work through the nodes in order of increasing value
        paths = 0
        for val, nodes in sorted(by_value.items()):
            # for each node, merge together it and any linked sets
            # which have value no higher than it
            for n in nodes:
                for nn in links[n]:
                    if vals[nn] <= val:
                        merge(n, nn)
            # now count how many nodes are in each set
            groups = defaultdict(int)
            for n in nodes:
                groups[ancestor(n)]+=1
            # use the sizes of these groups to update path count
            paths += sum(k*(k+1)//2 for k in groups.values())

        return paths