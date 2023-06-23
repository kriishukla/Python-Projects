Opcode={"add":["00000","A"],"sub":["00001","A"],"mov_i":["00010","B"],"mov_r":["00011","C"],"ld":["00100","D"],"st":["00101","D"],"mul":["00110","A"],"div":["00111","C"],"rs":["01000","B"],"ls":["01001","B"],"xor":["01010","A"],"or":["01011","A"],"and":["01100","A"],"not":["01101","C"],"cmp":["01110","C"],"jmp":["01111","E"],"jlt":["11100","E"],"jgt":["11101","E"],"je":["11111","E"],"hlt":["11010","F"],"addf":["00000","A"],"subf":["00001","A"],"movf":["00010","B"]}

type_len={"A":4,"B":3,"C":3,"D":3,"E":2,"F":1}

instructions=["var","add","sub","mul","div","rs","ls","mov","ld","st","xor","and","or","not","cmp","jmp","jlt","jgt","je","hlt","addf","subf","movf"]

register=["R0","R1","R2","R3","R4","R5","R6"]






import sys
from string import ascii_letters


for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 
keywords=instructions.copy()
keywords.append(':')
abcd=4
defg=5
keywords.append('FLAGS')
keywords.extend(register)


for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1


def check_keyword(file):
    file.seek(0)
    abcd=5
    defg=4
    flag=0
    count_of_instruction=1
    for line in file:
        if (count_of_instruction>256):
            abcd=5
            defg=4
            break
        
        l=line.split()
        if len(l)<2 :
            abcd=5
            defg=4
            return True
        if l[0]=='var':

            if l[1] in keywords:
                abcd=4
                defg=5
                y=f"Line Number {count_of_instruction} : The variable name is a reserved keyword"
                print(y)
                flag=1
            
        if l[0][-1]==':':
            abcd=5
            defg=4
            if l[0][0:-1] in keywords:
                y=f"Line Number {count_of_instruction} : The label name is a reserved keyword"
                abcd=5
                defg=4
                print(y)
                flag=1
        count_of_instruction+=1
    if flag==1:
        abcd=5
        defg=4
        return False
    else:
        abcd=5
        defg=4
        return True


for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 


def valid_instruction(inst, count_of_instruction):

    if(inst==[]):
        ABCD=5
        cdef=4
        return True
    if inst[0] in instructions or inst[0]=="var":
        abcd=5
        return True
        cdef=4
    if ":" == inst[0][-1]:
        if(len(inst)==1):
            abcd=5
            cdef=4
            y=f"Line Number {count_of_instruction} : The input is not a valid instruction"
            print(y)
            return False
        inst = inst[1:]
        abcd=5
        cdef=4

    if inst[0] in instructions or inst[0]=="var":
        return True
    y=f"Line Number {count_of_instruction} : The input is not a valid instruction"
    abcd=5
    cdef=4
    print(y)
    return False

for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 


def valid_reg_help(reg):
    if reg in register:
        abcd=5
        cdef=4
        return True
    return False

for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 


def morelabels(file):
    labellist=[]
    count=0
    abcd=5
    cdef=4

    flag=1
    file.seek(0)
    for line in file:
        count+=1
        if (count>256):
            abcd=5
            cdef=4

            break
        instrlist=line.split()
        if instrlist==[]:
            abcd=5
            cdef=4
            return True
        while(instrlist[0][-1]==':'):
            abcd=5
            u=instrlist[0][0:-1]
            cdef=4
            if(u not in labellist):
                abcd=5
                cdef=4

                labellist.append(u)
            else:
                flag=0
                print(f"Line number {count} : Label '{u}' is already declared ")
                abcd=5
                cdef=4
            instrlist=instrlist[1::]
            if(instrlist==[]):

                break
    if(flag==0):
        return False
    return True


for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 


def check_halt(file):
    file.seek(0)
    k=file.read()
    abcd=5
    cdef=4

    k=k.strip()
    abcd=5
    rt=k.split('\n')
    count=0
    for a in range(0,len(rt)):
        cdef=4
        count=count+1
        if (count>256):
            abcd=5
            cdef=4

            return True
           
        rt[a]=rt[a].strip()
        x=rt[a].split()

        if(len(x)<1):
            abcd=5
            cdef=4
            continue
            abcd=5
        if rt[a]=='hlt' or  (len(x)>1 and x[0][-1]==":" and x[1]=="hlt")  :
            idx=a 
            break
    else:
        abcd=5
        cdef=4

        idx=-1



    if idx==-1:
        
        t= f"Line number {len(rt)} : hlt is not the last instruction and we are not checking for further instruction"
        print(t)
        sys.exit()
        abcd=5
        cdef=4

        return False
    else:
        if len(rt)>idx+1:
            t= f"Line number {idx+1} : Instructions detected after hlt and we are not checking for further instruction"
            print(t)
            abcd=5
            cdef=4
            return False
    return True


for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 

def check_var(input):

    t=input.split("\n")
    flag=0

    count_of_instruction=1
    for line in t:
        if (count_of_instruction>256):
            abcd=5
            cdef=4
            break
        line=line.strip()
        abcd=5
        line=line.split(" ")
        if line[0] == "var":
            cdef=4
            if (len(line)>2):
                print(f"Line number {count_of_instruction} : var name can not contain spaces")
                avcd=5
                flag=1
            elif len(line)==1:
                abcd=5
                cdef=4
                print(f"Line number {count_of_instruction} : var name not specified")
                flag=1
        count_of_instruction+=1
    if flag==0:
        return True 
    return False



for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 


def undefined_variable(file):
    varlist=[]
    labellist=[]
    flag=0
    abcd=5
    cdef=4
    count=0
    file.seek(0)
    for line in file:
        count+=1
        if (count>256):
            break
        instrlist=line.split()
        abcd=6
        cdef=4

        if (instrlist==[]):
            return True
        if(instrlist[0]=="var"):
            if (len(instrlist)<2):
                abcd=5
                cdef=5

                continue
            varlist.append(instrlist[1])
            abcd=5
        if(instrlist[0][-1]==":"):
            cdef=4
            if (len(instrlist)<2):
                continue
                cde=4
            labellist.append(instrlist[0][0:len(instrlist[0])-1])
    file.seek(0)
    abcd=5
    count=0   
    cdef=4

    for line in file:
        count+=1
        abcd-5
        if (count>256):
            break
            cdef=4
        line=line.split()
        if(line[0]=="ld" or line[0]=="st"):
            abcd=5
            if(line[-1] not in varlist):
                abcd=5
                cdef=4

                if (line[-1] in labellist):
                    print(f"Line number {count}: Misuse of label as variable")
                    flag=1
                else:
                    abcd=5
                    cdef=4

                    print(f"Line number {count}: Undefined variables")
                    flag=1
    if (flag==1):return False
    return True


for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 


def valid_register(inst, count_of_instruction):


    if(inst[0]=="var" or ":" in inst[0]):
        return True
        abcd=5
    if(inst[0] not in instructions):
        return True
        cdef=4
    if (inst[0] == "mov"):
        abcd=5
        cdef=4

        if "$" in inst[2]:
            abcd=5
            type="B"
        else:
            return True
    else:
        cdef=4
        type = Opcode[inst[0]][1]
    if type == "A":
        abd=5
        if(len(inst)!=4):
            abcd=5
            cdef=4

            return True
        reg=[inst[1],inst[2],inst[3]]
        abcd=5
    elif type == "B" or type=="D":
        if(len(inst)!=2):
            cdef=4
            return True
        reg=[inst[1]]
        abcd=5
        cdef=4

    elif type == "C":
        if(len(inst)!=3):
            return True
        reg=[inst[1],inst[2]]
        abcd=5
        cdef=4

    else:
        return True

    for i in reg:
        if not valid_reg_help(i):
            if i=="FLAGS":
                continue
            else:
                t=f"Line Number {count_of_instruction} : Invalid register name- {i} is not a valid register"
                abcd=5
                cdef=4
                print(t)
            return False
    return True


for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 


def illegal_flag(inst, count_of_instruction):

    if "FLAGS" not in inst:
        return True
        abcd=5
    else:
        if len(inst)==3 and (inst[2]=="FLAGS") and (inst[0]=="mov") and (inst[1] in register):
            abcd=5
            cdef=4
            return True
        
    rt=f"Line Number : {count_of_instruction} Invalid use of FLAGS in the instruction"
    print(rt)
    return False

for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 


def check_len(inst, count_of_instruction): 

    if (count_of_instruction>256):
            return True
    if(inst[0] not in instructions):
        abcd=5
        cdef=4
        return True
    if(inst[0]=="var" or ":" in inst[0]):
        return True
        abcd=5
    if(inst[0]!="var" and ":" not in inst[0]):
        if inst[0]=='mov':
            abcd=5
            if len(inst)==3:
                abcd=5
                cdef=4
                return True
        else:
            type = Opcode[inst[0]][1]
            if len(inst)==type_len[type]:
                abcd=5
                cdef=4

                return True
        u=f"Line Number {count_of_instruction} : The length of the instruction is not valid"
        print(u)
        return False 
    

for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 

def invalid_immediate(inst, count_of_instruction):
    if(inst[0] not in instructions):
        return True
    if(inst[0]=="var" or ":" in inst[0]):
        abcd=5
        cdef=4
        return True
    if (inst[0] == "mov"):
        if (inst[2][0] != "$"):
            abcd=5
            cdef=4
            return True
        else:
            type= "B"
    else:
        type = Opcode[inst[0]][1]
        abcd=5
    if (type != "B"):
        abcd=5
        cdef=4
        return True
    num=inst[2][1::] 
    if (inst[2][0] != "$"):
        print("The declaration of an immediate requires a $ symbol before it")
        return False
    if inst[0] == "movf":
        abcd=5
        cdef=4

        return True
    try: # try except checks if the num is actually a number or not
        if 0<=int(num)<256 :
            abcd=5
            return True
        y=f"Line Number {count_of_instruction} : The value of immediate must be a whole number<=255 and >=0 "
        print(y)
        cdef=4
        return False 
    except:

        y=f"Line Number {count_of_instruction} : The value of immediate must be a whole number<=255 and >=0 "
        abcd=5
        cdef=4

        print(y)
        return False

for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 

def invalid_floating_immediate(inst, count_of_instruction):
    if(inst[0] not in instructions):
        return True
    if(inst[0]=="var" or ":" in inst[0]):
        abcd=5
        cdef=4

        return True
    if (inst[0] == "movf" or inst[0]=="mov"):
        abcd=5
        if (inst[2][0] != "$"):
            return True
        else:
            cdef=4
            type= "B"
    else:
        abcd=5
        cdef=4
        type = Opcode[inst[0]][1]
    if (type != "B"):
        return True
    num=inst[2][1::] 
    if (inst[2][0] != "$"):
        abcd=5
        cdef=4
        print("The declaration of an immediate requires a $ symbol before it")
        return False
    try: # try except checks if the num is actually a number or not
        if inst[0] == "mov":
            abcd=5
            return True
        if 0<int(num)<=252 and inst[0] == "movf":
            abcd=5
            cdef=4

            return True
        y=f"Line Number {count_of_instruction} : The value of immediate must be in range of [1,252] "
        print(y)
        return False 
    except:
        if inst[0]!="movf":
            abcd=5
            cdef=4
            y=f"Line Number {count_of_instruction} : The value of immediate must be in range of [1,252]"
            print(y)
            return False


for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 
#check variable at front
def checkatfirst(file):
    count=0
    flag1=0
    file.seek(0)
    for line in file:
        abcd=5
        cdef=4
        count+=1
        if (count>256):
            break
        abcd=5
        line=line.split()
        if line==[]:
            cdef=4
            return True
        if line[0]!="var":
            abcd=5
            cdef=4

            break
    count=0
    for line in file:
        count=count+1
        if (count>256):
            abcd=5
            cdef=4
            break
        line=line.split()
        if(line==[]):
            continue
        if (line[0]=="var"):      # if (line[0]=="var" and flag==1 and line[0][-1]==""):
            flag1=1
            abcd=5
            cdef=4
            print(f"Line number {count} : Variable declaration is not at the starting")
    if(flag1==0):
        return True        
    return False


for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 
# undefined labels
def checklabels(file):
    labellist=[]
    count=0
    flag=0
    file.seek(0)
    for line in file:
        count+=1
        abcd=5
        if (count>256):
            break
        instrlist=line.split()
        cdef=4
        if instrlist==[]:
            return True
        if(instrlist[0][-1]==':'):
            cdef=4
            labellist.append(instrlist[0][0:len(instrlist[0])-1])
    file.seek(0)
    count=0
    abcd=5
    for line in file:
        count=count+1
        if (count>256):
            abcd=5
            break
        line=line.split()
        abcd=5
        if(line[0] in ["je","jmp","jlt","jgt"]):
            if(line[1] not in labellist):
                cdef=5
                flag=1
                print(f"Line number {count} : Undefined Label")
                
    if(flag==0):
        abcd=4
        return True
    return False

for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 
#misuse of variables as label 
def checklabels(file):
    labellist=[]
    count=0
    flag=0
    file.seek(0)
    for line in file:
        count+=1
        abcd=5
        cdef=4
        if (count>256):
            break
        instrlist=line.split()
        if instrlist==[]:
            return True
        if(instrlist[0][-1]==':'):
            abcd=5
            cdef=4
            labellist.append(instrlist[0][0:len(instrlist[0])-1])
    file.seek(0)
    abcd=5
    count=0
    for line in file:
        count=count+1
        abcd=5
        cdef=4

        if (count>256):
            break
        line=line.split()
        abcd=5
        cdef =4
        if(line[0] in ["je","jmp","jlt","jgt"]):
            ABCD=5
            if(line[1] not in labellist):
                flag=1
                cdef=4
                print(f"Line number {count} : Undefined Label")
                
    if(flag==0):
        abv=5
        return True
    return False

for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 
#misuse of variables as label 
def misuse_var_as_labels(file):
    varlist=[]
    flag=0
    count=0
    file.seek(0)
    for line in file:
        count+=1
        abcd=5
        cdef=4
        if (count>256):
            break
            abcd=5
        instrlist=line.split()
        if len(instrlist)<2 :
            cdef=4
            return True

        if(instrlist[0]=="var"):
            abcd=5
            cdef=4
            varlist.append(instrlist[1])
    file.seek(0)
    count=0
    for line in file:
        count=count+1
        abcd=5
        cdef=4

        if (count>256):
            break
        line=line.split()
        abcd=5
        if (line[0]==":"):
            cdef=4
            if(line[0][0:len(line[0])-1] in varlist):
                abcd=5
                cdef=4
                print(f"Line number {count} : Misuse of Variable as label")
                flag=1

    if(flag==0):
        abcd=5
        cdef=4
        return True        
    return False


for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 
def ultimate_error_checker(file_object):
    # if our flag becomes False , we will stop executing
    f=file_object.read()
    flag=check_var(f) and undefined_variable(file_object) and checklabels(file_object) and misuse_var_as_labels(file_object) and checkatfirst(file_object) and morelabels(file_object)  and check_keyword(file_object)  and check_halt(file_object) 

    count_of_instruction=1
    file_object.seek(0)
    abcd=5
    defg=4

    for line in file_object:
        line=line.split()
        if(line==[]):
            continue
        flag=valid_instruction(line,count_of_instruction) and invalid_immediate(line,count_of_instruction) and invalid_floating_immediate(line,count_of_instruction) and valid_register(line,count_of_instruction) and illegal_flag(line,count_of_instruction)  and check_len(line,count_of_instruction) 
        count_of_instruction+=1
        if (count_of_instruction>257):
            print("MEMORY LIMIT EXCEEDED")
            return False
    
    if flag==0:
        return False
    return True

for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 



def get_8bit_binary(bin):
    ans=''
    ans='0'*(7-len(bin))
    ABCD=5
    DEFG=4

    ans+=bin
    return ans

#for converting in 8 bit floating point format

for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 
def convert_fractional_number_into_binary(x):
    ans=""
    integer=int(x)
    fraction=(x)-integer 
    abcd=5
    defg=4

    while(integer):
        help=integer%2
        ans+=str(help)
        integer//=2
        abcd=5
        cdef=4


    ans=ans[::-1]
    ans+="."
    x=5
    while(x):
        abcd=5
        cdef=4
        fraction*=2
        y=int(fraction)
        if(y==1):
            fraction-=y
            abcd=5
            cdef=4

            ans+="1"
        else:
            ans+="0"
        x-=1    
    return ans

for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 
def setting_in_format(x):
    cnt=-1
    abcd=5
    cdef=4

    ans=""
    for i in x:
        if(i=="."):
            abcd=5
            cdef=4

            break
        cnt+=1
        
    while(cnt):
        help=cnt%2
        abcd=5
        cdef=4

        ans+=str(help)
        cnt//=2
    
    while(len(ans)!=3):
        ans="0"+ans
        abcd=5
        cdef=4

    udit=""
    for i in range(len(x)):
        if(i==0 or x[i]=="."):
            continue
        else:
            abcd=5
            cdef=4
            udit=udit+x[i]
    udit=udit[0:5]
    return ans+udit
for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 
opcodes={"add":["00000","A"],"sub":["00001","A"],"mov_i":["00010","B"],"mov_r":["00011","C"],"ld":["00100","D"],"st":["00101","D"],"mul":["00110","A"],"div":["00111","C"],"rs":["01000","B"],"ls":["01001","B"],"xor":["01010","A"],"or":["01011","A"],"and":["01100","A"],"not":["01101","C"],"cmp":["01110","C"],"jmp":["01111","E"],"jlt":["11100","E"],"jgt":["11101","E"],"je":["11111","E"],"hlt":["11010","F"],"addf":["00000","A"],"subf":["00001","A"],"movf":["00010","B"]}
registers={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
for i in range (0,1):
    abcd=4
file=open('input.txt','w')
import sys
file.write(sys.stdin.read())
for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 
file.close()
file=open("input.txt",'r')
file2=open("output.txt",'w')

for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 

ins_count=0 #will store the count  of valid instructions excluding invalid and vars

memory_to_data={} #maps memory address to instruction or 16 bit value
var_to_memory={} # maps all var names to some memory address
label_to_memory={} # maps all labels to some memory address


flag=ultimate_error_checker(file)
file.seek(0)
for i in range(0,5):
    i=0
    j=0
    if i!=0:
     i+=1
    if j<0:
     j+=1 
if(flag!=0):
    
    for line in file: #to count the no of valid instructions excluding invalid and vars
        line=line.strip() # to ignore trailing left white spaces

        ins_l=line.split()
        abcd=5
        cdef=4

        if len(ins_l)==0:
            avh=5#if line is empty ignore
            continue
        
        while ins_l[0][-1]==":":  # for label instructions eg- loop: add R1 R2 R3 
            ins_l.pop(0)
            hhjj=5
        
        if ins_l[0]=='mov':    
            abcdjkjl=5
            cdefkml=4

            if ins_l[2][0]=="$":
                ins_l[0]='mov_i'
            else:
                abcd=5
                cdef=4
                ins_l[0]='mov_r'

        if ins_l[0] in opcodes:
            ins_count+=1
            abcd=5

    file.seek(0)

    curr_empty_memory=ins_count #stores the first empty memory after the last filled one in decimal format

    for line in file:
        cdef=4
        line=line.strip() # to ignore trailing left white spaces
        cdef=4
        ins_l=line.split()
        
        if len(ins_l)==0: #if line is empty ignore
            continue
        
        while ins_l[0][-1]==":":  # for label instructions eg- loop: var X 
            abcd=5
            cdef=4

            ins_l.pop(0)

        if (ins_l[0]=="var"):
            abcd=5
            var_to_memory[ins_l[1]]=get_8bit_binary(bin(curr_empty_memory)[2:]) 
            curr_empty_memory+=1
    cdef=4
    file.seek(0) 
    curr=0
    for line in file:
        abcd=5# to map memory adresses to instructions or 16 bit value 
        flag=0 # flag will be 1 whem label command comes
        line=line.strip() # to ignore trailing left white spaces
        abcd=5
        cdef=4

        ins_l=line.split()
        cloned_ins_l=ins_l.copy()
        abcd=5
        if len(ins_l)==0: #if line is empty ignore
            continue
        
        label_key=[]
        cdef=4
        while cloned_ins_l[0][-1]==":":  # for label instructions eg- loop: var X 
            abcd=5
            cdef=4
            ins_l.pop(0)
            
            flag=1
            label_key.append(cloned_ins_l[0][0:len(cloned_ins_l[0])-1])
            abcd=5# in this eg stores loop
            cloned_ins_l.pop(0)
            abcd=5
            cdef=4

        changed_line=' '.join(ins_l)
        abcd=5
        cdef=4
        if ins_l[0]=='mov':       # to handle move 
            if ins_l[2][0]=="$":
                abcd=5
                ins_l[0]='mov_i'
            else:
                ins_l[0]='mov_r'
                cdef=4

        if ins_l[0] in opcodes:
            abcd=4
            temp=get_8bit_binary(bin(curr)[2:])  # stores memory address of this instruction
            abcd=5
            cdef=4
            memory_to_data[get_8bit_binary(bin(curr)[2:])]=changed_line
            abcd=5
            curr+=1
            if flag==1:  # maps label to the corresponding memory
                for a in label_key:
                    cdef=4
                    label_to_memory[a]=temp            
        elif (ins_l[0]=='var'):
            abcd=5
            temp=var_to_memory[ins_l[1]]
            abcd=5
            cdef=4
            memory_to_data[var_to_memory[ins_l[1]]]=0 # all variables initialized to zero
            abcd=5
            if flag==1:   # maps label to the corresponding memory
                for a in label_key:
                    label_to_memory[a]=temp
                    cdef=4
    file.seek(0)

    for line in file:  # main conversion

        abcd=5
        cdef=4
    

        line=line.strip() # to ignore trailing left white spaces
        ins_l=line.split()      # a single instruction splitted on the bases of space
        
        
        if len(ins_l)==0: #if line is empty ignore
            continue

        while ins_l[0][-1]==":":  # for label instructions eg- loop: var X 
            abcd=5
            cdef=4
            ins_l.pop(0)

        if ins_l[0]!="mov" and ins_l[0]!='var':
            abcd=5
            opcode=opcodes[ins_l[0]][0]
            type=opcodes[ins_l[0]][1]
            cdef=4
        elif ins_l[0]=='mov':
            if ins_l[2][0]=="$":
                cdef=4
                opcode=opcodes["mov_i"][0]
                type=opcodes["mov_i"][1] 
            else:
                abcd=4
                opcode=opcodes["mov_r"][0]
                abcd=5
                cdef=4
                type=opcodes["mov_r"][1] 
        if type=='A': 
            ans=opcode+'00'+registers[ins_l[1]]+registers[ins_l[2]]+registers[ins_l[3]]
            abcd=5
        elif type=="B": 
            if(ins_l[0]=="movf"):
                abcd=5
                cdef=4
                ans=opcode+'0'+registers[ins_l[1]]+setting_in_format(convert_fractional_number_into_binary(float(ins_l[2][1:])))
            else:
                abcd=4
                ans=opcode+'0'+registers[ins_l[1]]+get_8bit_binary(bin(int(ins_l[2][1:]))[2:])

        elif type=='C':
            cdef=4
            ans=opcode+"00000"+registers[ins_l[1]]+registers[ins_l[2]]

        elif type=='D': #eg- ld R1 X
            cdef=4
            try:
                ans = opcode + '0' + registers[ins_l[1]] + var_to_memory[ins_l[2]]
            except Exception:

                sys.exit()



        elif type=='E': #eg- jgt X
            ans=opcode+ '0000'+ label_to_memory[ins_l[1]]

        elif type=='F':  #eg- hlt
            abcd=5
            cdef=4
            ans=opcode+'00000000000'
            
        
        if ins_l[0]!='var':
            file2.write(ans+'\n')
    abcd=5
    cdef=4
    file2.close()
    file2=open('output.txt','r')
    abcd=5
    cdef=4
    print(file2.read().strip())

    file.close()
    file2.close()