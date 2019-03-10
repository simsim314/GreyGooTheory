#include <iostream>
#include <math.h>
// Kernel function to add the elements of two arrays
__global__
void add(int n, float *x, float *y)
{
  int index = blockIdx.x * blockDim.x + threadIdx.x;
   for(long j = 0; j < 20; j++)
	{
		int i = index; 
		x[i] = y[i] + 2;
		y[i] = x[i] * 7;				
	}	
}

int main(void)
{
  int N = 1<<20;
  float *x, *y;

  // Allocate Unified Memory – accessible from CPU or GPU
  cudaMallocManaged(&x, N*sizeof(float));
  cudaMallocManaged(&y, N*sizeof(float));

  // initialize x and y arrays on the host
  for (int i = 0; i < N; i++) {
    x[i] = 1.0f;
    y[i] = 2.0f;
  }

  // Run kernel on 1M elements on the GPU
	int blockSize = 256;
	int numBlocks = 100;
	add<<<numBlocks, blockSize>>>(N, x, y);
	
  // Wait for GPU to finish before accessing on host
  cudaDeviceSynchronize();

  // Check for errors (all values should be 3.0f)
	for(int i = 0; i < 10; i++)
		std::cout << x[i];
	
	std::cout << "Hello!";

  // Free memory
  cudaFree(x);
  cudaFree(y);
  
  return 0;
}