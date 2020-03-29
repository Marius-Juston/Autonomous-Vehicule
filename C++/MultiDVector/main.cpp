//TODO: include the iostream and vector libraries
#include <iostream>
#include <vector>

//TODO: Use the standard namespace
using namespace std;


vector<vector<int >> matrixAdd(const vector<vector<int >> &matrix1, const vector<vector<int >> &matrix2);

void matrixShow(const vector<vector<int>> &matrix) {
    for (const auto &i : matrix) {
        for (int j : i) {
            cout << j << ' ';
        }
        cout << endl;
    }
}


int main() {
    vector<vector<int>> twoVector(5, vector<int>(3, 2));
    vector<vector<int>> twoVector2(5, vector<int>(3, 4));

    vector<vector<int>> added = matrixAdd(twoVector, twoVector2);
    matrixShow(added);

    return 0;
}

vector<vector<int >> matrixAdd(const vector<vector<int >> &matrix1, const vector<vector<int >> &matrix2) {
    int cols = matrix1[0].size();

    vector<vector<int>> f(matrix1.size(), vector<int>(cols, 0));

    for (int i = 0; i < matrix1.size(); ++i) {
        for (int j = 0; j < cols; ++j) {
            f[i][j] = matrix1[i][j] + matrix2[i][j];
        }
    }

    return f;
}
