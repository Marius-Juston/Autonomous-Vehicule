#include "headers/move.h"
#include "headers/zeros.h"

using namespace std;

vector<vector<float> > move(int dy, int dx, vector<vector<float> > &beliefs) {
    unsigned int height = beliefs.size(), width = beliefs[0].size();

    vector<vector<float> > newGrid = zeros(height, width);

    unsigned int j;
    unsigned int i;

    for (unsigned int k = 0; k < height * width; ++k) {
        i = k / width;
        j = k % width;
        newGrid[(i + dy + height) % height][(j + dx + width) % width] = beliefs[i][j];
    }
    return newGrid;
}
