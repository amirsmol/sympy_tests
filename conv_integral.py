from __future__ import division
from sympy import *
from sympy.plotting import plot
from sympy.plotting import plot_parametric

# sigma, Elect_Amp, K_e1, time,nu_frequency,,lambda_e1 = symbols('sigma, Elect_Amp, K_e1, time,nu_frequency,s_time,lambda_e1',positive=True)
sigma_t =symbols(" sigma_t ")
Elect_t =symbols(" Elect ")
time,s_time  =symbols(" time,s_time ",positive=True)


pi=3.14
nu_frequency=.1
# /(2*pi);
lambda_e1=1.0;


 # sigma = integrate(K_e1*exp(-lambda_e1*( time - s_time ))*Elect_Amp * sin(2*pi*nu_frequency) ,s_time)

# sigma = integrate(K_e1* exp(-lambda_e1*( s_time )) ,s_time)
# sigma = integrate( s_time  ,s_time)
# sigma = integrate( sin(2*pi*nu_frequency*s_time)  ,s_time)


# sigma= integrate(K_e1*exp(-lambda_e1*( time - s_time )) * Elect_Amp * sin(2*pi*nu_frequency*s_time), s_time)


Elect=sin(2*pi*nu_frequency*time)
Elect_dot=diff(Elect,time)

sigma= integrate(exp(-lambda_e1*( time - s_time ))* Elect_dot.subs(time,s_time), s_time)

# print sigma;
sigma_t=sigma.subs(s_time,time)-sigma.subs(s_time,0)


# sigma_t_plot=plot(sigma_t,(time,0,10))

hysteresis_plot= plot_parametric(Elect,sigma_t , (time,0,10/nu_frequency) )


# plot([cos, sin], [-4, 4])


print sigma_t


# print sigma


