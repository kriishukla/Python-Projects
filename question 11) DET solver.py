print("Define your matrix")
x = float(input("Is your matrix 2x2 or 3x3 or 4x4? enter 2,3 and 4 respectively "))

if x == 2:
        A = float(input("a11:"))
        B = float(input("a12:"))
        C = float(input("a21:"))
        D = float(input("a22:"))
        AD = A*D
        CB = C*B
        det = AD - CB

        print("value of determinant is",det)

if x == 3:

        A = float(input("a11:"))
        B = float(input("a12:"))
        C = float(input("a13:"))
        D = float(input("a21:"))
        E = float(input("a22:"))
        F = float(input("a23:"))
        G = float(input("a31:"))
        H = float(input("a32:"))
        I = float(input("a33:"))
        EI = E*I
        FH = F*H
        detEFHI = EI - FH
        BI = B*I
        CH = C*H
        detBCHI = BI - CH
        BF = B*F
        CE = C*E
        detBCEF = BF - CE

        DET = A * (detEFHI) - D * (detBCHI) + G * (detBCEF)
        print("value of determinant is",DET)
def deter(A,B,C,D,E,F,G,H,I):
        EI = E*I
        FH = F*H
        detEFHI = EI - FH
        BI = B*I
        CH = C*H
        detBCHI = BI - CH
        BF = B*F
        CE = C*E
        detBCEF = BF - CE

        DET = A * (detEFHI) - D * (detBCHI) + G * (detBCEF)
        return(DET)

        
if x==4:
    A = float(input("a11:"))
    B = float(input("a12:"))
    C = float(input("a13:"))
    D = float(input("a14:"))
    E = float(input("a21:"))
    F = float(input("a22:"))
    G = float(input("a23:"))
    H = float(input("a24:"))
    I = float(input("a31:"))
    J = float(input("a32:"))
    K = float(input("a33:"))
    L = float(input("a34:"))
    M = float(input("a41:"))
    N = float(input("a42:"))
    O = float(input("a43:"))
    P = float(input("a44:"))
    Q=deter(F,G,H,J,K,L,N,O,P)
    R=deter(E,G,H,I,K,L,M,O,P)
    S=deter(E,F,H,I,J,L,M,N,P)
    T=deter(E,F,G,I,J,K,M,N,O)
    print("value of determinant is",A*Q+B*R+C*S+D*T)
    
    
    