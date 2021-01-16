from random import randint
import copy
import pickle

class Field:

    #Поле, на основе которого будет случайным образом создано новое
    
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

    #Отображение поля

    def write(self):
        print("i\j|0 1 2 |3 4 5 |6 7 8")
        for i in range(9):
            if i % 3 == 0:
                print("---+------+------+-----")
            s = ''
            for j in range(9):
                if j % 3 == 0:
                    s += '|'
                if self.field[i][j] == 0:
                    s += ' '
                else:
                    s += str(self.field[i][j])
                s += ' '
            print(i, "", s)
            
        
    #Генерация случайного поля с count заполненными элементами
        
    def generation(self, count):

        #Проверка поля на возможность существования или решаемость
        
        if count > 81:
            count = 81
        if count < 18:
            count = 18
        for i in range (20):

            #Транспонирование
            
            if randint(0, 1) == 1:
                self.field = [[self.field[i][j] for i in range(9)] for j in range(9)]

            #Случайная перестановка строк
                
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
                
    #Реализация сохранения игры
                
    def pause(self):
        
        save_file = open("progress.pkl", "wb")
        pickle.dump(self.field, save_file)
        save_file.close()
        save_actual_file = open("actual.pkl", "wb")
        pickle.dump(self.actual_field, save_actual_file)
        save_actual_file.close()
        
    def loading(self):
        
        load_file = open("progress.pkl", "rb")
        self.field = pickle.load(load_file)
        load_file.close()
        load_actual_file = open("actual.pkl", "rb")
        self.actual_field = pickle.load(load_actual_file)
        load_actual_file.close()

def main():
        
    current_field = Field()

    #Проверка на тип поля
            
    print("Do you want to continue last game (yes or no)?")
    while True:
        s = input()
        if s == "no":    
            count = int(input("Enter number of filled cells: "))
            current_field.generation(count)
            break
        elif s == "yes":
            current_field.loading()
            break
        else:
            print("Wrong answer, try again")
                
    #Отображение поля
                
    current_field.write()

    #Проверка на тип игры (кто играет)

    print("Who would play (human or pc)?")
    
    while True:
        s = input()

        #Игра за человека
        
        if s == "human":
            while current_field.field != current_field.actual_field:            
                ans = input("Next change (i, j, num) or 'pause': ").split()
                if ans[0] == "pause":
                    current_field.pause()
                    return 1
                else:
                    i, j, num = int(ans[0]), int(ans[1]), int(ans[2])
                    if current_field.actual_field[i][j] == num:
                        current_field.field[i][j] = num
                        current_field.write()
                    else:
                        print("Wrong answer, try again")
            print("You win!")
            return 1

        #Игра за компьютер
        
        elif s == "pc":
            current_field.field = current_field.actual_field
            current_field.write()
            print("So easy!")
            return 1
        
        else:
            print("Wrong answer, try again")

main()



            
            

