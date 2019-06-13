import pysweetcat as sc
import numpy as np
import pyexoplaneteu as exo

stars=sc.get_data()
exoplanets=exo.get_data()

for i in range(stars.size):
	
		
	planets=0
	index=np.array([])
	for j in range(exoplanets.size):
		if exoplanets['star_name'][j] == stars['name'][i]:
			planets+=1
			index=np.append(index,j)



	if len(index) > 0:

		f=open(stars['name'][i]+".txt","w")
		f.write('---\r\nlayout:entry\r\nStar-name:'+stars['name'][i]+'\r\n')
		f.close()

		f2=open(stars['name'][i]+".txt","a")

		for k in ['teff','feh','mass']:
			f2.write(k+':'+str(stars[k][i])+'\r\n')


		f2.write('Exoplanets: [')
		for planet in index:
			f2.write(str(exoplanets['name'][int(planet)]))
			if planet != index[-1]:
				f2.write(',')
			else: 
				f2.write(']\r\n')

		f2.write('Exoplanets-Mass: [')
		for planet in index:
			f2.write(str(exoplanets['mass'][int(planet)]))
			if planet != index[-1]:
				f2.write(',')
			else: 
				f2.write(']\r\n')
		f2.write('Exoplanets-Period: [')
		for planet in index:
			f2.write(str(exoplanets['orbital_period'][int(planet)]))
			if planet != index[-1]:
				f2.write(',')
			else: 
				f2.write(']\r\n')	
		
		f2.write('Number-Exoplanets:'+str(planets)+'\r\n---')
		f2.close()
	

	

		
		
		
	

#for key in stars:
	#print(key,stars[key][1])

#print(exoplanets['name'][0],stars['name'][0])
#if exoplanets['name'][0] == stars['name'][0]+' b':
	#print('True')