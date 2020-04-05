#include "headers/sense.h"

using namespace std;

vector<vector<float> >
sense(char color, vector<vector<char> > &grid, vector<vector<float> > &beliefs, float p_hit, float p_miss) {
    unsigned int i, j, height = grid.size(), width = grid[0].size();

    for (i = 0; i < height; i++) {
        for (j = 0; j < width; j++) {
            beliefs[i][j] = beliefs[i][j] * ((grid[i][j] == color) ? p_hit : p_miss);
        }
    }
    return beliefs;
}
