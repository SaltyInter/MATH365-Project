#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

void printVec( vector<double> vec, int years, ofstream &output )
{
    output << years;
    
    for( const auto i : vec )
        output << "\t" << (int)i << "\t";

    output << '\n';
}

void distribution( vector<vector<double>> A, vector<double>& x, int start, int n, ofstream& o )
{

        // loop n times to obtain distribution
        for( int times = 1; times <= n; ++times, start++ ) {
            vector<double> resultVec{};

            for( int i{}; i < A.size(); ++i ) {
                double dotProd = 0;

                for( int j = 0; j < A[i].size(); ++j )
                    dotProd += A[i][j] * x[j];

                resultVec.push_back( dotProd );
            }

            printVec( resultVec, start, o );

	        // overwrite existing vector x with the final result
            x = resultVec;
        }
    }

}


int main()
{
    // transition matrix
    vector<vector<double>> a1 = {{ .50, .20, .15 },{ .25, .50, .15 },{ .25, .30, .70 }};

    // inverse transition matrix
    vector<vector<double>> inverse_a1 = { {2.59, -.809, -.383},{-1.17, 2.659, -.319},{-0.426, -0.851, 1.702}};

    // state vector
    vector<double> x0 = { 1000, 1000, 1000 };

    vector<double> ix0 = { 1000, 1000, 1000 };

    vector<vector<double>> a2 = { {0.6, 0.095, 0.05, 0.005}, {0.245, 0.5, 0.14, 0.005},{0.145, 0.395, 0.8, 0.02},{0.01, 0.01, 0.01, 0.97}};

    ofstream output;
    output.open( "dist.txt" );

    output << "Initial Dist\n" << endl << "1000\t" << "1000\t" << "1000\t" << endl;

    output << "Inverse\n";

    distribution( inverse_a1, ix0, -1, 1, output );

    output << "\nYear\n";

    distribution( a1, x0, 1, 3, output );

    x0.push_back( 200 );

    distribution( a2, x0, 4, 3, output );

    output.close();

    return 0;
}



