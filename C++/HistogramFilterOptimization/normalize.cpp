#include "headers/normalize.h"

using namespace std;

vector<vector<float> > normalize(vector<vector<float> > &grid) {
    float total = 0.0;
    for (const vector<float> &r: grid) {
        for (float e : r) {
            total += e;
        }
    }

    unsigned int i, j, height = grid.size(), width = grid[0].size(), area = height * width, k;

    vector<vector<float >> newGrid(height, vector<float>(width));

    for (k = 0; k < area; ++k) {
        i = k / width;
        j = k % height;

        newGrid[i][j] = grid[i][j] / total;
    }

    return newGrid;
}
