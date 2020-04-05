#include "scalar_multiply_improved.hpp"

using namespace std;

vector<vector<int> > scalar_multiply_improved(vector<vector<int> > matrix, int scalar) {

    // OPTIMIZATION: Instead of creating a new variable
    // called resultmatrix, update the input matrix directly

    vector<int>::size_type num_rows = matrix.size();
    vector<int>::size_type num_cols = matrix[0].size();
    unsigned int r;
    unsigned int c;
    unsigned int total_size = num_rows * num_cols;

    for (int i = 0; i < total_size; i++) {
        r = i / num_cols;
        c = i % num_cols;
        matrix[r][c] = matrix[r][c] * scalar;
    }

    return matrix;
}
