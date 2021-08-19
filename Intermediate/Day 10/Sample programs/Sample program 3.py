>>> import cmath
>>> z=complex(-2,1)
#make a complex number.
>>> cmath.exp(z)
# Raise z to a complex power.
(0.07312196559805963+0.1138807140643681j)
>>> cmath.exp(z.real)
# the cmath module takes in real as well as complex parameters.
(0.1353352832366127+0j)
>>> cmath.log(z,10)
#logarithm of z to the base 10
(0.3494850021680094+1.1630167557051545j)
>>> cmath.log(10,z)
# logarithm of 10 to  the base z
(0.2369795135136017-0.7886208085195003j)
>>> cmath.log(z,z)
#alogarithm of z to the base z
(1+0j)
>>> cmath.sqrt(z)
# square root of z
(0.34356074972251244+1.455346690225355j)
>>> cmath.acos(z)
# arccos of z
(2.6342363503726487-1.4693517443681852j)
>>> cmath.atan(z)
# arctan of z
(-1.1780972450961724+0.17328679513998632j)
>>> cmath.sin(z)
# arc sine of z
(-1.4031192506220405-0.4890562590412937j)
>>> cmath.acosh(z)
# hyperbolic inverse cosine
(1.4693517443681852+2.6342363503726487j)
>>> cmath.tanh(z)
# hyperbolic tangent
(-1.0147936161466335+0.0338128260798967j)
>>> cmath.pi
# The usual pi constant
3.141592653589793
>>> pow(z,z)
# z raised to the power z.(note that this is not from the cmath module.
(-0.00220568464655929+0.013562654681556313j)
