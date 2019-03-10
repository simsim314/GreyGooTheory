#include <iostream>
#include <math.h>
#include "utils.cuh"

class LifeState
{
public: 
	int W; 
	int H; 
	int* data; 
	
	common void Init(int w, int h)
	{
		data = cu_new_arr<int>(W * H);
		cu_init(&W);
		cu_init(&H);
		W = w; 
		H = h; 
	}
	
	common ~LifeState()
	{
		cudaFree(&H);
		cudaFree(&W);
		cudaFree(data);
	}
};

class SingleSnake
{
public: 
	LifeState* state; 
	SingleSnake* parent_snake; 
	SingleSnake* child_snake; 
	int xcenter, ycenter, length; 
	
};