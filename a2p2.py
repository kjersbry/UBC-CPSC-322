#true if any of the values are zero
def isZero(*values):
    for i in values:
        if i == 0:
            return True
    return False


#true if values assigned so far are consistent
def consistent(values):
    A = values[0]
    B = values[1]
    C = values[2]
    D = values[3]
    E = values[4]
    F = values[5]
    G = values[6]
    H = values[7]

    if isZero(D):
        #D=0 means max A,B,C are assigned. There are no constraints w only A, B, C
        return True 

    #check all constraints
    if (isZero(A,G) or A >= G) and (isZero(G, C) or abs(G-C)==1) and (isZero(D, C) or D!=C):
        if (isZero(G,F) or G!=F) and (isZero(E, F) or abs(E-F)%2!=0) and (isZero(A, H) or A < H):
            if (isZero(H, C) or abs(H-C)%2==0) and (isZero(E, C) or E!=C) and (isZero(H, F) or H!=F):
                if (isZero(F, B) or abs(F-B)==1) and (isZero(E, D) or E < (D-1)) and (isZero(C, F) or C!=F):
                    if (isZero(G, H) or G < H) and (isZero(D, G) or D>=G) and (isZero(E, H) or E!=(H-2)) and (isZero(D, F) or D!=F):
                        return True
    return False
    
def reset_from(index, lst):
    for i in range(index, len(lst)):
        lst[i]=0
    return lst

#forslag iter-funksjon:
#returner false hvis failed check


def DFS():
    domain = [1,2,3,4]
    #variables = [A, B, C, D, E, F, G, H]
    var_values = [0,0,0,0,0,0,0,0]
    solutions = []
    num_fails = 0
    for A in domain:
        var_values = reset_from(0, var_values)
        var_values[0] = A #eller +=1, men da må du gjøre noe med linja over for å ikke overskrive A
        print(' ')
        print("A=" + str(A), end = ' ')
        #print(var_values)
        for B in domain:
            var_values = reset_from(1, var_values)
            var_values[1] = B
            print("B=" + str(B), end = ' ')    
            #print(var_values)        
            if not consistent(var_values):
                print("failure")
                num_fails += 1
                continue

            for C in domain:
                var_values = reset_from(2, var_values)
                var_values[2] = C
                print("C=" + str(C), end = ' ')
                #print(var_values)
                if not consistent(var_values):
                    print("failure")
                    num_fails += 1
                    continue                

                for D in domain:
                    var_values = reset_from(3, var_values)
                    var_values[3] = D
                    print("D=" + str(D), end = ' ')
                    #print(var_values)
                    if not consistent(var_values):
                        print("failure")
                        num_fails += 1
                        continue

                    for E in domain:
                        var_values = reset_from(4, var_values)
                        var_values[4] = E
                        print("E=" + str(E), end = ' ')
                        #print(var_values)
                        #if E == 3:
                        #    return


                        if not consistent(var_values):
                            print("failure")
                            num_fails += 1
                            continue 

                        for F in domain:
                            var_values = reset_from(5, var_values)
                            var_values[5] = F
                            print("F=" + str(F), end = ' ')
                            #print(var_values)
                            if not consistent(var_values):
                                print("failure")
                                num_fails += 1
                                continue 

                            for G in domain:
                                var_values = reset_from(6, var_values)
                                var_values[6] = G
                                print("G=" + str(G), end = ' ')
                                #print(var_values)
                                if not consistent(var_values):
                                    print("failure")
                                    num_fails += 1
                                    continue 

                                for H in domain:
                                    var_values = reset_from(7, var_values)
                                    var_values[7] = H
                                    print("H=" + str(H), end = ' ')
                                    #print(var_values)
                                    if not consistent(var_values):
                                        print("failure")
                                        num_fails += 1
                                        continue 
                                    else:
                                        print("solution")
                                        solutions.append([A, B, C, D, E, F])

    #report solutions
    #report failing consistency checks
    print("SOLUTIONS: ")
    print(solutions)
    print("FAILED CONSISTENCY CHECKS: " + str(num_fails))



#def DFS_recursive(values):
#    if not consistent:
#        return
    # do stuff to values
#    return DFS_recursive(values)

DFS()