#include "headers/blur.h"
#include "headers/zeros.h"

using namespace std;

vector<vector<float> > blur(vector<vector<float> > &grid, float blurring) {
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
