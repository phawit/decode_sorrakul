text = ' เีึ่ก | วาตศี | ยนลฮา | าทาัว | ฮขขกห | ..น้้ | ณมวเ.'
key_txt = 'ข้าวผัดปู'

#text_coded = input('Enter your text: ')
#key_txt = input('Enter your key_txt: ')

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

def decode(text_Y,key):
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
    k = 0
    r = 0
    for i in range(1,7):
       if text[-i] == 'ฮ' and r == 0:
          k += 1
       else:
          r = 1
    text = text[0:len(text)-k]
    
    if len(text)%len(key) != 0:
       text += 'ฮ'*(len(key) - len(text)%len(key))
    
    n_key = len(key)
    text_keyed = ''
    text_arg=[0]*n_key
    n_rank = len(text)//n_key
    text_div = [0]*n_key
    text_decode = ''

    for i in range(0,n_key):  
        text_div[i] = text[i*n_rank:n_rank*i+n_rank]
        text_arg[int(key[i])] = text_div[i]
    for i in range(0,n_key):
        text_keyed += text_arg[i]
    for i in range(0,n_rank):
        text_decode += text_keyed[i::n_rank]
        
    r = 0
    for i in range(1,len(key)):
        if text_decode[-i] == 'ฮ':
            r += 1
    text_decode = text_decode[0:len(text_decode)-r]
    
    return text_decode


c = cut(key_txt)
key_num = text_key(c)
text_decode = decode(text,key_num)

print('text_coded: {}'.format(text))    
print('key: {}'.format(key_txt))
print('text_decode: {}'.format(text_decode))


