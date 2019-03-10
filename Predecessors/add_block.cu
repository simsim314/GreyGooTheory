#include <iostream>
#include <math.h>

#define cuda __device__  
#define kernel __global__  
#define common __host__  

template<class T>
common T* cu_new_arr(int size)
{
    T* result; 
	cudaMallocManaged((void**)&result, size * sizeof(T));
	//cudaMemset(result, 0, size * sizeof(T));
	return result; 
}

kernel
void add(int n, int *x, int *y)
{
	int idx = blockIdx.x * blockDim.x + threadIdx.x;
	//int xi = x[i];
	//int yi = y[i];
	int i = idx; 
	
	for(long j = 0; j < 50000000; j++)
	{
		
		 i += 17;
		 
		 if(i > 1000000)
			 i /= 2; 
		 
		 //y[i] = x[i] + 17; 
	}	
	
	x[idx] = i;
	//y[i] = yi; 
}

int main(void)
{
	int N = 1<<20;
	int *x, *y;
	x = cu_new_arr<int>(N);
	y = cu_new_arr<int>(N);

	for (int i = 0; i < N; i++) {
		x[i] = 1;
		y[i] = 2;
	}

	int blockSize = 32;
	int numBlocks = 18;
	add<<<numBlocks, blockSize>>>(N, x, y);

	cudaDeviceSynchronize();
	std::cout << numBlocks << "," << blockSize <<"\n\n\n";

	cudaFree(x);
	cudaFree(y);

	return 0;
}

//50000 * 32 * 18 rea/write + calculate = 1 sec. 
//10 operations. 
//