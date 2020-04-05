#include "headers/normalize.h"

using namespace std;

vector<vector<float> > normalize(vector<vector<float> > &grid) {
    float total = 0.0;
    for (const vector<float> &r: grid) {
        for (float e : r) {
            total += e;
        }
    }

    unsigned int i;
    unsigned int j;
    vector<float> newRow;
    unsigned int height = grid.size(), width = grid[0].size();

    vector<vector<float >> newGrid;

    for (i = 0; i < height; i++) {
        newRow.clear();
        for (j = 0; j < width; j++) {
            float newProb = grid[i][j] / total;
            newRow.push_back(newProb);
        }
        newGrid.push_back(newRow);
    }

    return newGrid;
}
