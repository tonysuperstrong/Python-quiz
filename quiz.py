class Quiz:
    def __init__(self):
        self.wrong=0
        self.right=0

    def generate(self,x ,y):
        if x ==y:
            self.right+=1
        else:
            self.wrong+=1

    def end(self):
        print(f"right Score:{self.right}, wrong Score :{self.wrong}")







