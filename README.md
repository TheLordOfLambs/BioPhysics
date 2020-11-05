# BioPhysics

## Data
The goal of the project is to model physics of [this experiment](http://lptms.u-psud.fr/membres/mlenz/teaching/modeling-DNAPackaging.pdf)
Datas can be found [here](http://lptms.u-psud.fr/membres/mlenz/teaching/modeling-DNAPackaging-data.txt)

## How to use Github

### Instalation

first you need to install git

on linux simply use the command 
```console
apt-get install git-all
```
for mac or windows you can ether use a [desktop version](https://desktop.github.com/) (wich I never tried) or a [bash version](https://git-scm.com/downloads) (less user friendly but more control)
for the bash version on mac you can check if it is allready installed by using : 
```console
git --version
```
### Using git (Bash)

the first thing you will do is clone the repository. To do so simply type  : 
```console
git clone https://github.com/TheLordOfLambs/BioPhysics.git
```
Then it will create a BioPhysics file. You can now go inside with : 
```console
cd BioPhysics
```
After doing your work eather modifying, creating files use the command :
```console
git add .
git commit -m "right what you've done"
```
then to publish it on github use the command : 
```console
git push origin
```
** /!\ ** Before starting working allways use the command: 
```console
git pull 
```
it will keep your folder up to date in case someone have modified some files
