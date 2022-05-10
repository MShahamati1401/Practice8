

def menu():
    print('1- Sum')
    print('2- tafrigh')
    print('3- zarb')
    print('4- taghsim')
    get_operate = input('Please Inter Amalgar:')
    return get_operate
def sum_kasr():
    sorate_f = (list[-2]['sorat'] * list[-1]['makhraj']) + (list[-1]['sorat'] * list[-2]['makhraj'])
    makhraj_f = list[-2]['makhraj'] * list[-1]['makhraj']
    list_f.append({'sorat':sorate_f, 'makhraj': makhraj_f})
    print(f"{list_f[-1]['sorat']}/{list_f[-1]['makhraj']}")

def tafrigh():
    sorate_f = (list[-2]['sorat'] * list[-1]['makhraj']) - (list[-1]['sorat'] * list[-2]['makhraj'])
    makhraj_f = list[-2]['makhraj'] * list[-1]['makhraj']
    list_f.append({'sorat':sorate_f, 'makhraj': makhraj_f})
    print(f"{list_f[-1]['sorat']}/{list_f[-1]['makhraj']}")

def zarb():
    sorate_f = (list[-2]['sorat'] * list[-1]['sorat'] )
    makhraj_f = list[-2]['makhraj'] * list[-1]['makhraj']
    list_f.append({'sorat': sorate_f, 'makhraj': makhraj_f})
    print(f"{list_f[-1]['sorat']}/{list_f[-1]['makhraj']}")

def taghsim():
    sorate_f = (list[-2]['sorat'] * list[-1]['makhraj'])
    makhraj_f = list[-2]['makhraj'] * list[-1]['sorat']
    list_f.append({'sorat': sorate_f, 'makhraj': makhraj_f})
    print(f"{list_f[-1]['sorat']}/{list_f[-1]['makhraj']}")

def get_num():
    sorat = int(input('Inter sorate Kasr: '))
    makhraj = int(input('Inter makhraj kasr: '))
    return sorat, makhraj

while True:
    list = []
    list_f = []
    sorat, makhraj = get_num()
    list.append({'sorat': sorat, 'makhraj': makhraj})
    operator = menu()
    sorat, makhraj = get_num()
    list.append({'sorat': sorat, 'makhraj': makhraj})
    if operator == '1':
        sum_kasr()

    if operator == '2':
        tafrigh()

    if operator == '3':
        zarb()

    if operator == '4':
        taghsim()

    edame = input("Do you want Continue Press 'y' or exit 'n'")
    if edame == 'n':
        exit()

