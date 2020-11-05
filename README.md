# BioPhysics

## The Project
The goal of the project is to model physics of DNA packaging inside a viral capsid. To do so a molecular motor, known as the *portal motor*, push the double-stranded DNA inside the capsid. [This experiment](http://lptms.u-psud.fr/membres/mlenz/teaching/modeling-DNAPackaging.pdf) measure the force exerced by the motor to fill the capsid. Datas can be found [here](http://lptms.u-psud.fr/membres/mlenz/teaching/modeling-DNAPackaging-data.txt).

## The files
Please use this section to explain what is in each files. It will make collaboration easier.

* **Entropy.ipynb** First draft of an Entropy-based model
* **First model-Félix.ipynb** 
* **Model-Angelo.ipynb** First attempt to establish a free energy with both configuration entropy and energy due to bending (Wrong calculation should be discarded)
* **Some reflexion Félix (correction).ipynb** *Differences with Some reflexion.ipynb ???*
* **Some reflexion.ipynb** First draft of the *spiral* model
* **basicfit.ipynb** First test of fiting with the model proposed by Nemo (Comparing volume spanned by DNA with volume of the capsid)









## The team

* **Angelo Charry**
* **Némo Malhomme**
* **Carlo Paris**
* **Francesco Saverio Pezzicoli**
* **Félix Vannier**


## How to use Github

### Instalation

first you need to install git

on linux simply use
```console
apt-get install git-all
```
for mac or windows you can ether use a [desktop version](https://desktop.github.com/) (wich I never tried) or a [bash version](https://git-scm.com/downloads) (less user friendly but more control)
for the bash version on mac you can check if it is allready installed by using 
```console
git --version
```
### Using git (Bash)

The first thing you will do is clone the repository. To do so simply type 
```console
git clone https://github.com/TheLordOfLambs/BioPhysics.git
```
Then it will create a *BioPhysics* folder. You can then go inside with  
```console
cd BioPhysics
```
After doing your work eather modifying, creating files, you can add your modification like so
```console
git add .
git commit -m "write what you've done"
```
Finally to publish it on github use the command  
```console
git push origin
```
**/!\ Before starting working allways use the command **
```console
git pull 
```
it will keep your folder up to date in case someone have modified somes files
