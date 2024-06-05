def towerOfHanoi(n,s,e,d):
    if n==1:
        print(n,"from",s,"to",d)
        print("hello")
        return 
    towerOfHanoi(n-1,s,d,e)
    print(n,"from",s,"to",d)
    towerOfHanoi(n-1,e,s,d)
towerOfHanoi(4,"source","extra","destiny")