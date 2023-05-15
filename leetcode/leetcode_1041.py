class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        st=[0,0]
        pos=0
        n=0
        while n<4:
            for i in instructions:
                if i=='L':
                    pos+=1
                elif i=='R':
                    pos-=1
                else:
                    if pos%4==0:
                        st[1]+=1
                    elif pos%4==1:
                        st[0]+=1
                    elif pos%4==2:
                        st[1]-=1
                    else:
                        st[0]-=1
            n+=1
        return st==[0,0]
instructions = "GL"
print(Solution().isRobotBounded(instructions))
