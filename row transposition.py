import math

# Encryption
def encryptMessage(msg,key):
    cipher = ""
  
    # track key indices
    k_indx = 1
  
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = [int(x) for x in str(key)]
  
    # calculate column of the matrix
    col = len(key_lst)
      
    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))
  
    # add the padding character '_' in empty
    # the empty cell of the matix 
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
   
  
    # create Matrix and insert message and 
    # padding characters row-wise 
    matrix = [msg_lst[i: i + col] 
              for i in range(0, len(msg_lst), col)]
    

  
    # read matrix column-wise using key
    for _ in range(col):
        curr_idx = key_lst.index(k_indx)
        cipher += ''.join([row[curr_idx] 
                          for row in matrix])                
        k_indx += 1
  
    return cipher

text = input("enter your text: ")
key = int(input("enter your key: "))
cipher = encryptMessage(text,key)
print("Encrypted Message: {}".
               format(cipher))