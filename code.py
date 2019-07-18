import pysweetcat as sc
import numpy as np
import pyexoplaneteu as exo

stars=sc.get_data()
exoplanets=exo.get_data()

for i in range(stars.size):
	

	
	planets=np.array([])
	for j in range(exoplanets.size):
		if exoplanets['star_name'][j] == stars['name'][i]:
			planets=np.append(planets,j)
			



	if len(planets) > 0:

		dict =	{
			"Star-name": stars['name'][i],
  			"teff": stars['teff'][i],
  			"feh": stars['feh'][i],
  			"mass": stars['mass'][i],
  			"Exoplanets": [],
  			"Exoplanets-Mass":[],
  			"Exoplanets-Period": []
		}



		
		date=[stars['last_update'][i]]

		for planet in planets:
			dict['Exoplanets'] += [exoplanets['name'][int(planet)]]
			dict['Exoplanets-Mass'] += [exoplanets['mass_sini'][int(planet)]]
			dict['Exoplanets-Period'] += [exoplanets['orbital_period'][int(planet)]]
			date+= [exoplanets['updated'][int(planet)]]

		date=max(date)

		f=open(date+stars['name'][i]+".md","w")

		f.write('---\r\nlayout: entry\r\n')
		for k , v in dict.items():
			f.write(str(k)+': '+str(v)+'\r\n')

		f.write('---')
		f.close()
	

	

		
		
		
	
