//
// Created by mariu on 4/3/2020.
//

#ifndef C_MATRIX_H
#define C_MATRIX_H

#include <vector>
#include <iostream>

class Matrix {
private:
    std::vector<float>::size_type rows;
    std::vector<float>::size_type cols;
    std::vector<std::vector<float>> grid;
public:
    Matrix();

    Matrix(std::vector<std::vector<float>> grid);

    Matrix(float initialValue, int rows, int columns);

    unsigned int getRows() const;

    unsigned int getCols() const;

    std::vector<std::vector<float>> getGrid();

    void setGrid(const std::vector<std::vector<float>> &grid);

    Matrix matrix_transpose();

    Matrix matrix_add(Matrix other);

    void matrix_print();
};


#endif //C_MATRIX_H
