#pragma once
#define cuda __device__  
#define kernel __global__  
#define common __host__  

template<class T>
common T* cu_new_arr(int size)
{
    T* result; 
	cudaMallocManaged((void**)&result, size * sizeof(T));
	cudaMemset(result, 0, size * sizeof(T));
	return result; 
}

template<class T>
common void cu_init(T* p)
{
	cudaMallocManaged((void**)&p, sizeof(T));
	cudaMemset(p, 0, sizeof(T));
}