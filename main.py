import random
class pipes:
    pipes=[]
    colors=["Red","Green","blue","yellow"]
    rand = random.randint(0,8)
    def __init__(self):
        for i in range(9):
            pipe = []
            for j in range(4):
                if(i == self.rand):
                    self.rand = -1
                    pipe.append("blank")
                    continue
                pipe.append(random.choice(self.colors))
            self.pipes.append(pipe)
                
    def toString(self):
        str = ""
        for i in range(4):
            for j in range(0,len(self.pipes)):
                if(j<5):

                    str += "\t"*(j%5)+ f"{j} : "+self.pipes[j][i]+"\t"
                else:
                    str += "\t"*(j%5)+ f"{j} : "+self.pipes[j][i]+"\t\n"
            str+="\n"
        print(str)
pipe = pipes()
pipe.toString()



