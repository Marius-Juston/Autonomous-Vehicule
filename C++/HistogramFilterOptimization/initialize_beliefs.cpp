#include "headers/initialize_beliefs.h"

using namespace std;

vector<vector<float> > initialize_beliefs(vector<vector<char> > &grid) {
    unsigned int height = grid.size(), width = grid[0].size();

    return vector<vector<float>>(height, vector<float>(width, 1. / (width * height)));
}