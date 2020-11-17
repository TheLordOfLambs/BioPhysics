import numpy as np
import math
import matplotlib.pyplot as plt

#This program computes numerically the total energy cost of putting DNA in a capsid,
#as a function of the inserted lenght, according to the "Spiral Layers model"
#(according to which the capsid contains many circles slots arranged in layers,
#and we fill the lowest energy energy (aka biggest) ones first)

#When i'll have the time, i'll make the link from energy to force and then fit
#the d parameter (distance between two neigbour DNA strands)

#This model only considers bending energy. Entropy is completely neglected,
#and steric interactions are simply treated as an impassable wall of minimal distance.


def energy(r): #Energies of circles of radiuses r (r is an array)
    kb = 1.38e-23
    T = 300
    b = 50*1e-9 #correlation lenght of DNA, 50 nm
    return np.where(r==0, math.inf, 1/r) #1/r -> kb*t*pi*b/r

def perimeter(r): #Perimeter of a circle of radius r (r can be an array)
    p=2*r*math.pi
    return p

#Array of radiuses of the first free circe (j+1th) of each layer
def r(j, R, d):
    i = np.arange(len(j))
    return np.where( (R-i*d)**2 > ((j+1)*d)**2, np.sqrt( (R-i*d)**2 - ((j+1)*d)**2 ), 0 )

#This function does one iteration of finding the layer with the lowest energy available circle
#And then filling it
def iter_fill(R, d, occupations, L, E):
    
    
    radius = r(occupations, R, d)
    energies = energy(radius)
    minE = np.amin(energies)
    minEindex = np.argmin(energies)
    
    #Filling said circle
    L += perimeter(radius[minEindex])
    E += minE
    #Symetry: Pairs of symetrical circles are filled at the same time because they have the same energy.
    if occupations[minEindex]:
        L += perimeter(radius[minEindex])
        E += minE
    occupations[minEindex]+=1

    return occupations, L, E

def init_fill(R, d): #Creates an array of available layers and sets them all to completely empty.
    #Returns an array containing -1, which signify "completely empty" for each layer.
    return np.array([-1 for i in range(math.ceil(R/d))]), 0, 0

#Uses all precedently defined fonctions to actually compute E(L).
#The occupations variable is an array of integers
#Its values are Y coordinates of the highest energy filled circle
#(aka the number of filled circles -1, since we start with 0)
def packing_energy(R, d, Ltot):
    listL=[0]
    listE=[0]
    
    occupations, L, E = init_fill(R,d)
    
    while L<Ltot and E<math.inf:
        occupations,L,E = iter_fill(R, d, occupations, L, E)
        listL.append(L), listE.append(E)
        
    return listL, listE

def plot_energy_graph(R,d,L):
    L,E=packing_energy(R, d, L)
    
    plt.plot(L,E, '.')
    plt.show()
    
    
#First argument: R, capsid size
#second argument: d, DNA strands distance (to fit)
#Third parameter: maximum lenght. I've put infinity to get the full graph.
plot_energy_graph(50, 0.3, math.inf)

    
    
    
    
    
    
    
