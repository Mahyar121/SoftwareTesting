#include <iostream>
#include <string>
using namespace std;


int main()
{
	int a[15] = { 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 1, 2, 100, 199, 200 };
	int b[15] = { 100, 100, 100, 100, 100, 1, 2, 100, 199, 200, 100, 100, 100, 100, 100 };
	int c[15] = { 1, 2, 100, 199, 200, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100 };
	bool isTriangle = false;
	
	cout << "| Case | a     | b     | c      | Expected Output |" << endl;
	for (int i = 0; i < 15; i++)
	{
		if ((a[i] + b[i] > c[i]) && (b[i] + c[i] > a[i]) && (a[i] + c[i] > b[i]))
		{
			isTriangle = true;
		}
		else
		{
			isTriangle = false;
		}

		if (isTriangle)
		{
			if ((a[i] == b[i]) && (b[i] == c[i]))
			{
				cout << "| " << i + 1 << "   | " << a[i] << "   | " << b[i] << "   |  " << c[i] << "     | " << "Equilateral |" << endl;
			}
			else if (((a[i] == b[i]) && (a[i] != c[i]) && (b[i] != c[i])) || ((a[i] == c[i]) && (a[i] != b[i]) && (c[i] != b[i])) || ((b[i] == c[i]) && (b[i] != a[i]) && (c[i] != a[i])))
			{
				cout << "| " << i + 1 << "   | " << a[i] << "   | " << b[i] << "   |  " << c[i] << "       | " << "Isosceles |" << endl;
			}
			else if ((a[i] != b[i]) && (a[i] != c[i]) && (b[i] != c[i]))
			{
				cout << "| " << i + 1 << "   | " << a[i] << "   | " << b[i] << "   |  " << c[i] << "     | " << "Scalene |" << endl;
			}
		}
		else
		{
			cout << "| " << i+1 << "   | " << a[i] << "   | " << b[i] << "   |  " << c[i] << "     | " << "Not a Triangle |" << endl;
		}
	}
	system("Pause");
	return 0;
}