#include "headers/zeros.h"

using namespace std;

vector<vector<float> > zeros(unsigned int height, unsigned int width) {
    // OPTIMIZATION: Reserve space in memory for vectors
    return vector<vector<float>>(height, vector<float>(width, 0));
}