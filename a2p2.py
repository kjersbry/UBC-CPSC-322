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


def varToString(varindex):
    if varindex==0:
        return "A"
    if varindex==1:
        return "B"
    if varindex==2:
        return "C"
    if varindex==3:
        return "D"
    if varindex==4:
        return "E"
    if varindex==5:
        return "F"
    if varindex==6:
        return "G"
    if varindex==7:
        return "H"
    else:
        return "-"

#Each iteration/step in the search
#returs false if the consistency check failed
def iter(values, variable, iteration):
    values = reset_from(variable, values)
    values[variable] = iteration
    print(varToString(variable) + "=" + str(iteration), end = ' ')    
    if not consistent(values):
        print("failure")
        return False
    elif variable == 7: # = H
        print("solution")
    return True

#DFS with pruning
def DFS():
    domain = [1,2,3,4]
    #values of [A, B, C, D, E, F, G, H]:
    var_values = [0,0,0,0,0,0,0,0]
    solutions = []
    num_fails = 0
    for A in domain:
        var_values = reset_from(0, var_values)
        var_values[0] = A #eller +=1, men da må du gjøre noe med linja over for å ikke overskrive A
        print(' ')
        print("A=" + str(A), end = ' ')
        for B in domain:
            if not iter(var_values, 1, B):
                num_fails += 1
                continue

            for C in domain:
                if not iter(var_values, 2, C):
                    num_fails += 1
                    continue                

                for D in domain:
                    if not iter(var_values, 3, D):
                        num_fails += 1
                        continue

                    for E in domain:
                        if not iter(var_values, 4, E):
                            num_fails += 1
                            continue

                        for F in domain:
                            if not iter(var_values, 5, F):
                                num_fails += 1
                                continue

                            for G in domain:
                                if not iter(var_values, 6, G):
                                    num_fails += 1
                                    continue 

                                for H in domain:
                                    if not iter(var_values, 7, H):
                                        num_fails += 1
                                        continue
                                    else:
                                        solutions.append([A, B, C, D, E, F])
    print("SOLUTIONS: ")
    print(solutions)
    print("FAILED CONSISTENCY CHECKS: " + str(num_fails))

#DFS()

def DFS_recursive(values, variable, solutions, failed_checks):
#    if not consistent:
#        return
    # do stuff to values
#    return DFS_recursive(values)

    print(varToString(variable) + "=" + str(values[variable]), end = ' ')
    #Termination:    
    if not consistent(values):
        print("failure")
        failed_checks += 1
        return (failed_checks, solutions)
    elif variable == 7 and values[variable] != 0: # = H
        print("solution")
        solutions.append(values)
        return (failed_checks, solutions)

    values = reset_from(variable + 1, values)
    if variable < 7: #not reached end
        variable += 1
    elif values[variable] < 4: #increment position
        values[variable] += 1
    elif values[0] < 4: #back to A
        values = reset_from(1, values)
        values[0] += 1
    else: #reached end?
        print("what")
        return (failed_checks, solutions)
    
    return (DFS_recursive(values, variable, solutions, failed_checks))


(failed_checks, solutions) = DFS_recursive([1,0,0,0,0,0,0,0], 0, [], 0)