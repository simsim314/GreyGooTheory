#include <vector> 
#include <stdio.h>
#include <math.h> 
#include <iostream> 
#include <vector>
#include "SnakyUtils.h"
#define SRC 2  //Source of the change 
#define FLP 1  //Flip count. 0 first flip 1 second flip 
#define VAL 0  //Value of the cell. 0, 1, 2 - 2 for unknown. 

using namespace std; 

class SnakyLifeState
{
public: 
	int W; 
	int H; 
	vector<int> data; 
	//One bit is this is first or second attempt. First attempt scored higher as it's more stable as snake and more stable as CGOL state. 
	//first 2 bits for the state
	//12 bits to refer to the index of snake opened me. 
	
	SnakyLifeState(int w, int h)
	{
		data = vector<int>(W * H, -1);
		W = w; 
		H = h; 
	}
	
	int get_xy(int x, int y)
	{
		int i = y * W + x; 
		return data[i];
	}
	
	int set_xy(int x, int y, int val)
	{
		int i = y * W + x; 
		data[i] = val;
	}
	
	int get_state(int val)
	{
		if(val == -1)
			return 2; 
		
		return val % 4; 
	}
	
	void set_state(int state, int& val)
	{
		if(state == -1)
		{	
			val = -1;
			return; 
		}
		
		int v = state;
		val |= v;
	}
	
	bool is_first(int val)
	{
		if(val == -1)
			return true; 
		
		return (val >> 2) % 2 == 0; 
	}	

	int get_setter(int val)
	{
		if(val == -1)
			return -1; 
		
		return val >> 3; 
	}
		
	void setxy(int op, int x, int y, int val = 0)
	{
		int v = get_xy(x, y);

		if(op == 0)
			set_state(val, v);
		else if(op == 1)
			set_flip_flag(val, v);
		else 
			set_setter(val, v);
		
		set_xy(x, y, v);
	}

	void set_flip_flag(int flag, int& val)
	{
		if(flag == -1)
		{	
			val = flag; 
			return; 
		}
		
		if(flag == 1)
		{
			int v = 1 << 2;
			val |= v;
			return; 
		}
		
		int val_flag = (val >> 2) % 2; 

		if(val_flag == flag)
		{	
			return; 
		}
		else 
		{
			int v = 1 << 2;
			val ^= v;
		}
		
	}
	
	void set_setter(int setter, int& val)
	{
		if(setter == -1)
		{
			val = -1; 
			return; 
		}
		
		setter = setter << 3;
		val |= setter;
	}
	
	int getxy(int op, int x, int y)
	{
		int v = get_xy(x, y);
		
		if(op == 0)
			return get_state(v);
		else if(op == 1)
			return is_first(v);
		else 
			return get_setter(v);
	}

};

class SingleSnake
{
	SnakyLifeState child; //should all be known
	SnakyLifeState snake; //unknowns
	int xcenter, ycenter, length; 
	static const int R2 = 25; 
	
	int life_rule(int cnt_1, int ini)
	{
		if(cnt_1 == 3 || (ini == 1 && cnt_1 == 2))
			return 1;
		
		return 0; 
	}
	
	int life_rule(const vector<int>& total_vals, int ini)
	{
		int cnt_1 = total_vals[1];
		int cnt_unk = total_vals[2];
		
		int val = life_rule(cnt_1, ini);
		
		for(int i = 1; i < cnt_unk; i++)
		{	
			if(life_rule(cnt_1 + i, ini) != val)
			{
				val = 2; 
				break; 
			}
		}
		
		return val; 
	}
	
	int contradiction(int x, int y)
	{
		vector<int> total_vals(3, 0);
		
		for(int i = 0; i < 9; i++)
		{
			int x, y, dx, dy; 
			SnakeAlgo::index_to_xy(i, x, y, dx, dy);
			total_vals[snake.getxy(VAL, x + xcenter, y + ycenter)]++;
		}
		
		int val = snake.getxy(VAL, x + xcenter, y + ycenter);
		int new_val = life_rule(total_vals, val);
		
		if(new_val != 2)
		{
			if(child.getxy(VAL, x + xcenter, y + ycenter) != new_val)
				return -1; 
		}
		
		return new_val; 
	}
	
	void try_set_unroll(int centerx, int centery, int prev_val)
	{
		snake.set_xy(centerx, centery, prev_val);
		
		for(int i = 1; i < R2; i++)
		{
			int x, y, dx, dy; 
			SnakeAlgo::index_to_xy(i, x, y, dx, dy);
			
			if(snake.getxy(SRC, centerx + x, centery + y) == length)
				snake.setxy(SRC, centerx + x, centery + y, -1);
		}
	}

	bool try_set(int in_x, int in_y, int in_val)
	{
		int centerx = xcenter + in_x;
		int centery = ycenter + in_y;
		
		int prev_val = snake.get_xy(centerx, centery);
		
		snake.setxy(VAL, centerx, centery, in_val);
		snake.setxy(SRC, centerx, centery, length);
		
		bool news = false; 
		
		do
		{
			for(int i = 1; i < R2; i++)
			{
				int x, y, dx, dy; 
				SnakeAlgo::index_to_xy(i, x, y, dx, dy);
				int val = contradiction(centerx + x, centery + y);
				
				if(val == -1)
				{
					try_set_unroll(centerx, centery, prev_val);
					return false; 
				}
				
				if(val != 2)
				{
					if(snake.getxy(VAL,centerx + x,centery + y) == 2)
					{
						snake.setxy(VAL,centerx + x, centery + y, in_val);
						snake.setxy(SRC,centerx + x, centery + y, length);
						news = true; 
					}
				}
			}
		}
		while(news);
		
		length++; 
	}

	void next()
	{
		int x, y, dx, dy; 
		SnakeAlgo::index_to_xy(length, x, y, dx, dy);
		
		int val = snake.getxy(VAL, xcenter + x, ycenter + y); 
		
		if(val == 2)
			val = 0;
		else
		{
			if(val == 0)
				val = 1;
			
			if(val == 1)
			{
				try_set_unroll(xcenter + x, ycenter + y, -1);
				length--; 
				return;
			}
		}
		
		
		try_set(x, y, val);
		//Here we shuold state 1, 0 if -1 and flip if 0 or 1. 
		//And estimate the best path. 
	}
};

class MultiSnake
{
public: 
	MultiSnake* top; 
	
	int index; 
	SnakyLifeState* state; 
	MultiSnake* parent_snake; 
	MultiSnake* child_snake; 
	
};




//Even: 1->4, 2->16, 3->36
//		1->2  2->4  3->6 
//i -> (2i)^2 -> 4ii

//Odd: 1->9 2->25 3 -> 49
//     1->3 2->5  3-> 7
//i -> (2i + 1)^2 = 4ii + 4i + 1

/*
int xy_to_index(int x, int y)
{
	int a = max(abs(x), abs(y)) + 1;
	
	int idx_even = 4 * a * a; 
	int idx_odd  = 4 * a * a + 4 * a + 1; 
	
	int x, y, dx, dy; 
	index_to_xy(idx_even, x, y, dx, dy);
	dx += 1; 
	
}
*/

int main()
{
	getchar();
}