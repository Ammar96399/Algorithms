def choixActivitesGloutonRecursif(s, f, i, n):
    if i <= n:
        m = i + 1
        while m <= n and s[m] < f[i]:
            m = m + 1
        
        print("The activity " + str(i) + " that starts at " + str(s[i]) + " and ends at " + str(f[i]))
        choixActivitesGloutonRecursif(s, f, m, n)
    
    else:
        return 0 

s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
choixActivitesGloutonRecursif(s, f, 0, len(s)-1)