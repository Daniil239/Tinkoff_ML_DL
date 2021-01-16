#Решим задачу при помощи градиентного спуска
def X_derivative(x, y):
    result = 36 * (x ** 5) + 8 * (x ** 3) * (y ** 2) + 20 * x + 6 * y - 6
    return result
def Y_derivative(x, y):
    result = 4 * ( x ** 4) * y + 6 * x + 20 * y
    return result
def function(x, y):
    result = 6 * (x ** 6) + 2 * (x ** 4) * (y ** 2) + 10 * (x ** 2) + 6 * x * y + 10 * (y ** 2) - 6 * x + 4
    return result
    
#Выберем некоторую начальную позицию
x, y, x0, y0 = 0, 0, 0, 0
#Выберем шаг спуска
a = 0.0001
for i in range(10000):
    #На каждой иттерации обновим значения x0 и y0 
    x -= a * X_derivative(x0, y0)
    y -= a * Y_derivative(x0, y0)
    x0, y0 = x, y
print("ML + DL Enter Exam\nTask 2\nAnswer:")
print("min(f(x, y)) = f(", "%0.3f" % x, ",", "%0.3f" % y, ") =", "%0.3f" % function(x, y))
