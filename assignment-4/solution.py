from pprint import pprint
def solution(x,y):

    dict_1 = {}
    z_list = []
    asd = []
    
    number = 1

    for i in range(1, y + 1):
        for j in range(1, i + 1):        
            z_list.append(number)
            number = number + 1
            asd.append()
        dict_1[i] = z_list.copy()
        z_list.clear()
           

    pprint(dict_1)

solution(1,10)