def result_print(number):

    print("Ответ: " + str(number))

def factor(n):
    i = 2
    number = []
    while i * i <= n:
       while n % i == 0: 
           number.append(i)
           n = n / i
       i = i + 1

    if n > 1:
        number.append(int(n))
       
    result_print(number) 
       
        
 
n = int(input("Введите число: "))
factor(n)