#this code is to calculate the reference signal strength(rss) and signal attenuation factor(n)

#importing libraries
import time
import subprocess
import numpy
import math

#declaring an empty list to store average signal strength value at 10 different locations
Y = []

#function to calculate average value of signal strength at a particular location by taking 20 readings of signal strength at that location
def average_rssi():
    avg = 0
    for i in range(20):
        #getting the result of command line command and storing it in a variable
        result = subprocess.check_output(["netsh", "wlan", "show", "network", "mode=Bssid"])
        #converting the result(datatype-bytes) first into string and then storing substrings in list y
        y = list((result.decode('ASCII')).split())

        for i in range(len(y)):
            if y[i] == 'Signal':
                a = y[(i + 2)]
                signal = a[0:len(a) - 1]

        dbm = ((int(signal)) / 2) - 100
        print(dbm)
        avg += dbm
        time.sleep(20)

    avg /= 20
    return avg

#getting the average value of signal strength at 10 different locations and storing it in the list Y
for i in range(10):
    rssi = average_rssi()
    Y.append(rssi)
    print(Y)
    time.sleep(5)

print(Y)
#converting list Y into a numpy array
Y = numpy.array(Y)
#reshaping Y from dimension (1,10) into (10,1)
Y.reshape((10,1))

#declaring a numpy array according to distance calculating formula PL(d) = PL(d0) - 10*n*log(d/d0) where PL(d) is the signal strength at distance d and d0=1m is the reference distance
Z = numpy.array([[1, -10 * math.log(1.5, 10)],
                 [1, -10 * math.log(2, 10)],
                 [1, -10 * math.log(3, 10)],
                 [1, -10 * math.log(3.5, 10)],
                 [1, -10 * math.log(4, 10)],
                 [1, -10 * math.log(4.5, 10)],
                 [1, -10 * math.log(5, 10)],
                 [1, -10 * math.log(5.5, 10)],
                 [1, -10 * math.log(6, 10)],
                 [1, -10 * math.log(6.5, 10)]])

#X=[[rss], [n]] therefore Y=Z*X and by method of least square algorithm to minimize error we get X=(Z_transpose.Z)^(-1).(Z_transpose.Y)
Z_trans = Z.transpose()
A = numpy.linalg.inv(Z_trans.dot(Z))
B = Z_trans.dot(Y)
X = A.dot(B)
rss = X[0][0]
n = X[1][0]
print(rss)
print(n)
