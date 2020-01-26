from cmath import sqrt
#It supports only when a,b and c are real number and a != 0
a,b,c = map(int, input("Enter the three coefficients").split())

d = b*b-4*a*c

sol1 = (-b-sqrt(d))/2*a
sol2 = (-b+sqrt(d))/2*a

print("Solutions are {0} and {1}".format(sol1,sol2))
