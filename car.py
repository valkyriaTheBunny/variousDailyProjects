def cons(a, b): #provided code for the constuction of cons
    def pair(f):
        return f(a,b)
    return pair

def car(cons): #takes in the cons function
    #pulls the first item input to the cons function, and returns it
    return cons(lambda a, b: a) 

def cdr(cons):
    #pulls the second/last item input to the cons function,
    #and returns it
    return cons(lambda a, b: b)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))