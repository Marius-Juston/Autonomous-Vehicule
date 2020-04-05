#include "headers/move.h"
#include "headers/zeros.h"

using namespace std;

vector<vector<float> > move(int dy, int dx, vector<vector<float> > &beliefs) {
    unsigned int height = beliefs.size(), width = beliefs[0].size(), i, j, total = height * width, k;

    vector<vector<float> > newGrid = zeros(height, width);

    for (k = 0; k < total; ++k) {
        i = k / width;
        j = k % width;
        newGrid[(i + dy + height) % height][(j + dx + width) % width] = beliefs[i][j];
    }
    return newGrid;
}
