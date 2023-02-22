#include <iostream>

//multiplies 3x3 transistion matrix with distribution
float** multiplyMatrix3x3(float A[3][3] , float** x) {
	 float** Ax = 0;
	 Ax = new float* [3];
	 for (int i = 0; i < 3; i++) {
		 Ax[i] = new float[4];
		 for (int j = 0; j < 4; j++) {
			 Ax[i][j] = A[i][0] * x[0][j] + A[i][1] * x[1][j] + A[i][2] * x[2][j];
		 }
	}
	 return Ax;
}

//multiplies 4x4 transistion matrix with distribution
float** multiplyMatrix4x4(float A[4][4], float** x) {
	float** Ax = 0;
	Ax = new float* [4];
	for (int i = 0; i < 3; i++) {
		Ax[i] = new float[4];
		for (int j = 0; j < 4; j++) {
			Ax[i][j] = x[i][0] * A[0][j] + x[i][1] * A[1][j] + x[i][2] * A[2][j] + x[i][3] * A[3][j];
		}
	}
	return Ax;
}

//prints matrix
void printMatrix(int row, int col, float** matrix) {
	 for (int i = 0; i < row; i++) {
		 for (int j = 0; j < col; j++) {
			 std::cout << matrix[i][j] << " ";
		 }
		 std::cout << "\n";
	 }
	 std::cout << "\n";
 }

void distributionCalc(int years) {
	/* initial transistion matrix.
		60%		10%		5%
		25%		50%		15%
		15%		40%		80%
	*/
	float A1[3][3] = { {0.6, 0.1, 0.05}, {0.25,0.5, 0.15},{0.15, 0.40, 0.8}};

	/* transistion matrix after 3 years.
		60%		9.5%	5%		0.5%
		24.5%	50%		14%		0.5%
		14.5%	39.5%	80%		2%
		1%		1%		1%		97%
	*/
	float A2[4][4] = { {0.6, 0.095, 0.05, 0.005}, {0.245, 0.5, 0.14, 0.005},{0.145, 0.395, 0.8, 0.02},{0.01, 0.01, 0.01, 0.97}};

	/* initial distribution of buyers.
		1	0	0	0
		1	0	0	0
		1	0	0	0
	*/

	//creates empty 3x4 array
	float** x0 = 0;
	x0 = new float* [3];
	for (int i = 0; i < 3; i++) {
		x0[i] = new float[4];
	}

	//adds value for initial distribution
	for (int i = 0; i < 3; i++) {
		x0[i][0] = 1;
		for (int j = 1; j < 4; j++) {
			x0[i][j] = 0;
		}
	}
	
	//x1 = Ax0
	float** finalDistribution = multiplyMatrix3x3(A1,x0);
	std::cout << "Initial Distribution:" << "\n";
	printMatrix(3, 4, finalDistribution);

	for (int i = 1; i < years; i++) {
		if (i > 2) {
			finalDistribution = multiplyMatrix4x4(A2, finalDistribution);
			std::cout << "Distribution after " << i << " years:" << "\n";
			printMatrix(3, 4, finalDistribution);
		}
		else {
			finalDistribution = multiplyMatrix3x3(A1, finalDistribution);
			std::cout << "Distribution after " << i << " years:" << "\n";
			printMatrix(3, 4, finalDistribution);
		}
	}

}

int main(){
	int years;
	std::cout << "Enter number of years: ";
	std::cin >> years;

	distributionCalc(years);

	return 0;
}