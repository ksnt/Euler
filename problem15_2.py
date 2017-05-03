print (reduce(lambda x,y: x * y, [i for i in range(1,41)])/ (reduce(lambda x,y: x*y, [j for j in range(1,21)])**2))
