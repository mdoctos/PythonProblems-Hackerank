if __name__=='__main__':
    x=int(input())
    y=int(input())
    z=int(input())
    n=int(input())
    result_list=[]
    #logic to for  You are given three integers  and  representing the dimensions of a
    # cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, .
    # Please use list comprehensions rather than multiple loops, as a learning exercise.
    #x,y,z representing the dimension and i,j,k coordinates such that
    #i+j+k is not equal to n
    #0<=i<=x;0<=j<=y,0<=k<=z
    #we used multiple loop
    # for i in range(0,x+1):# x is also included in the range
    #   for j in range(y+1):
    #       for k in range(z+1):
    #           if i+j+k!=n:
    #              result_list.append([i,j,k])

    # [expression then for loop then conditional statement for list compresion]
    #using list compresion we dont use multiple loop ,saves time and space
    result_list=[[i,j,k]for i in range(0, x + 1)for j in range(y+1)for k in range(z+1)if i+j+k!=n]
    print(result_list)
