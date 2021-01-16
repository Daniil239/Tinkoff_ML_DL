from random import randint
import copy
import pickle

notmylist = [1]
file = open("load.pkl", "rb") # "wb"
notmylist = pickle.load(file) # pickle.dump(mylist, file)
file.close()
print(notmylist)

class Field:
    def __init__(self):
        self.actual_field = [[]]
        self.field = [[4, 9, 3, 2, 6, 1, 5, 8, 7],
                      [8, 2, 7, 5, 4, 3, 6, 1, 9],
                      [1, 5, 6, 9, 8, 7, 3, 4, 2],
                      [7, 4, 2, 6, 3, 8, 1, 9, 5],
                      [6, 3, 9, 1, 7, 5, 4, 2, 8],
                      [5, 1, 8, 4, 2, 9, 7, 3, 6],
                      [9, 8, 4, 3, 5, 6, 2, 7, 1],
                      [3, 7, 5, 8, 1, 2, 9, 6, 4],
                      [2, 6, 1, 7, 9, 4, 8, 5, 3]]
        
    def generation(self, count):
        if count > 81:
            count = 81
        if count < 18:
            count = 18
        for i in range (20):
            if randint(0, 1) == 1:
                self.field = [[self.field[i][j] for i in range(9)] for j in range(9)]
            for i in range(0, 9, 3):
                if randint(0, 1) == 1:
                    self.field[i], self.field[i + 1] = self.field[i + 1], self.field[i]
                if randint(0, 1) == 1:
                    self.field[i], self.field[i + 2] = self.field[i + 2], self.field[i]
                if randint(0, 1) == 1:
                    self.field[i + 2], self.field[i + 1] = self.field[i + 1], self.field[i + 2]
        self.actual_field = copy.deepcopy(self.field)
        i = 0
        while i < 81 - count:
            if self.field[i % 9][randint(0, 8)] != 0:
                self.field[i % 9][randint(0, 8)] = 0
                i += 1

print("Who will play (human or pc)?")
while True:
    s = input()
    if s == "human":
        count = int(input("Enter number of filled cells: "))
        current_field = Field()
        current_field.generation(count)

        for line in current_field.field:
            print(line)
        while current_field.field != current_field.actual_field:            
            ans = input("Next change (i, j, num): ").split()
            i, j, num = int(ans[0]), int(ans[1]), int(ans[2])
            if current_field.actual_field[i][j] == num:
                current_field.field[i][j] = num
                for line in current_field.field:
                    print(line)
            else:
                print("Wrong answer, try again")
                
            
        break
    elif s == "pc":

        break
    else:
        print("Wrong answer")
        

            
            

