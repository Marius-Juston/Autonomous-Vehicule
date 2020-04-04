//
// Created by mariu on 4/3/2020.
//

#include "matrix.h"

Matrix::Matrix() {
    rows = 4;
    cols = 4;

    grid = std::vector<std::vector<float>>(rows, std::vector<float>(cols, 0));
}

Matrix::Matrix(std::vector<std::vector<float>> grid) {
    setGrid(grid);
}

void Matrix::setGrid(const std::vector<std::vector<float>> &grid) {
    Matrix::grid = grid;

    rows = grid.size();

    if (rows > 0) {
        cols = grid[0].size();
    } else {
        cols = 0;
    }
}

unsigned int Matrix::getRows() const {
    return rows;
}

unsigned int Matrix::getCols() const {
    return cols;
}

std::vector<std::vector<float>> Matrix::getGrid() {
    return grid;
}

Matrix Matrix::matrix_transpose() {
    std::vector<std::vector<float>> transpose = std::vector<std::vector<float>>(cols, std::vector<float>(rows, 0));

    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            transpose[c][r] = grid[r][c];
        }
    }

    return Matrix(transpose);
}

Matrix Matrix::matrix_add(Matrix other) {
    if (rows == other.rows && cols == other.cols) {
        std::vector<std::vector<float>> added = std::vector<std::vector<float>>(rows, std::vector<float>(cols, 0));

        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                added[r][c] = grid[r][c] + other.getGrid()[r][c];
            }
        }

        return Matrix(added);
    }

    throw std::invalid_argument("matrices are not the same size");
}

void Matrix::matrix_print() {
    for (const std::vector<float> &row: grid) {
        for (float e: row) {
            std::cout << e << '\t';
        }
        std::cout << std::endl;
    }
}

Matrix::Matrix(float initialValue, int rows, int columns) {
    Matrix::rows = rows;
    Matrix::cols = columns;

    grid = std::vector<std::vector<float>>(rows, std::vector<float>(cols, initialValue));
}
