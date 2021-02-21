def choixActiviteIteratif(s, f, i): 
    n = len(s)
    print("The activity " + str(0) + " that starts at " + str(s[0]) + " and ends at " + str(f[0]))
    for m in range (i+1, n):
        if s[m] >= f[i]:
            print("The activity " + str(m) + " that starts at " + str(s[m]) + " and ends at " + str(f[m]))
            i = m
        
s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
choixActiviteIteratif(s, f, 0)