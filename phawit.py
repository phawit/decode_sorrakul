from pythainlp.tokenize import word_tokenize
text = ' เีึ่ก | วาตศี | ยนลฮา | าทาัว | ฮขขกห | ..น้้ | ณมวเ.'
#text = input('Enter your text: ')

max_key = 8
n_check = 5

def ofen_key():
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-OFTENS_KEY-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    word_true_ok = 0
    F = open("ofen_key.txt","r") 
    a = F.readlines()
    key_ok = []
    q_ok = 1
    text_dict_ok = ''

    for i in range(0,len(a)):
        F = open("ofen_key.txt","r") 
        a = F.readlines()
        b = a[i][0:len(a[i])-1]
        x = cut(b)
        key = text_key(x)
        print('{}::  key: {} '.format(i,key))

        text_decode = decode(text,key)
        text_dict,word_true,q = check(text_decode,n_check)

        if word_true > word_true_ok:
           word_true_ok = word_true 
           text_dict_ok = text_dict
           key_ok = key
           q_ok = q
           file = open("decoded.txt","a") 
           file.write('key  :: {}  \tTrue: {} False: {}\t{}%\n'.format(key_ok,word_true_ok,q_ok-word_true_ok,100*word_true_ok/q_ok))
           file.write('text :: {}\n\n'.format(text_dict_ok))
           file.close()

        print('key_ok: {}\tTrue: {} False: {} {}% text_dict_ok: {}'.format(key_ok,word_true_ok,q_ok-word_true_ok,100*word_true_ok/q_ok ,text_dict_ok))
        
    return key_ok,word_true_ok,q_ok,text_dict_ok


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


def cut_text(text_Y):
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

    return text


def test_key(a):
     if a%5 != 0:
        a += 5-a%5
     k = 0
     x = [0]*10

     for i in range(1,max_key+1):
         b = a%i
         if b == 0:
            x[k] = i 
            k += 1
            b = a 
        
     x = x[0:k]

     if x[1] == 2:
        x = x[2:len(x)]
     else:
        x = x[1:len(x)]

     print("key_test: {}".format(x))

     return x


def to_int(a):
      c = 0
      for i in range(0,len(a)):
           b = a[i]*10**(len(a)-1-i)
           c += b

      return c 
 

def base(a,b):
       c = [0]*b
       for i in range(1,len(c)):
               c[-i] = a%b
               a = a//b
               c[-i-1] = a
       for i in range(0,len(c)):
             if c.count(i) != 1:
                x = 0
                return 0

       return c


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
    if len(key) == 0:
       key = '0'
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



def check(text_decode,n_check_word):
 
    text_sp=word_tokenize(text_decode,engine='icu')
    text_dict = [0]*len(text_sp)
    word_true = 0

    q = len(text_sp)
    if len(text_sp) >= n_check_word:
       q = n_check_word
    for i in range(0,q):

      text_dict[i]=word_tokenize(text_sp[i],engine='dict')
      
      if text_dict[i] != False:
         word_true += 1

    return text_decode,word_true,q


file = open("decoded.txt","a") 
file.write('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-START-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n')
file.close()

key_ok,word_true_ok,q_ok,text_dict_ok = ofen_key()

print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-RANDOM..KEY-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
j = 1
ct = cut_text(text)
test_k = test_key(len(ct))
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

for g in range(0,len(test_k)):
   k = test_k[g]
   key = str(to_int([k-1]*k))
   e = int(key,k)
   for i in range(0,e):     
        key = base(i,k)
        if key != 0:
          print('{}::  key: {} '.format(j,key))
          j += 1
          text_decode = decode(text,key)
          text_dict,word_true,q = check(text_decode,n_check)
          if word_true > word_true_ok:
             word_true_ok = word_true 
             text_dict_ok = text_dict
             key_ok = key
             q_ok = q
             file = open("decoded.txt","a") 
             file.write('key  :: {}  \tTrue: {} False: {}\t{}%\n'.format(key_ok,word_true_ok,q_ok-word_true_ok,100*word_true_ok/q_ok))
             file.write('text :: {}\n\n'.format(text_dict_ok))
             file.close()
             print('key_ok: {}\tTrue: {} False: {} {}% text_dict_ok: {}'.format(key_ok,word_true_ok,q_ok-word_true_ok,100*word_true_ok/q_ok ,text_dict_ok))
          print('key_ok: {}\tTrue: {} False: {} {}% text_dict_ok: {}'.format(key_ok,word_true_ok,q_ok-word_true_ok,100*word_true_ok/q_ok ,text_dict_ok))

file = open("decoded.txt","a")
file.write('-----------------------------------------------------------\n')
file.write('key  :: {}  \tTrue: {} False: {}\t{}%\n'.format(key_ok,word_true_ok,q_ok-word_true_ok,100*word_true_ok/q_ok))
file.write('text :: {}\n\n'.format(text_dict_ok))
file.close()
print('------------------------------------------------------------------------------')
print('key  :: {}      True: {} False:{}	{}%'.format(key_ok,word_true_ok,q_ok-word_true_ok,100*word_true_ok/q_ok))
print('text :: {}'.format(text_dict_ok))



