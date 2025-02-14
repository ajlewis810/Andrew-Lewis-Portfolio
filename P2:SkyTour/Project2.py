##Homework 6 problem 2 
# How can we go about doing this lets see we are asked to consider a Messier Tour of all the Messier objects, there are 110. 
#Lets write the code for these objects observing on Nov 12, 2023 from the Keck Observatory in Hawaii. 
#The main goal is to plt target elevatin as a function of time in LST and UT

#In the plot the elevation should be expressed in degrees and the time axes should be in decimal 


#import the necessary packages 

import numpy as np 
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style, quantity_support
import astropy.units as u 
from astropy.coordinates import AltAz, EarthLocation, SkyCoord
from astropy.time import Time 


#We are going to need a for loop to go through all the Messier objects, but lets start with one for right now. 

target_list = ['jupiter', 'venus', 'mars']

m33 = SkyCoord.from_name('M42')


#Need to set our observation point which we will take our observations which is at the Keck Observatory in Hawaii 

#Data on Keck: 19.8260 N, 155.4747 W, Height: 4,145 meters 

#keck_obs = EarthLocation( lat = 19.8260 *u.deg, lon = 155.4747*u.deg, height = 4145*u.m)
#utcoffset = -10*u.hour  # Hawaii Time 


#Data on Orange County: 33.7175 N, 117.8311 W, height : 190 m 

keck_obs = EarthLocation(lat = 33.7175 *u.deg, lon = 117.8311, height = 190 * u.m)
utcoffset = -8 *u.hour #Pacific Standar Time 
time = Time('2025-2-13 00:00:00') - utcoffset




m33altaz = m33.transform_to(AltAz(obstime = time, location = keck_obs))

print(f"M33's Azimuthal Angle  = {m33altaz.az:.2f}")
print(f"M33's Altitude = {m33altaz.alt:.2f}")
  
#OK so we can find the alt and az at a specific time, now lets see if we can find it for a range of times

midnight = time
 
#In Hawaii on November 12, Sunsets at 5:50 pm and Rises at 6:40 Pm so lets observe from 6pm to 7AM 
observing_time = np.linspace(-6, 7, 100) * u.hour

Night_Nov12_23 = AltAz(obstime = midnight+observing_time, location = keck_obs)

M33N1223altaz = m33.transform_to(Night_Nov12_23)

M33N_12_23_alt = M33N1223altaz.alt
M33N_12_23_az = M33N1223altaz.az

plt.plot(observing_time, M33N_12_23_alt)
plt.xlim(-6, 7)
plt.xlabel("6PM Sunset to 7AM Sunrise")
plt.ylabel("Altitude in Degrees")
plt.title("M33 Altitude 11/12/23 from Keck Observatory") 
plt.show()

plt.plot(observing_time, M33N_12_23_az)
plt.xlim(-6, 7)
plt.xlabel("6PM Sunset to 7AM Sunrise")
plt.ylabel("Azimuthal Angle in Degrees")
plt.title("M33 Altitude 11/12/23 from Keck Observatory")

plt.show()


for target in target_list: 
	body = SkyCoord.from_name(target)
	bodyaltaz = body.transform_to(AltAz(obstime = midnight+observing_time, location = keck_obs))
	plt.plot(observing_time, bodyaltaz.alt, label = target)
	plt.xlim(-6, 7)
	plt.xlabel("6PM Sunset to 7AM Sunrise")
	plt.ylabel("Altitude in Degrees")
	plt.ylim(0, 90)
	plt.title("Altitude of Various Messier Objects at Midnight on 11/12/23 from Keck Observatory (LST)")
	plt.legend(loc = "upper right", fontsize = "small") 


plt.show()

#Cool, can do the same thig for azimuthal angle, just replace the above with .az and you caan find any object on the sky anywhere 
#in the world at any time as long as you change the location and time. 



#Save as pdf here and add this to the submission
plt.savefig('Altitude_Keck_Observatory_11_12_23.pdf', format='pdf', bbox_inches='tight')








