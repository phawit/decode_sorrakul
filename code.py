text = 'เข้าตีข้าศึก ณ ที่หมายก. วันว. เวลาน.'
key_txt = 'ข้าวผัดปู'
#text = input('Enter your text: ')
#key_txt = input('Enter your key_txt: ')

def text_coded(text_Y,key):
    
    text_z = [0]*len(text_Y)
    k = 0
    for i in range(0,len(text_Y)):
        if text_Y[i] == ' ' or text_Y[i] == '|':
            k = k           
        else:                        
           text_z[k] = text_Y[i]
           k += 1
    text_z = text_z[0:k]
    text = ''
    for i in range(0,len(text_z)):
         text += text_z[i] 
    
    if len(text)%len(key) != 0:
       p ='ฮ'*(len(key)-len(text)%len(key))
       text += p

    n_key = len(key)
    text_arg =''*n_key
    n_rank = len(text)//n_key
    text_div = [0]*n_key
    text_x = [0]*n_key
    text_y =''*n_key
    
    for i in range(0,n_key):
        text_arg += text[i::n_key]
    for i in range(0,n_key):  
        text_div[i] = text_arg[i*n_rank:n_rank*i+n_rank]
    for i in range(0,n_key):
        text_x[i] = text_div[int(key[i])]
    for i in range(0,n_key):
        text_y += text_x[i]

    if len(text_y)%5 != 0:
       p = 'ฮ'*int(5-len(text_y)%5)
       text_y += p
       
    text_Y = ''
    for i in range(0,len(text_y)//5):  
        text_Y += text_y[i*5:5*i+5] +' | '
    text_Y = text_Y[0:len(text_Y)-3]

    return text_Y

def text_key(a):
    x = sorted(a)
    y = [0]*len(a)
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if a[i] == x[j]:
               y[i] = j 

    for j in range(1,len(y)+1):
         s = y[-j]
         k = 0
         for i in range(1,len(y)+1):
              if y[-i] == s:
                 y[-i] = s+k 
                 k -= 1
                 
    return(y)

def cut(a):
    b = [0]*len(a)
    z = 0
    for i in range(0,len(a)):
        b[i] = a[i]
    for i in range(0,len(a)):
        if a[i] == 'ะ' or a[i] == 'า' or a[i] == 'ิ' or a[i] == 'ี' or a[i] == 'ุ' or a[i] == 'ู' or a[i] == 'เ' or a[i] == 'แ' or a[i] == '่' or a[i] == '้' or a[i] == '๊'  or a[i] == '๋' or a[i] == 'ำ' or a[i] == 'ๆ' or a[i] == 'ๅ'  or a[i] == '์' or a[i] == 'ไ'  or a[i] == 'ใ' or a[i] == 'ึ' or a[i] == 'ื' or a[i] == '็' or a[i] == 'ํ' or a[i] == 'ั'  or a[i] == 'โ':
           b[i] = 0
           z += 1
    c = [0]*(len(a)-z)
    j = 0
    for i in range(0,len(a)):
        if b[i] != 0:
            c[j] = b[i]
            j += 1
    return c 


c = cut(key_txt)
key_num = text_key(c)
x = text_coded(text,key_num)

print('text: {}'.format(text))
print('key: {}'.format(key_txt))
print('text_decode: {}'.format(x))



