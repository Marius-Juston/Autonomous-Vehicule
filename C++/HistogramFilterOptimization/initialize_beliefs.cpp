#include "headers/initialize_beliefs.h"

using namespace std;

// OPTIMIZATION: pass large variables by reference
vector<vector<float> > initialize_beliefs(vector<vector<char> > &grid) {

    // OPTIMIZATION: Which of these variables are necessary?
    // OPTIMIZATION: Reserve space in memory for vectors
    vector<float>::size_type height = grid.size();
    vector<float>::size_type width = grid[0].size();

    vector<vector<float> > newGrid;
    vector<float> row;
    newGrid.reserve(height);
    row.reserve(width);

    float prob_per_cell = 1.0f / (height * width);

    for (int i = 0; i < width; ++i) {
        row.push_back(prob_per_cell);
    }

    for (int i = 0; i < height; ++i) {
        newGrid.push_back(row);
    }

    return newGrid;
}