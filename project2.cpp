#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>

using namespace std;

//prints out matrix
void printMatrix( vector<vector<double>> vec, ofstream &out, bool t) {
    for (int i = 0; i < vec.size(); i++)
    {
        for (int j = 0; j < vec[i].size(); j++)
        {        
            out << vec[i][j];
            //adds superscript just for growth matrix
            if (t) {
                out << "^t";
            }
            out << "\t";
        }
        out << "\n";
    }
    out << "\n";
}

//multiplies eigenvector by a value
vector<vector<double>> multiplyEigenVector(vector<vector<double>> vec, double val) {
    vector<vector<double>> result(2, vector<double>(1));
    for (int i = 0; i < vec.size(); i++){
        for (int j = 0; j < vec[i].size(); j++)
        {
          result[i][j] = vec[i][j] * val;
        }
    }
    return result;
}

//multiplies growth matrix with solutions
vector<vector<double>> multiplyMatrix(vector<vector<double>> vec, vector<vector<double>> sol) {
    vector<vector<double>> result(2, vector<double>(2));
    for (int i = 0; i < vec.size(); i++) {
        for (int j = 0; j < vec[i].size(); j++)
        {

            result[i][j] = vec[i][j] * sol[j][0];
            
        }
    }
    return result;
}

//adds two 2x1 matrixes
vector<vector<double>> addingMatrix(vector<vector<double>> vec1, vector<vector<double>> vec2) {
    vector<vector<double>> result(2, vector<double> (1));
    for (int i = 0; i < result.size(); i++) {
        for (int j = 0; j < result[i].size(); j++)
        {
            result[i][j] = vec1[i][j] + vec2[i][j];
        }
    }
    return result;
}

int main(){
    ofstream out;
    out.open("project2result.txt");

   //Investigates all possible solutions for different values of parameters 0 ≤ 𝐴 ≤ 5, 0 ≤ 𝐵 ≤ 5, 0 ≤ 𝐶 ≤ 5, 0 ≤ 𝐷 ≤ 5.
   for (double A = 0; A <= 5; A++) {
        for (double B = 0; B <= 5; B++) {
            for (double C = 0; C <= 5; C++) {
                for (double D = 0; D <= 5; D++) {
                    
                    //converts B and D into -B and -D to fit matrix
                    B *= -1;
                    D *= -1;

                    //calculates the b and c coefficient for the characteristic polynomial.
                    double polyb = -A - D;
                    double polyc = (A * D) - (B * C);
                    //calculates the eigenvalues via quadratic formula
                    double ev1 = (-polyb + sqrt(pow(polyb, 2) - (4 * polyc))) / 2;
                    
                    double ev2 = (-polyb - sqrt(pow(polyb, 2) - (4 * polyc))) / 2;
                    
                    //filters out imaginary values and skips loop
                    if (isnan(ev1) || isnan(ev2)) {
                        B *= -1;
                        D *= -1;
                        continue;
                    }
                    //creates the eigenvector matrixes
                    vector<vector<double>> u1(2, vector<double>(1));
                    vector<vector<double>> u2(2, vector<double>(1));

                    //calculates eigenvector for ev1
                    if ((A - ev1) == 0 && B == 0) {
                        if (C == 0 && (D - ev1) == 0) {
                            u1 = { {1},{0} };
                        }
                        else {
                            if (C == 0) {
                                u1 = { {1}, { 0 } };
                            }
                            else if (-(D - ev1) == 0) {
                                u1 = { {0},{1} };
                            }
                            else if (C == -(D - ev1)) {
                                u1 = { {1},{1} };
                            }
                            else
                                u1 = { { (-(D - ev1) / C)}, { 1 } };
                        }
                    }
                    else if (C == 0 && (D - ev1) == 0) {
                        if ((A - ev1) == 0 && B == 0) {
                            u1 = { {1},{0} };
                        }
                        else {
                            if ((A - ev1) == 0) {
                                u1 = { { 1}, { 0} };
                            }
                            else if (-B == 0) {
                                u1 = { {0},{1} };
                            }
                            else if (-B == (A - ev1)) {
                                u1 = { {1},{1} };
                            }
                            else
                                u1 = { { (-B / (A - ev1))}, { 1} };
                        }
                            
                    }
                    else {
                        if (B == 0 && (D-ev1) == 0) {
                            u1 = { {0},{1} };
                        }
                        else if((A - ev1) == 0 && C == 0){
                            u1 = { { 1}, { 0} };
                        }
                        else
                        u1 = { {-B / (A - ev1)}, {(-C * (-B / (A - ev1))) / (D - ev1)} };
                    }

                    //calculates eigenvector for ev2
                    if ((A - ev2) == 0 && B == 0) {
                        if (C == 0 && (D - ev2) == 0) {
                            u2 = { {0},{1} };
                        }
                        else {
                            if (C == 0) {
                                u2 = { {1}, { 0 } };
                            }
                            else if (-(D - ev2) == 0) {
                                u2 = { {0},{1} };
                            }
                            else if (C == -(D - ev2)) {
                                u2 = { {1},{1} };
                            }
                            else
                            u2 = { { (-(D - ev2) / C)}, { 1 } };
                        }
                            
                    }
                    else if (C == 0 && (D - ev2) == 0) {
                        if ((A - ev2) == 0 && B == 0) {
                            u2 = { {0},{1} };
                        }
                        else {
                            if ((A - ev2) == 0) {
                                u2 = { {1}, { 0} };
                            }
                            else if (-B == 0) {
                                u2 = { {0},{1} };
                            }
                            else if (-B == (A - ev2)) {
                                u2 = { {1},{1} };
                            }
                            else
                            u2 = { { (-B / (A - ev2))}, { 1 } };
                        }
                            
                    }
                    else {
                        if (B == 0 && (D-ev2) == 0) {
                            u2 = { {0},{1} };
                        }
                        else if ((A - ev2) == 0 && C==0) {
                            u2 = { { 1}, { 0} };
                        }
                        else
                        u2 = { {-B / (A - ev2)}, {(-C * (-B / (A - ev2))) / (D - ev2)} };
                    }

                         //solves for the matrix containing x(t) and y(t)
                        vector<vector<double>> solPart1 = multiplyEigenVector(u1, (C * pow(2.71828, ev1)));
                        vector<vector<double>> solPart2 = multiplyEigenVector(u2, (C * pow(2.71828, ev2)));
                        vector<vector<double>> solution = addingMatrix(solPart1, solPart2);

                        out << "A: " << A << "\tB: " << -1 * B << "\tC: " << C << "\tD: " << -1 * D << "\t" << "\n\n";
                        out << "eigenvalue 1: " << ev1 << "\neigenvalue 2: " << ev2 << "\n\n";
                        out << "eigenvector 1:\n";
                        printMatrix(u1, out, false);
                        out << "eigenvector 2:\n";
                        printMatrix(u2, out, false);
                        out << "Solution:\n";
                        printMatrix(solution, out, true);

                        vector<vector<double>> matrix = {{A,B}, {C,D}};
                        vector<vector<double>> finalMatrix = multiplyMatrix(matrix, solution);

                        out << "Growth Matrix: \n";
                        printMatrix(finalMatrix, out, true);

                        out << "\n\n";
                        
                        //reverts B and D back to positive values to be used by for loops
                        B *= -1;
                        D *= -1;
                }
            }
        }
    }
   
    out.close();
    return 0;
}
