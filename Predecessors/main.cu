#include <iostream>
#include <math.h>
#include "utils.cuh"
#include "snake.cuh"

kernel
void add(int n, LifeState *states)
{
	int idx = blockIdx.x * blockDim.x + threadIdx.x;
	states[idx].data[0] = states[idx].W + states[idx].H; 
}

int main(void)
{
	int blockSize = 32;
	int numBlocks = 18;
	
	int N = blockSize * numBlocks;
	LifeState* states;
	states = cu_new_arr<LifeState>(N);
	
	for(int i = 0; i < N; i++)
		states[i].Init(10,10);
	
	add<<<numBlocks, blockSize>>>(N, states);

	cudaDeviceSynchronize();
	
	std::cout << states[0].data[0];
	
	for(int i = 0; i < N; i++)
	{	
		std::cout << states[i].data[0];
		states[i].~LifeState();
	}
	cudaFree(states);
	
	return 0;
}