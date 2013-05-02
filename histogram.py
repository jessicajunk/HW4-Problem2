#HW 4 Problem 2
#Plots a histogram showing the distribution of prime numbers up to 10^7 modulo n
n = 15
p = prime_range(2, 10^7)
count = 0
for i in p:
    p[count] = i % n
    count += 1
stats.TimeSeries(p).plot_histogram()
