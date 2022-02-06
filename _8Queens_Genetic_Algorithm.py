import random



def Fitness(arr):
    length= len(arr)
    f=[28]*length

    for i in range(length):
        col=[]
        for j in range(7):
            for k in range(j+1,8):
                if arr[i][j] == arr[i][k]:
                    f[i]-=1

                if abs(arr[i][j] -arr[i][k]) == abs(k-j):
                    f[i]-=1
   # print("Fitness:\t" ,f)
    return f
 


def Possibility(arr ,fitness):
    sum_f=0
    p=[]
    for i in fitness:
        sum_f += i
    
   
    
    
    for i in fitness:
        p.append(round((i*100 / sum_f),2) )

    #print("Possibility:\t" ,p)

    temp = arr
    arr = []

    for j  in zip(p,temp,fitness):
        arr.append(j)
    
    arr.sort(reverse=True,key=lambda x:x[0])

    return arr

   

def Cross_Over(number_of_child , arr):
    cross_over=[[None for i in range(8)] for j in range(number_of_child)]
    check_cross=[]
    

    for i in range(0,number_of_child,2):
        flag = True
        while flag:
            
            flag_2=True
            index_row = random.randint(0,len(arr)-1),random.randint(0,len(arr)-1)
            
            if index_row[0] == index_row[1]:
                continue

            for row in check_cross:
                if row == index_row or row == (index_row[1] , index_row[0]):
                    flag_2 = False
                    break

            if flag_2:
                flag = False
                check_cross.append(index_row)

        

        index = random.randint(1,7)

        print(arr[index_row[0]][1][:index],arr[index_row[0]][1][index:])
        print(arr[index_row[1]][1][:index],arr[index_row[1]][1][index:]) 
        print()

        cross_over[i][:index] = arr[index_row[0]][1][:index]
        cross_over[i][index:] = arr[index_row[1]][1][index:]
        
        
        if number_of_child%2!=0 and i == number_of_child-1:
            break

        cross_over[i+1][:index] = arr[index_row[1]][1][:index]
        cross_over[i+1][index:] = arr[index_row[0]][1][index:]
        

    return cross_over



def Mutation(arr):
    mut=[]
    mutation = []
    for i in arr:
        if random.randint(1,10) == 10:
            mut = i
            mut[random.randint(0,7)] = random.randint(1,8)
            mutation.append(mut)
    return mutation



def selection(arr):
    selected=[]
    
    len_arr = len(arr)
    
    selected.append(arr[0])
    selected.append(arr[1])
    selected.append(arr[-1])
    selected.append(arr[len_arr//2])
    
    while True:
        index = random.randint(2,len_arr-2)
        if index!=len_arr//2:
            selected.append(arr[index])
            break
    return selected
    

def print_(title,arr):
    print(title+':')
    for row in arr:
        print(row)

################################## start program ##########################################

#define First Population
first_population = [[random.randint(1,8) for i in range(8)]for j in range(10)]
answer = []
f=[]
flag=True
flag_3=True

while flag :

    

    f = Fitness(first_population)
    
    for i in range(5):
       if f[i]==28:
           print(first_population[i])
           flag = False
           break
   
    #for i in range(1,5):
    #    if f[0]!=f[i]:
    #        flag_3 = False
    #        break
    #
    #if flag_3:
    #    print("This population is not answer")
    #    break

        

    first_population = Possibility(first_population,f)

    print_("First Population",first_population)
    print('\n')

     
    #Cross-over ////////////////////////////////////////////////////////////////////////////
    
    cross_over = Cross_Over(5,first_population)
    print_('cross over',cross_over)
    print('\n-----------------------------------\n')
     
    #Mutation ///////////////////////////////////////////////////////////////////////////

    mutation = Mutation(cross_over)
    print_('mutation',mutation)
    print('\n-----------------------------------\n')

    #select Final Populatoin  ///////////////////////////////////////////////////////////
    final_population=[]
    
    for i in first_population:
        final_population.append(i[1])
    
    for i in cross_over:
        final_population.append(i)
    
    for i in mutation:
        final_population.append(i)
    
    
    final_population = Possibility(final_population,Fitness(final_population))
    
    select = selection(final_population)
    
    first_population=[]
    
    for i in select:
        first_population.append(i[1])

    #input(chr)