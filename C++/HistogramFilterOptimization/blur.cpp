#include "headers/blur.h"
#include "headers/zeros.h"

using namespace std;

// OPTIMIZATION: Pass large variable by reference
vector<vector<float> > blur(vector<vector<float> > &grid, float blurring) {

    // OPTIMIZATION: window, DX and  DY variables have the
    // same value each time the function is run.
    // It's very inefficient to recalculate the vectors
    // every time the function runs. 
    // 
    // The const and/or static operator could be useful.
    // Define and declare window, DX, and DY using the
    // bracket syntax: vector<int> foo = {1, 2, 3, 4} 
    // instead of calculating these vectors with for loops 
    // and push back

    // 2D vector reprenting the blur filter
    float corner = blurring / 12.0f, adjacent = blurring / 6.0f;

    vector<vector<float> > window = {{corner,   adjacent,        corner},
                                     {adjacent, 1.0f - blurring, adjacent},
                                     {corner,   adjacent,        corner}};


    unsigned int height = grid.size(), width = grid[0].size();
    vector<vector<float> > newGrid = zeros(height, width);

    int ii;
    int jj;
    int j;

    for (int i = 0; i < height; ++i) {
        for (j = 0; j < width; ++j) {
            for (ii = -1; ii < 2; ++ii) {
                for (jj = -1; jj < 2; ++jj) {
                    newGrid[(i + jj + height) % height][(j + ii + width) % width] +=
                            grid[i][j] * window[ii + 1][jj + 1];
                }
            }
        }
    }

    return newGrid;
}
