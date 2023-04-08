def card_conv(x:int, r:int)->str:
    
    d=''
    dchar='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while(x>0):
        d+=dchar[x%r]
        x//=r

    return d[::-1]

if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')

    while True:

        while True:
            x = int(input('변환하고 싶은 양의 정수를 입력하세요.: '))
            if x>0:
                break
        
        while True:
            r = int(input('몇 진수로 변환하고 싶으십니까? : '))
            if r>0:
                break

        
        print(f'{x}를 {r}진수로 변환시킨 값은 {card_conv(x, r)}입니다.')

        
        retry = str(input('다시 시도하시겠습니까? (Y/N)'))
        if retry == 'N' or 'n':
            break