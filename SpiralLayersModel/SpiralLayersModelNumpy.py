import numpy as np
import math
import matplotlib.pyplot as plt

#This program computes numerically the total energy cost of putting DNA in a capsid,
#as a function of the inserted lenght, according to the "Spiral Layers model"
#(according to which the capsid contains many circles slots arranged in layers,
#and we fill the lowest energy energy (aka biggest) ones first)

#When i'll have the time, i'll fit
#the d parameter (distance between two neigbour DNA strands)

#This model only considers bending energy. Entropy is completely neglected,
#and steric interactions are simply treated as an impassable wall of minimal distance.


def energy(r, factor=1): #Energies of circles of radiuses r (r is an array)
    
    return np.where(r==0., math.inf, factor*math.pi/r)

def perimeter(r): #Perimeter of a circle of radius r (r can be an array)
    p=2*r*math.pi
    return p

#Array of radiuses of the first free circe (j+1th) of each layer
def r(j, R, d):
    i = np.arange(len(j))
    return np.where( (R-i*d)**2 > ((j+1)*d)**2, np.sqrt( (R-i*d)**2 - ((j+1)*d)**2 ), 0 )

#This function does one iteration of finding the layer with the lowest energy available circle
#And then filling it
def iter_fill(R, d, occupations, L, E, factor=1):
    
    
    radius = r(occupations, R, d)
    energies = energy(radius, factor)
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
def packing_energy(R, d, Ltot, factor=1):
    listL=[0]
    listE=[0]
    
    occupations, L, E = init_fill(R,d)
    
    while L<Ltot and E<math.inf:
        occupations,L,E = iter_fill(R, d, occupations, L, E, factor)
        listL.append(L), listE.append(E)
        
    return listL, listE

def energy_to_force(listL, listE):
    return np.gradient(listE, listL)
    

def plot_graphs(R,d,L):
    lengths,energies=packing_energy(R, d, L)
    forces = energy_to_force(lengths, energies)
    
    plt.plot(lengths,forces, '.', color='r')
    plt.show()
    plt.plot(lengths,energies, '.')
    plt.show()
    
#Constants; R,l,b are in nm
R = 20
L = 19000*.33
kb = 1.38e-23
T = 300
b = 50 #correlation lenght of DNA, 50 nm


#d = 0.02*1e-9
#plot_graphs(R, d, L)


#Now, let's get to the fitting !
from scipy.optimize import curve_fit

#I haven't put any security in case the data has values of L inserted too big for the model, because in practive we're very far from there.
def model(x, d, kbTbpi):
    lengths,energies=packing_energy(R, d, math.inf, factor = kbTbpi)
    forces = energy_to_force(lengths, energies)
    
    #print("PHASE 1")
    #print(lengths)
    #print(x)
    
    #As our model gives data at fixed values and not continuously, we need to map the entry data to values of x we have a y for.
    data_x_indexes = np.searchsorted(lengths, L*x/100, 'right')-1
    #We now have the indexes of the elements of the "lengths" array to which most closely correspond.
    #print(data_x_indexes)
    return forces[data_x_indexes]

def draw_me_a_fit(datax, datay, model):
    popt, pcov = curve_fit(model, datax, datay)
    x = L*datax/100
    y = model(datax, popt[0], popt[1])
    
    
    plt.plot(x, datay, 'b+', label='data')
    plt.plot(x, y, 'r--', label='fit: d=%5.3f, factor=%5.3f' % tuple(popt))

    plt.xlabel('Length inserted in the capsid (nm)')
    plt.ylabel('Force (idk)') 
    plt.title('Fit of the Spiral-Layers model')
    plt.legend()
    plt.show()
    
datax = np.array([30.37292789969,31.99187600139,33.6108241031,35.22977220481,36.84872030651,38.46766840822,40.65324834552,42.27219644723,43.89114454894,45.51009265064,47.12904075235,48.74798885406,50.36693695576,51.98588505747,53.60483315918,55.22378126088,56.84272936259,58.4616774643,60.080625566,61.69957366771,63.31852176942,64.93746987113,66.55641797283,68.17536607454,69.79431417625,71.41326227795,73.03221037966,74.65115848137,76.27010658307,77.88905468478,79.50800278649,81.12695088819,82.7458989899,84.36484709161,85.98379519331,87.60274329502,89.22169139673,90.84063949843,92.45958760014,94.07853570185,95.69748380355,97.31643190526,98.93538000697,100.5543281087,102.1732762104,103.7922243121])

datay = np.array([-0.5429885000496,-0.6086670962625,-0.1817562208784,0.01527956776048,0.01527956776048,-0.08323832655894,-0.08323832655894,0.1137974620799,0.4093511450382,1.033297809061,1.263172895806,1.460208684445,1.624405174978,1.952798156042,2.576744820065,3.200691484088,3.726120253792,4.842656389412,6.057710419352,7.502639536036,8.750532864082,9.867068999703,11.27915881828,13.15099881035,16.00801774561,18.17541142064,19.94873351839,21.49218052939,22.70723455933,24.11932437791,25.89264647566,28.15855804501,30.6543447011,33.47852433826,36.99232923565,39.84934817091,42.11525974026,43.92142113612,45.46486814712,46.81127936949,47.92781550511,48.88015515019,49.79965549717,50.52212005552,51.34310250818,51.9670491722])
    


draw_me_a_fit(datax[:40], datay[:40], model)