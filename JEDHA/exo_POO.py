

class Math():
    
    #compute the square root of any number
    def square_root(x) :
        result =  x**0.5
        print("The square root of  {} is {:0.1f} ".format(x, result))
        
        
    #Calculate the average of any list of numbers       
    def average(my_list):
        somme = 0
        nb_elements = 0
        for item in my_list:
            somme += item
            nb_elements += 1
        mean = somme / nb_elements
        print("The average of {} is  {:0.1f} ".format(tuple(my_list), mean))
        #print(mean)
        
    #Method to find out if a number is even or odd    
    def odd (x) :
        if x % 2 != 0 :
            print("{} is  odd ".format(x))
        else :
              print("{} is not odd ".format(x))

    #Give the total sum of a list of numbers              
    def total(my_list):
        sums = 0
        for item in my_list:
            sums += item

        print("The total of {} is {:0.1f}".format(tuple(my_list), sums))
        #print(sums)

math1 = Math
math1.square_root(9)
list1 = [10, 30, 20,10]
math1.average(list1)
math1.odd(4)
math1.odd(11)
math1.total(list1)