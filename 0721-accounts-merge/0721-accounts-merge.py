class DisjointSet:
    def __init__(self, n):
        self.parent = [0] * (n + 1)
        for i in range(len(self.parent)):
            self.parent[i] = i
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)
    
    def find_par(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find_par(self.parent[node])
        return self.parent[node]
    
    def union_by_rank(self, u, v):
        ultp_u = self.find_par(u)
        ultp_v = self.find_par(v)
        
        if ultp_u == ultp_v:
            return
        if self.rank[ultp_u] < self.rank[ultp_v]:
            self.parent[ultp_u] = ultp_v
        elif self.rank[ultp_u] > self.rank[ultp_v]:
            self.parent[ultp_v] = ultp_u
        else:
            self.parent[ultp_v] = ultp_u
            self.rank[ultp_u] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_id = {}
        email_to_name = {}
        i = 0

        for acc in accounts:
            name = acc[0]
            for mail in acc[1:]:
                if mail not in email_to_id:
                    email_to_name[mail] = name
                    email_to_id[mail] = i
                    i += 1

        ds = DisjointSet(len(email_to_id) - 1)

        for acc in accounts:
            emails = acc[1:]
            for i in range(len(emails) - 1):
                ds.union_by_rank(email_to_id[emails[i]], email_to_id[emails[i + 1]])

        parent_group = defaultdict(list)

        for email, id in email_to_id.items():
            parent = ds.find_par(id)
            parent_group[parent].append(email)
        
        result = []
        for emails in parent_group.values():
            emails.sort()
            name = email_to_name[emails[0]]
            result.append([name] + emails)

        return result