# f= open("main.tx", "r")
# # f.write("Hello")
# t = f.read()
# print(t)

def game():
    return float(input("Enter your score: "))
    

score = game()
with open("highscore.txt") as f:
    highscore = int(f.read())
if(highscore<score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))
        
    