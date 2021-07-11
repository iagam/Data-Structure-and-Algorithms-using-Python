def naivegcd(m,n):
    
    # Store the factors of m in a separate list fm
    fm = []
    for i in range(1,m+1):
        if (m%i) == 0:
            fm.append(i)
            
    # Store the factors of n in a separate list fn
    fn = []
    for i in range(1,n+1):
        if (n%i) == 0:
            fn.append(i)
    
    # Create a common list of factors. Add common factors from fm and fn to cf
    cf = []
    for i in fm:
        if i in fn:
            cf.append(i)
    
    # Return the largest(rightmost) element from cf
    return cf[-1]