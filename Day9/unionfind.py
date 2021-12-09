"""
Union-Find type functions.
"""

class UnionFind:

    def __init__(self, union_func=lambda a, b: a, starter_set=[]):
        """
        union_func is the function that determines which element gets picked in a union.
        """
        self.parent = {}
        self.union_func = union_func
        for item in starter_set: self.makeset(item)
        pass

    def makeset(self, n):
        self.parent[n] = n
        pass

    def find(self, n):  # path-splitting algorithm
        while self.parent[n] != n:
            nxt = self.parent[n]
            self.parent[n] = self.parent[nxt]
            n = nxt
        return n

    def union(self, a, b):
        """
        Returns True if root(a) already equaled root(b),
        False otherwise
        """
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root == b_root: return True

        # determine which root is being pointed to now
        new_a_root = self.union_func(a_root, b_root)

        if new_a_root == a_root:
            new_b_root = b_root
        elif new_a_root == b_root:
            new_b_root = a_root
        else:
            raise Exception("UNION-FUNC DID NOT RETURN " + str(a) + " OR " + str(b) + "!!!!")

        # (a_root, b_root) = #(min(a_root, b_root), max(a_root, b_root))
        self.parent[new_b_root] = new_a_root
        return False


class UnionFindSize(UnionFind):

    def __init__(self, union_func=lambda a, b: a, starter_set=[]):
        """
        union_func is the function that determines which element gets picked in a union.
        """

        ## DO NOT access this directly...use get_size
        self.size = {}  # size only valid while parent is valid
        super().__init__(union_func, starter_set)
        pass

    def get_size(self, n):
        return self.size[self.find(n)]

    def makeset(self, n):
        super().makeset(n)
        self.size[n] = 1

    def union(self, a, b):
        """
        Returns True if root(a) already equaled root(b),
        False otherwise
        """
        a_size = self.get_size(a)
        b_size = self.get_size(b)
        ans = super().union(a, b)
        if not ans:
            self.size[self.find(a)] = a_size + b_size
        return ans
