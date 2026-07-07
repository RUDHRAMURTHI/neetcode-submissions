class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        _open={
            ')':'(',
            ']':'[',
            '}':'{'
            }
        for item in s:
            # print("item:", item)
            # print("stack:", stack)
            if item in _open.values():
                # print("item added to stack")
                stack.append(item)
            else:
                if stack:
                    last=stack.pop()
                    if _open[item] != last:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True

            
        