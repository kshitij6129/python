user=int(input("choose \n1 for work\n2 for kinetic energy\n3 for potential energy\n4 for total energy:"))
if (user==1):
    f=int(input("enter the amount of force:"))
    d=int(input("enter the amount of displacement:"))
    def Work(f,d):
        work=(f*d)
        return work
    obj1=Work(f,d)
    print("work=",obj1)
    Work(f,d)
elif (user==2):
    m=int(input("enter the amount of mass:"))
    v=int(input("enter the amount of velocity:"))
    def kinetic_energy(m,v):
        k=(1/2*m*(v*v))
        return k
    obj1=kinetic_energy(f,d)
    print("kinetic energy=",obj1)
    kinetic_energy(m,v)
elif (user==3):
    m=int(input("enter the amount of mass:"))
    h=int(input("enter the amount of height:"))
    g=10
    def potential_energy(m,h,g):
        p=m*g*h
        return p
    obj1=potential_energy(m,v,g)
    print("potential energy=",obj1)
    potential_energy(m,h,g)
elif (user==4):
    m1=int(input("enter the amount of mass:"))
    v=int(input("enter the amount of velocity:"))
    m2=int(input("enter the amount of mass:"))
    h=int(input("enter the amount of height:"))
    g=10
    def total_energy(m,h,g,v):
        t=(1/2*m*(v*v))+(m*g*h)
        return t
    obj1=total_energy(m,v,g,v)
    print("total energy=",obj1)
    total_energy(m,h,g,v)
