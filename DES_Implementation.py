
INITIAL_PERMUTATION=[58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
EXPANSION_PERMUTATION=[32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
PERMUTATION_TABLE= [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
INVERSE_PERMUTATION_TABLE = [40, 8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37 , 5 , 45 , 13 , 53 , 21 , 61 , 29,36 , 4 , 44 , 12 , 52 , 20 , 60 , 28,35 , 3 , 43 , 11 , 51 , 19 , 59 , 27,34 , 2 , 42 , 10 , 50 , 18 , 58 , 26,33 , 1 , 41 , 9 , 49 , 17 , 57 , 25]
SBOX1= [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
SBOX2=[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
SBOX3=[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
SBOX4=[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
SBOX5=[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
SBOX6=[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
SBOX7=[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
SBOX8=[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
PC=[ 14,17,11,24,1,5,3 ,28 ,15 ,6 ,21, 10,23,19, 12,4  ,26 ,8,16,  7,27, 20, 13,2,41,52 ,31,37,47,55,30 ,40, 51 ,45 ,33  , 48,44  ,49,39,56,  34 ,53,46, 42,50, 36, 29, 32]
table_for_key=[ 57 , 49 , 41, 33 ,25, 17, 9,1 , 58 ,50 ,42,34 ,26,18,10 ,2,59,51,43 ,35,27,19,11 ,3 ,60,52  ,44,36,63,55,47, 39 ,31, 23,15,7,62, 54,46 ,38,30,22,14 , 6,61,53,45,37,29,21, 13,5,28, 20,12,4]
Input=str(input("Enter Message to be Encrypted : "))
first_key=str(input("KEY(64 Bits) : "))
SBOX=[SBOX1,SBOX2,SBOX3,SBOX4,SBOX5,SBOX6,SBOX7,SBOX8]
full_key=bin(int(first_key,16))         #Converts key to binary 
full_key=full_key[2:]                   #and removes 0b from it
if len(full_key)<64:
    for x in range(64-len(full_key)):     #for initial zeroes
        full_key="0"+full_key

if(len(full_key)!=64):
    print("Key size must be 64 bits")
    exit()
  


permuted_key=""
left_key=""
right_key=""
for index in table_for_key:
    permuted_key+=full_key[index-1]      #permutation of key bits

def pbox(PERMUTATION_TABLE,str):           #permutes given string according to given table
    answer=""
    for x in PERMUTATION_TABLE:
        answer+=str[x-1]
    return answer

for x in range(28):
    left_key+=permuted_key[x]               
    right_key+=permuted_key[28+x]

right=["","","","","","","","","","","","","","","",""]
left=["","","","","","","","","","","","","","","",""]

#expansion_and_key_xor for shifting bits
def shift(string,d):
    Lfirst = string[0 : d]
    Lsecond = string[d :]
    Rfirst = string[0 : len(string)-d]
    Rsecond = string[len(string)-d : ]
    return Lsecond+Lfirst

# standard shifting of key bits
right[0]=shift(right_key,1)
left[0]=shift(left_key,1)
right[1]=shift(right[0],1)
left[1]=shift(left[0],1)
for x in range(2,8):
    right[x]=shift(right[x-1],2)
    left[x]=shift(left[x-1],2)
right[8]=shift(right[7],1)
left[8]=shift(left[7],1)
for x in range(9,15):
    right[x]=shift(right[x-1],2)
    left[x]=shift(left[x-1],2)
right[15]=shift(right[14],1)
left[15]=shift(left[14],1)

key=["","","","","","","","","","","","","","","",""]

for x in range(16):
    key_before_permutation=""
    key_before_permutation+=left[x]+right[x]
    key[x]=pbox(PC,key_before_permutation)

#----------------------------------------KEYS ARE FOUND ----------------------/#
Message=bin(int(Input,16))          #Converts message to binary
# Message=Message[2:]
# h=len(Message)
# if h<64:
#     for x in range(64-h):
#         Message="0"+Message
def comp(x):
    x=x[2:]
    h=len(x)
    if h<64:
        for i in range(64-h):
            x="0"+x
    return x

Message=comp(Message)

if(len(Message)!=64):
    print("Text size must be 64 bits")
    exit()
  
Message_after_permutation=""                          
for x in INITIAL_PERMUTATION:
	Message_after_permutation+=Message[x-1]

def expansion_32_to_48(rightbits,ep) :
    final_bits=""
    for index in ep:
        final_bits+=rightbits[index-1]
    return final_bits

def xor(string,key):
    answer=""
    for x in range(48):
        if string[x]==key[x] :
            answer+="0"
        else :
            answer+="1"
    return answer
#xor is for xor of 48 digits
#xor u is for xor of 32 digits            
def xor_u(string,key):
    answer=""
    for x in range(32):
        if string[x]==key[x] :
            answer+="0"
        else :
            answer+="1"
    return answer

def sbox(sbox,str):
    answer=""
    r=int((str[0]+str[5]),2)
    c=int((str[1]+str[2]+str[3]+str[4]),2)
    e1=sbox[r]
    u=bin(e1[c])# u is a string
    length=len(u)
    if length<6 :
        for x in range(2,8-length):
            answer+="0"
        for x in range(length-2):
            answer+=u[x+2]
    else :
        answer=u[2]+u[3]+u[4]+u[5]

    return answer

def sboxi(str,num):
    return sbox(SBOX[num],str)



def expansion_and_key_xor(str,key,ep):
    after_expansion=expansion_32_to_48(str,ep)
    after_xor=xor(after_expansion,key)
    return after_xor

l0=Message_after_permutation[0:32]      #l0 and r0 are left and right halfs of the text(permuted)
r0=Message_after_permutation[32:64]
for x in range(16):
    after_exp=expansion_and_key_xor(r0,key[x],EXPANSION_PERMUTATION)
    s1=after_exp[0:6]
    s2=after_exp[6:12]
    s3=after_exp[12:18]
    s4=after_exp[18:24]
    s5=after_exp[24:30]
    s6=after_exp[30:36]
    s7=after_exp[36:42]
    s8=after_exp[42:48]
    after_s1=sbox(SBOX1,s1)
    after_s2=sbox(SBOX2,s2)
    after_s3=sbox(SBOX3,s3)
    after_s4=sbox(SBOX4,s4)
    after_s5=sbox(SBOX5,s5)
    after_s6=sbox(SBOX6,s6)
    after_s7=sbox(SBOX7,s7)
    after_s8=sbox(SBOX8,s8)
    finalstringbefore=after_s1+after_s2+after_s3+after_s4+after_s5+after_s6+after_s7+after_s8
    final_string=pbox(PERMUTATION_TABLE,finalstringbefore)
    if x<16:
        temp=r0
        r0=xor_u(final_string,l0)
        l0=temp

before_inverse=r0+l0

cipher=""

for x in INVERSE_PERMUTATION_TABLE :
    cipher+=before_inverse[x-1]

Cipher_Text=hex(int(cipher,2))
Cipher_Text=Cipher_Text[2:]
print(f"Encrypted Text is : {Cipher_Text}")

# Code by Vikrant Malik