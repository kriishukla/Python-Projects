





import sys
import math

def floorPart(number: float) -> int:
    return math.floor(number)

def fractionalPart(number: float) -> float:
    return number - math.floor(number)


def f_to_bin(num: float, bias: int = 3) -> str:
    num = float(num)

    whole = floorPart(num)
    decimal = fractionalPart(num)

    bin_whole = bin(whole)[2:]
    bin_decimal = ''

    # i = 0
    # while i < 8 and (decimal - int(decimal)):
    #     decimal *= 2
    #     bin_decimal += str(int(decimal))
    #     decimal = (decimal - int(decimal))
    #     i += 1
    for i in range (8):
        if (decimal - int(decimal)):
            decimal *= 2
            bin_decimal += str(int(decimal))
            decimal = (decimal - int(decimal))
        else:
            break
        

    bin_decimal = bin_decimal + ('0' * (8 - len(bin_decimal)))

    if whole > 0:
        exp = len(bin_whole) - 1 + bias
        mantissa = (bin_whole[1:] + bin_decimal)[:5]
    else:
        count = 0
        while bin_decimal[count] == '0':
            count += 1
        exp = -(count + 1) + bias
        mantissa = bin_decimal[count + 1: count + 6]

    bin_exp = bin(exp)[2:].zfill(3)

    return bin_exp + mantissa

def convertIntegerToDecimal(binary):
    n = 0
    for i in range(len(binary)):
        n += int(binary[- i - 1]) * (2 ** i)
    return n


def convertFloatingToDecimal(binary, bias=3):
    exp = convertIntegerToDecimal(binary[:3]) - bias
    mantissa = binary[3:]
    p = 1
    for i in range(5):
        p += int(mantissa[i]) * (2 ** -(i + 1))
    number = p * (2 ** exp)
    return number


reg = [0,0,0,0,0,0,0,0]

# reg = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]
flag = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
pc = 0
# file=open ("bonus_hyp.txt","r")
# i=file.read()
# ins=i.split("\n")
ins = sys.stdin.readlines()
for i in range(len(ins)):
    ins[i]=ins[i].strip()

    

MEM = ["0000000000000000"]*128

for i in range (len(ins)):
    MEM[i] = ins[i]

#krishna part 3


# def get_required_code(instruction: str) -> list[str, str]:
#     opcode = instruction[:5]
#     reg1 = instruction[5:8]
#     mem = instruction[8:16]
#     return REGISTERS[reg1], mem





def b_to_d_7(binary):
    decimal = 0
    binary = str(binary)  # Ensure binary is a string
    
    if len(binary) != 7:
        raise ValueError("Invalid binary input. Must be a 7-bit binary number.")
    
    for i in range(7):
        if binary[i] == '1':
            decimal += 2**(6-i)
    
    return decimal

def b_to_d_3(binary):
    decimal = 0
    power = 0
    for digit in reversed(binary):
        if digit == '1':
            decimal =decimal+ 2 ** power
        power += 1
    return decimal

def d_to_b_7(decimal):
    if decimal != 0:
        pass
    
    else:
        return '0000000'
    
    binary = ''
    for i in range (0,1000000):
        if decimal <= 0:
            break 
    
        binary = str(decimal % 2) + binary
        decimal //= 2
    binary= "0"*(7-len(binary))+binary
    return binary

def d_to_b_16(decimal):
    if decimal != 0:
        pass
    
    else:
        return '0000000000000000'
    
    binary = ''
    for i in range (0,1000000):
        if decimal <= 0:
            break 
    
        binary = str(decimal % 2) + binary
        decimal //= 2
    binary= "0"*(16-len(binary))+binary
    return binary

def binf(immediate: float) -> str:
    mantissa = ""
    exponent = -5
    if not 1 <= immediate <= 252:
        flag[-4] = 1
        print("Overflow")
        if immediate < 1:
            return "0" * 8
        else:
            return "1" * 8
    while 2 ** exponent <= immediate:
        exponent += 1
    exponent -= 1
    num = immediate / 2 ** exponent - 1
    for _ in range(5):
        num *= 2
        if num < 1:
            mantissa += "0"
        else:
            mantissa += "1"
            num -= 1
    if num != 0:
        print("Overflow triggered")
        flag[-4] = 1
    return bin(exponent)[2:].zfill(3) + mantissa

def handle_float(value: str) -> float:
    exponent, mantissa = value[:3], value[3:]
    value = 0
    for i in range(5):
        value += int(mantissa[i]) * 2 ** (-i - 1)
    return (1 + value) * 2 ** int(exponent, base=2)
 # code for floating point by krishna  
 
# def handle_overflow() -> None:
#     REGISTER[7] = "0"*12 + "1000"
    
# def binf(immediate: float) -> str:
#     mantissa = ""
#     exponent = -5
#     if not 1 <= immediate <= 252:
#         handle_overflow()
#         if immediate < 1:
#             return "0" * 8
#         else:
#             return "1" * 8
#     while 2 ** exponent <= immediate:
#         exponent += 1
#     exponent -= 1
#     num = immediate / 2 ** exponent - 1
#     for _ in range(5):
#         num *= 2
#         if num < 1:
#             mantissa += "0"
#         else:
#             mantissa += "1"
#             num -= 1
#     if num != 0:
#         handle_overflow()
#     return bin(exponent)[2:].zfill(3) + mantissa


# def handle_float(value: str) -> float:
#     exponent, mantissa = value[:3], value[3:]
#     value = 0
#     for i in range(5):
#         value += int(mantissa[i]) * 2 ** (-i - 1)

#     return (1 + value) * 2 ** int(exponent, base=2)
# part 2 ends
while (True):


    instruction = ins[pc]

    if instruction[0:5] == "10011": # to calc hypotenuse of a triangle
        reg_num_1 = b_to_d_3(instruction[7:10])
        reg_num_2 = b_to_d_3(instruction[10:13])
        reg_num_3 = b_to_d_3(instruction[13:16])
        reg[reg_num_1] = int(((reg[reg_num_2] ** 2)+(reg[reg_num_3]) **2)**(1/2))
        if (reg[reg_num_1] >127 ):
            flag[-4] = 1
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            reg[reg_num_1] = 0   
        else:
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            flag[-4] = 0    # maybe all flags to be down see later
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc+=1
    if instruction[0:5] == "10101": # to calc ar of a rectangle
        reg_num_1 = b_to_d_3(instruction[7:10])
        reg_num_2 = b_to_d_3(instruction[10:13])
        reg_num_3 = b_to_d_3(instruction[13:16])
        reg[reg_num_1] = reg[reg_num_2] *reg[reg_num_3] 
        if (reg[reg_num_1] >127 ):
            flag[-4] = 1
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            reg[reg_num_1] = 0   
        else:
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            flag[-4] = 0    # maybe all flags to be down see later
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc+=1
        # ar of triangle
    if instruction[0:5] == "10110": 
        reg_num_1 = b_to_d_3(instruction[7:10])
        reg_num_2 = b_to_d_3(instruction[10:13])
        reg_num_3 = b_to_d_3(instruction[13:16])
        reg[reg_num_1] = int((reg[reg_num_2] *reg[reg_num_3] )*1/2)
        if (reg[reg_num_1] >127 ):
            flag[-4] = 1
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            reg[reg_num_1] = 0   
        else:
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            flag[-4] = 0    # maybe all flags to be down see later
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc+=1
    
    # exponent
    if instruction[0:5] == "10111":
        reg_num_1 = b_to_d_3(instruction[7:10])
        reg_num_2 = b_to_d_3(instruction[10:13])
        reg_num_3 = b_to_d_3(instruction[13:16])
        reg[reg_num_1] = reg[reg_num_2] ** reg[reg_num_3]
        if (reg[reg_num_1] >127 ):
            flag[-4] = 1
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            reg[reg_num_1] = 0   
        else:
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            flag[-4] = 0    # maybe all flags to be down see later
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc+=1
    
    #area of parabola
    if instruction[0:5] == "10100":
        reg_num_1 = b_to_d_3(instruction[7:10])
        reg_num_2 = b_to_d_3(instruction[10:13])
        reg_num_3 = b_to_d_3(instruction[13:16])
        print
        reg[reg_num_1] = int(((reg[reg_num_3] ** 3) - (reg[reg_num_2]**3))/3)
        if (reg[reg_num_1] >127 ):
            flag[-4] = 1
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            reg[reg_num_1] = 0   
        else:
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            flag[-4] = 0    # maybe all flags to be down see later
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc+=1
    
    # # increment
    # if instruction[0:5] == "10100":
    #     reg_num_1 = b_to_d_3(instruction[13:16])
    #     base=math.e
    #     reg[reg_num_1] =reg[reg_num_1] + 1

    #     if (reg[reg_num_1] >127 ):
    #         flag[-4] = 1
    #         flag[-1] = 0
    #         flag[-2] = 0
    #         flag[-3] = 0
    #         reg[reg_num_1] = 0   
    #     else:
    #         flag[-1] = 0
    #         flag[-2] = 0
    #         flag[-3] = 0
    #         flag[-4] = 0    # maybe all flags to be down see later
    #     flag_str = "".join(str(i) for i in flag)
    #     s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
    #     print(s)
    #     pc+=1

    # movf
    if instruction[0:5] == "10010":
        reg_num_1 = int(b_to_d_3(instruction[5:8]))
        imm=(convertFloatingToDecimal(instruction[8:]))
        reg[reg_num_1]=imm
        flag[-1] = 0
        flag[-2] = 0
        flag[-3] = 0
        flag[-4] = 0
        
        flag_str = "".join(str(i) for i in flag)

        s = d_to_b_7(pc) +"        "+ f_to_bin(reg[0]) +" " + f_to_bin(reg[1])+" " + f_to_bin(reg[2]) +" "+ f_to_bin(reg[3]) +" "+ f_to_bin(reg[4])+" " + f_to_bin(reg[5])+" " + f_to_bin(reg[6]) + " " + flag_str
        print(s)
        pc+=1
        
    
    # addf
    if instruction[0:5] == "10000" :
        reg_num_1 = int(b_to_d_3(instruction[7:10]))
        reg_num_2 = int(b_to_d_3(instruction[10:13]))
        reg_num_3 = int(b_to_d_3(instruction[13:])) 
        reg[reg_num_1] = reg[reg_num_2] + reg[reg_num_3]
        if (reg[reg_num_1] >127 ):
            flag[-4] = 1
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            reg[reg_num_1] = 0   
        else:
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            flag[-4] = 0    # maybe all flags to be down see later
        flag_str = "".join(str(i) for i in flag)
        print(f_to_bin(0.125))
        s = d_to_b_7(pc) +"        "+ f_to_bin(reg[0]) +" " + f_to_bin(reg[1])+" " + f_to_bin(reg[2]) +" "+ f_to_bin(reg[3]) +" "+ f_to_bin(reg[4])+" " + f_to_bin(reg[5])+" " + f_to_bin(reg[6]) + " " + flag_str
        print(s)
        pc +=1
        
        
    # subf
    if (instruction[0:5] == "10001"):
        reg_num_1 = int(b_to_d_3(instruction[7:10]))
        reg_num_2 = int(b_to_d_3(instruction[10:13]))
        reg_num_3 = int(b_to_d_3(instruction[13:])) 
        reg[reg_num_1] = reg[reg_num_2] - reg[reg_num_3]
        if (reg[reg_num_1] >127  or reg[reg_num_1]<0 ):
            flag[-4] = 1
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            reg[reg_num_1] = 0   
        else:
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            flag[-4] = 0    # maybe all flags to be down see later
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc +=1 
    

    if instruction[0:5] == "11000":  # right shift
        reg_num_1= b_to_d_3(instruction[5:8])
        imm = b_to_d_7(instruction[8:])
        value1 = int(reg[reg_num_1], base=2)
        value1 >>= imm
        reg[reg_num_1] = d_to_b_16(value1)
        flag[-4] = 0
        flag[-3] = 0
        flag[-2] = 0
        flag[-1] = 0
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc += 1
    
    if instruction[0:5] == "11001":  # left shift
        reg_num_1 = b_to_d_3(instruction[5:8])
        imm = b_to_d_7(instruction[8:])
        value1 = int(reg[reg_num_1], base=2)
        value1 <<= imm
        reg[reg_num_1] = d_to_b_16(value1)
        flag[-4] = 0
        flag[-3] = 0
        flag[-2] = 0
        flag[-1] = 0
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc += 1
    
    # halt
    if (instruction[0:5] == "11010"):
        flag[-1] = 0
        flag[-2] = 0
        flag[-3] = 0
        flag[-4] = 0
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        break
    
    # load
    if (instruction[0:5] == "00100"):
        reg_num_1 = int(b_to_d_3(instruction[6:9]))
        MEM_INDEX = int(b_to_d_7(instruction[9:16]))
        # reg[reg_num_1] = MEM[MEM_INDEX]
        reg[reg_num_1] = b_to_d_3(str(MEM[MEM_INDEX]))
        flag[-1] = 0
        flag[-2] = 0
        flag[-3] = 0
        flag[-4] = 0
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc +=1
    
    # store
    if (instruction[0:5] == "00101"):
        reg_num_1 = int(b_to_d_3(instruction[6:9]))
        MEM_INDEX = int(b_to_d_7(instruction[9:16]))
        # MEM[MEM_INDEX] = reg[reg_num_1]
        val_binary = d_to_b_16(reg[reg_num_1])
        MEM[MEM_INDEX] = val_binary
        flag[-1] = 0
        flag[-2] = 0
        flag[-3] = 0
        flag[-4] = 0
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc +=1
    

    ##ADD
    if (instruction[0:5] == "00000"):
        reg_num_1 = int(b_to_d_3(instruction[7:10]))
        reg_num_2 = int(b_to_d_3(instruction[10:13]))
        reg_num_3 = int(b_to_d_3(instruction[13:])) 
        reg[reg_num_1] = reg[reg_num_2] + reg[reg_num_3]
        if (reg[reg_num_1] >127 ):
            flag[-4] = 1
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            reg[reg_num_1] = 0   
        else:
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            flag[-4] = 0    # maybe all flags to be down see later
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc +=1
    ##SUB
    if (instruction[0:5] == "00001"):
        reg_num_1 = int(b_to_d_3(instruction[7:10]))
        reg_num_2 = int(b_to_d_3(instruction[10:13]))
        reg_num_3 = int(b_to_d_3(instruction[13:])) 
        reg[reg_num_1] = reg[reg_num_2] - reg[reg_num_3]
        if (reg[reg_num_1] >127  or reg[reg_num_1]<0 ):
            flag[-4] = 1
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            reg[reg_num_1] = 0   
        else:
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            flag[-4] = 0    # maybe all flags to be down see later
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc +=1   
        ##MUL
    if (instruction[0:5] == "00110"):
        reg_num_1 = int(b_to_d_3(instruction[7:10]))
        reg_num_2 = int(b_to_d_3(instruction[10:13]))
        reg_num_3 = int(b_to_d_3(instruction[13:])) 
        reg[reg_num_1] = reg[reg_num_2] * reg[reg_num_3]
        if (reg[reg_num_1] >127 ):
            flag[-4] = 1
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            reg[reg_num_1] = 0   
        else:
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            flag[-4] = 0    # maybe all flags to be down see later
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc +=1
        ##DIV       
    if (instruction[0:5] == "00111"):
        reg_num_1 = int(b_to_d_3(instruction[10:13]))
        reg_num_2 = int(b_to_d_3(instruction[13:16]))
        if (reg[reg_num_2] == 0):
            flag[-4] = 1
            reg[0] = 0
            reg[1] = 0
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
        
        
              
        else:
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            flag[-4] = 0    # maybe all flags to be down see later
            reg[0] = reg[reg_num_1] // reg[reg_num_2]
            reg[1] = reg[reg_num_1] % reg[reg_num_2]
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        pc +=1
    


    ###KEHSAV ADD CODE FOR MOV + ALL GATES

    # or

    if (instruction[0:5] == "01011"):
        reg_num_1 = int(b_to_d_3(instruction[7:10]))
        reg_num_2 = int(b_to_d_3(instruction[10:13]))
        reg_num_3 = int(b_to_d_3(instruction[13:])) 
        reg[reg_num_1]=reg[reg_num_2]|reg[reg_num_3]
        flag[-1] = 0
        flag[-2] = 0
        flag[-3] = 0
        flag[-4] = 0
        

        
        flag_str = "".join(str(i) for i in flag)

        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc+=1


    #xor
    if (instruction[0:5] == "01010"):
        reg_num_1 = int(b_to_d_3(instruction[7:10]))
        reg_num_2 = int(b_to_d_3(instruction[10:13]))
        reg_num_3 = int(b_to_d_3(instruction[13:])) 
        reg[reg_num_1]=reg[reg_num_2]^reg[reg_num_3]
        flag[-1] = 0
        flag[-2] = 0
        flag[-3] = 0
        flag[-4] = 0
        

        
        flag_str = "".join(str(i) for i in flag)

        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc+=1


    #and 
    if (instruction[0:5] == "01100"):
        reg_num_1 = int(b_to_d_3(instruction[7:10]))
        reg_num_2 = int(b_to_d_3(instruction[10:13]))
        reg_num_3 = int(b_to_d_3(instruction[13:])) 
        reg[reg_num_1]=reg[reg_num_2]&reg[reg_num_3]
        flag[-1] = 0
        flag[-2] = 0
        flag[-3] = 0
        flag[-4] = 0
        

        
        flag_str = "".join(str(i) for i in flag)

        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc+=1

    
    # mov imm
    if (instruction[0:5] == "00010"):
        reg_num_1 = int(b_to_d_3(instruction[6:9]))
        imm=int(b_to_d_3(instruction[9:]))
        reg[reg_num_1]=imm

        flag[-1] = 0
        flag[-2] = 0
        flag[-3] = 0
        flag[-4] = 0
        
        flag_str = "".join(str(i) for i in flag)

        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc+=1


    #mov reg 
    if (instruction[0:5] == "00011"):
        flag_str1 = "".join(str(i) for i in flag)
        reg[7] = b_to_d_3(flag_str1)

        reg_num_1 = int(b_to_d_3(instruction[10:13]))
        reg_num_2 = int(b_to_d_3(instruction[13:]))
        reg[reg_num_1]=reg[reg_num_2]

        flag[-1] = 0
        flag[-2] = 0
        flag[-3] = 0
        flag[-4] = 0
        
        flag_str = "".join(str(i) for i in flag)

        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc+=1
    
    
    
#    ###KRISHNA ADD YOUR CODE HERE
#        elif instruction[0:5] == "00100": #ld
#         reg1, mem = get_required_code(instruction)
#         reg[register(reg1)] = MEMORY[int(mem, base=2)]
        
#         flag_str = "".join(str(i) for i in flag)
#         s = d_to_b_7(pc) + "" + d_to_b_16(reg[0]) + "" + d_to_b_16(reg[1]) + "" + d_to_b_16(reg[2]) + "" + d_to_b_16(reg[3]) + "" + d_to_b_16(reg[4]) + "" + d_to_b_16(reg[5]) + "" + d_to_b_16(reg[6]) + "" + flag_str
#         print(s)
#         pc += 1

#     # STORE
#     elif instruction[0:5] == "00101":
#         reg1, mem = type_D(instruction)
#         MEMORY[int(mem, base=2)] = reg[register(reg1)]
        
#         flag_str = "".join(str(i) for i in flag)
#         s = d_to_b_7(pc) + "" + d_to_b_16(reg[0]) + "" + d_to_b_16(reg[1]) + "" + d_to_b_16(reg[2]) + "" + d_to_b_16(reg[3]) + "" + d_to_b_16(reg[4]) + "" + d_to_b_16(reg[5]) + "" + d_to_b_16(reg[6]) + "" + flag_str
#         print(s)
#         pc += 1
#         #part 1 ends
    


    
      
    # cmp  
    if (instruction[0:5] == "01110"):
        reg_num_1 = int(b_to_d_3(instruction[10:13]))
        reg_num_2 = int(b_to_d_3(instruction[13:16]))
        if reg[reg_num_1] == reg[reg_num_2]:
            flag[-1] = 1
            flag[-2] = 0
            flag[-3] = 0
            flag[-4] = 0
        elif reg[reg_num_1] < reg[reg_num_2]:
            flag[-3] = 1
            flag[-2] = 0
            flag[-1] = 0
            flag[-4] = 0
        elif reg[reg_num_1] > reg[reg_num_2]:
            flag[-2] = 1
            flag[-1] = 0
            flag[-3] = 0
            flag[-4] = 0
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc +=1
        
    # unconditional jump
    if (instruction[0:5] == "01111"):
        flag[-1] =0   #verify changes in the flag later
        flag[-2] =0
        flag[-3] =0
        flag[-4] =0
        
        flag_str = "".join(str(i) for i in flag)
        s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
        print(s)
        pc = int(b_to_d_7(instruction[9:16]))
        
        
   
    #jump if less then    
    if (instruction[0:5] == "11100"):
        if flag[-3] == 1:
            flag[-1] = 0
            flag[-2] = 0
            flag[-3] = 0
            flag[-4] = 0    # maybe all flags to be down see later
            flag_str = "".join(str(i) for i in flag)
            s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
            print(s)
            pc = int(b_to_d_7(instruction[9:16]))
            
            
        else:
            flag[-1] =0   #verify changes in the flag later
            flag[-2] =0
            flag[-3] =0
            flag[-4] =0
            flag_str = "".join(str(i) for i in flag)
            s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
            print(s)
            pc +=1
            
            
    
    #jump if greater then   
    if (instruction[0:5] == "11101"):
        if flag[-2] == 1:
            flag[-1] =0   #verify changes in the flag later
            flag[-2] =0
            flag[-3] =0
            flag[-4] =0
            flag_str = "".join(str(i) for i in flag)
            s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
            print(s)
            pc = int(b_to_d_7(instruction[9:16]))
            # flag[-2] = 0
        else:
            flag[-1] =0   #verify changes in the flag later
            flag[-2] =0
            flag[-3] =0
            flag[-4] =0
            flag_str = "".join(str(i) for i in flag)
            s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
            print(s)
            pc +=1
            
    
    # jump if equal   
    if (instruction[0:5] == "11111"):
        if flag[-1] == 1:
            flag[-1] =0   #verify changes in the flag later
            flag[-2] =0
            flag[-3] =0
            flag[-4] =0
            flag_str = "".join(str(i) for i in flag)
            s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
            print(s)
            pc = int(b_to_d_7(instruction[9:16]))
            # flag[-1] = 0
        else:
            flag[-1] =0   #verify changes in the flag later
            flag[-2] =0
            flag[-3] =0
            flag[-4] = 0
            s = d_to_b_7(pc) +"        "+ d_to_b_16(reg[0]) +" " + d_to_b_16(reg[1])+" " + d_to_b_16(reg[2]) +" "+ d_to_b_16(reg[3]) +" "+ d_to_b_16(reg[4])+" " + d_to_b_16(reg[5])+" " + d_to_b_16(reg[6]) + " " + flag_str
            print(s)
            pc +=1
            
        
            
            

# while (True):
#     instruction = ins[pc]
#     if (instruction[0:5] == "11010"):
#         break
#     # addition
#     if (instruction[0:5] == "00000"):
#         reg_num_1 = int(b_to_d_3(instruction[7:10]))
#         reg_num_2 = int(b_to_d_3(instruction[10:13]))
#         reg_num_3 = int(b_to_d_3(instruction[13:])) 
#         reg[reg_num_1] = reg[reg_num_2] + reg[reg_num_3]
#         if (reg[reg_num_1] >127 ):
#             flag[-4] = 1
#             reg[reg_num_1] = 0   
#         else:
#             flag[-4] = 0
#         flag_str = "".join(str(i) for i in flag)
#         s = d_to_b_7(pc) +""+ d_to_b_16(reg[0]) +"" + d_to_b_16(reg[1])+"" + d_to_b_16(reg[2]) +""+ d_to_b_16(reg[3]) +""+ d_to_b_16(reg[4])+"" + d_to_b_16(reg[5])+"" + d_to_b_16(reg[6]) + "" + flag_str
#         print(s)
#         pc +=1
# import numpy as np
# np.array[1,1,1]

# print ("congratulation all test cases passed marks = 100/100")
for i in range (len(MEM)):
    print(MEM[i])
