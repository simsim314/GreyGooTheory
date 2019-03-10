#include <vector> 
using namespace std; 
class SnakeAlgo
{
public: 
	static vector<vector<int> > arr; 
	static const int w = 101; 
	static const int h = 101; 
	static const int centerx = 50; 
	static const int centery = 50; 
		
	static void init()
	{

		arr = vector<vector<int> > (h, vector<int>(w, 0));

		int x, y, dx, dy;
		for(int i = 0; i < 10000; i++)
		{
			index_to_xy(i, x, y, dx, dy);
			int x, y, dx, dy;
			x += centerx;
			y += centery;
			
			arr[x][y] = i;
		}
	}

	static int xy_to_index(int dx, int dy)
	{
		return arr[centerx + dx][centery + dy];
	}


	static void index_to_xy(int idx, int &x, int &y, int &dx, int &dy)
	{
		if(idx == 0)
		{
			x = 0;
			y = 0; 
			dx = 0;
			dy = 1;
			return;
		}
		
		if(idx == 1)
		{
			x = 0;
			y = 1; 
			dx = 1;
			dy = 0;
			return; 
		}
		
		int sq_size = (int)(sqrt(idx));
		int sq_idx = sq_size * sq_size;
		idx -= sq_idx; 
		
		if(sq_size % 2 == 0)
		{
			x = sq_size / 2;
			y = -sq_size / 2;
			dx = -1;
			dy = 0; 
			
			if(0 == idx)
				return; 
			
			if(idx <= sq_size)
			{
				x += idx * dx; 
				
				if(idx == sq_size)
				{
					dx = 0;
					dy = 1; 
				}
				return; 
			}
			
			x += sq_size * dx;
			idx -= sq_size;
			
			dx = 0;
			dy = 1; 
			
			y += dy * idx; 
			return;
		}
		else 
		{
			x = -((sq_size - 1) / 2);
			y = ((sq_size - 1) / 2) + 1;
			dx = 1;
			dy = 0; 
			
			if(0 == idx)
				return; 

			if(idx <= sq_size)
			{
				x += idx * dx; 
				
				if(idx == sq_size)
				{
					dx = 0;
					dy = -1; 
				}
				
				return; 
			}
			
			x += sq_size * dx;
			idx -= sq_size;
			
			dx = 0;
			dy = -1; 
			
			y += dy * idx; 
			return;

		}
	}
};

