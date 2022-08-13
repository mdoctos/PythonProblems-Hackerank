if __name__ == '__main__':
    result_list = []
    grad_list=[]
    n=int(input())
    for i in range(n):
        name = input()

        score = float(input())

        result_list.append([name,score])
        grad_list.append(score)#calculation 2nd lowest
        #print(result_list)
        #print(grad_list)
    grad_list=sorted(set(grad_list)) #sorted unique
    m=grad_list[1]
    name=[]
    for val in result_list:
        if m==val[1]:
            name.append(val[0])
    name.sort()
    for nm in name:
        print(nm)












