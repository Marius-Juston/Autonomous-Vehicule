// Example.cpp : Defines the entry point for the application.
//

#include "matrix.h"
#include <iostream>

using namespace std;

int main() {
    Matrix a(.5, 4, 4);
    a.matrix_print();
    cout << endl;

    Matrix b(1, 4, 4);
    b.matrix_print();
    cout << endl;

    Matrix c = a.matrix_add(b);
    c.matrix_print();
    cout << endl;

    Matrix d({
                     {1, 2, 3},
                     {4, 5, 6}
             });
    d.matrix_print();
    cout << endl;

    d = d.matrix_transpose();
    d.matrix_print();

    return 0;
}
