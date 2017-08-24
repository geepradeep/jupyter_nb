import re, numpy

def parse_atoms():
	inputFile=open('files/benzene.xyz','r')
	a = inputFile.read()
	a = a.split('\n')
	atoms = ['atomname']*12
	coordinates = [[0.0 for x in range(3)] for y in range(12)]
	for i in range(len(a)):
		a[i] = re.sub(' +',' ',a[i])
		a[i] = a[i].rstrip()
		a[i] = a[i].split(' ')
	for i in range(2,14):
		atoms[i-2] = a[i][0]
	return atoms

def parse_coordinates():
	inputFile=open('files/benzene.xyz','r')
	a = inputFile.read()
	a = a.split('\n')
	atoms = ['atomname']*12
	coordinates = [[0.0 for x in range(3)] for y in range(12)]
	for i in range(len(a)):
		a[i] = re.sub(' +',' ',a[i])
		a[i] = a[i].rstrip()
		a[i] = a[i].split(' ')
	for i in range(2,14):
		coordinates[i-2] = numpy.array((float(a[i][1]),float(a[i][2]),float(a[i][3])))
	return coordinates
