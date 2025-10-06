import VectorCalculator as mvcalc 
import math  
import sympy as sp 

############################################problem 71 pg. 910 

####################part a  

#state given quantities from problem statement 

rampdist=259 #distance along ramp is 259ft
rampangle=(-1)*(math.radians(23)) #ramp is at an angle of 23 degrees below horizontal
xi = [0,0] #setting initial position at 0,0
xf = [rampdist*math.cos(rampangle),rampdist*math.sin(rampangle)]  #setting final position at 259ft down the ramp using the angle
a = ["0","-32"] #setting acceleration vector components (in ft/s^2)

###all this above looks like were just setting up something VERY similar to physics

#get initial expressions for x- and y-velocities and positions 

v = mvcalc.function_integral(a, ["t"], "t") #using my calculator function #this integrates acceleration to get velocity
v[0] = str(v[0]) + " + v_0x" #adding the result of integration for initial x-velocity
v[1] = str(v[1]) + " + v_0y" #adding the result of integration for initial y-velocity

x = mvcalc.function_integral(v, ["t"], "t") #using my calculator function #this integrates velocity to get position equations
x[0] = str(x[0]) + " + " + str(xi[0]) #adding the result of integration for initial x-position, same as above, but also adding initial x position
x[1] = str(x[1]) + " + " + str(xi[1]) #adding the result of integration for initial y-position, same as above, but also adding initial y position

#solving for v_0x and v_0y 

t = sp.symbols('t') #lowkey idk what this does, it looks like it just defines t as a symbol for sympy to use

x_expr = sp.sympify(x[0]) #again, idk what the simpify functon does, but it seems to convert the string into something sympy can work with
result_x = x_expr.subs(t, 2.9) #substituting t=2.9s into the x position equation
solution_x = sp.solve(sp.Eq(result_x, xf[0]), 'v_0x') #gets the initital x-velocity using the intital x position
v0x = solution_x[0] #sets the initial x-velocity to a variable
v[0] = v[0].replace("v_0x", str(v0x)) # replaces the initial x-velocity in the velocity equation with the value we just found

y_expr = sp.sympify(x[1]) #same as above, but for y position, sets up the equation
result_y = y_expr.subs(t, 2.9) #substituting t=2.9s into the y position equation
solution_y = sp.solve(sp.Eq(result_y, xf[1]), 'v_0y') #gets the initital y-velocity using the intital y position
v0y = solution_y[0]  #sets the initial y-velocity to a variable
v[1] = v[1].replace("v_0y", str(v0y)) # replaces the initial y-velocity in the velocity equation with the value we just found

#final solution to problem 


v0 = math.sqrt(v0x**2 + v0y**2) #finding the magnitude of the initial velocity vector using the v0x and v0y just found
angle = math.degrees(math.atan(v0y/v0x)) #finding the angle of the initial velocity vector using x0x and v0y
print("v0 =",v0,"angle =",angle) #prints!

###########################################part b 

#finding the total distance travelled 

speed = "sqrt((" + str(v[0]) + ")**2 + (" + str(v[1]) + ")**2)" #finds speed using magnitude formula of velocity vector
d = mvcalc.function_definite_integral([speed], ["t"], "t", 0, 2.9) #using my calculator function #integrated speed from t=0 to t=2.9s to get total distance travelled
print("The distance travelled is",d[0]) #prints!