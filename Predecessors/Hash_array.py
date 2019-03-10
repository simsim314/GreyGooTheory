import math
import matplotlib.pyplot as plt


def estimate(n, N1):
	M = 8 * 10**9
	K1 = M / n

	return n * (math.log(K1 - N1) - math.log(N1))

N = 5 * 10**7
max = 0
maxi = 0

nums = []
xs = []

for i in range(1, 300):
	val = estimate(i, N) / math.log(10)
	nums.append(val)
	xs.append(i)
	
	if val < 0 or val > 20:
		break 
	
plt.plot(xs, nums)
plt.ylabel('some numbers')
plt.show()
