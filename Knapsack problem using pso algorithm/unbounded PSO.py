import random
import math

#--- COST FUNCTION 
# function we are attempting to optimize (minimize)

val = [35, 85, 135, 10, 25, 2, 94]
kg = [2, 3, 9, 0.5, 2, 0.1, 4]
maxKg = 25


    

def func1_ev(x):
      t = prof(x)
      return w_kg(x, t)
  


def prof(x):
    total_prof = 0
    for i in range(len(x)):
        total_prof += x[i] * val[i]  
    return total_prof


def w_kg(x, profit):
    total_kg = 0
    for i in range(len(x)):
        total_kg += x[i] * kg[i] 

    if total_kg <= maxKg:
        return profit - 100*(min(0,(maxKg-total_kg)))
    elif total_kg > maxKg:
        return -profit
   




class Particle:
    def __init__(self,initial):
        self.position_i=[]          # particle position
        self.velocity_i=[]          # particle velocity
        self.pos_best_i=[]          # best position individual
        self.fit_best_i=-1          # best fitness individual
        self.fit_i=-1               # fitness individual

        for i in range(0,num_dimensions):
            self.velocity_i.append(random.uniform(0,1))
            self.position_i.append(initial[i])

    # evaluate current fitness
    def evaluate(self,costFunc):
        self.fit_i=costFunc(self.position_i)

        # check to see if the current position is an individual best
        if self.fit_i > self.fit_best_i:
            self.pos_best_i=self.position_i
            self.fit_best_i=self.fit_i

    # update new particle velocity
    def update_velocity(self,pos_best_g):
        w=0.99     # constant inertia weight (how much to weigh the previous velocity)
        c1=1.99  # cognative constant
        c2=1.99    # social constant

        for i in range(0,num_dimensions):
            r1=random.random()
            r2=random.random()

            vel_cognitive=c1*r1*(self.pos_best_i[i]-self.position_i[i])
            vel_social=c2*r2*(pos_best_g[i]-self.position_i[i])
            self.velocity_i[i]=w*self.velocity_i[i]+vel_cognitive+vel_social
            
    

    # update the particle position based off new velocity updates
    def update_position(self,bounds):
        
        
        for i in range(0,num_dimensions):
            
            
            
                
           
            self.position_i[i]=self.position_i[i]+self.velocity_i[i]
            
            if self.position_i[i] > bounds[i][1]:      
                self.position_i[i] = bounds[i][1]
            elif self.position_i[i] < bounds[i][0]:    
                self.position_i[i] = bounds[i][0]
            else:
                self.position_i[i] = round(self.position_i[i])
            
            
            
            
class PSO:
    def __init__(self,initial,bounds,num_objects,particles,max_iter):
        global num_dimensions

        num_dimensions=num_objects
        fit_best_g=-1                   # best error for group
        pos_best_g=[]                   # best position for group

        # establish the swarm
        swarm=[]
        for i in range(0,particles):
            swarm.append(Particle(initial))

        # begin optimization loop
        i=0
        while i < max_iter:
            #print i,err_best_g
            # cycle through particles in swarm and evaluate fitness
            for j in range(0,particles):
                swarm[j].evaluate(func1_ev)

                # determine if current particle is the best (globally)
                if swarm[j].fit_i > fit_best_g:
                    pos_best_g=list(swarm[j].position_i)
                    fit_best_g=float(swarm[j].fit_i)

            # cycle through swarm and update velocities and position
            for j in range(0,particles):
                swarm[j].update_velocity(pos_best_g)
                swarm[j].update_position(bounds)
            i+=1

        # print final results
        print ('FINAL:')
        print (pos_best_g)
        sum=0
        summ=0
        for i in range((num_objects)):
            sum+=pos_best_g[i]*val[i]
            summ+=pos_best_g[i]*kg[i]
        print("the profit = ",sum)
        print(summ)
            
        


#--- EXECUTE

initial=[] # initial starting location [x1,x2...]
for i in range(len(val)):
   initial.append(0)
print(initial)
bounds=[]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)..
for i in range(len(val)):
    bounds.append((initial[i],math.floor(maxKg/kg[i])))
print(bounds)
    

PSO(initial,bounds,num_objects=len(val),particles=len(val)*10,max_iter=60)