class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        k = {}
        for key, value in knowledge:
            k[key] = value
        
        i = 0
        res = []
        while i < len(s):   
            if s[i] == '(':
                i += 1
                key = []
                while s[i] != ')':
                    key.append(s[i])
                    i += 1
                
                key = ''.join(key)
                print(f"key = {key}")
                # after creating the key check if the key exist in knowledge
                if key in k:
                    # if it does exist then add it's value in res
                    res.append(k[key])
                else:
                    # if its absent then append '?'
                    res.append('?')

            elif s[i] != ')':
                res.append(s[i])
            
            i += 1
                
        
        return ''.join(res)