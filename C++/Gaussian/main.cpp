//
// Created by mariu on 4/3/2020.
//

#include "gaussian.h"
#include <iostream>

using namespace std;

int main() {
    Gaussian gaussianA(30, 100);
    Gaussian gaussianB(10, 25);

    std::cout << "average " << gaussianA.getMu() << std::endl;
    std::cout << "evaluation " << gaussianA.evaluate(15.0) << std::endl;

    std::cout << "mul results variance " << gaussianA.mul(gaussianB).getVariance() << std::endl;
    std::cout << "mul results average " << gaussianA.mul(gaussianB).getMu() << std::endl;

    std::cout << "add results variance " << gaussianA.add(gaussianB).getVariance() << std::endl;
    std::cout << "add results average " << gaussianA.add(gaussianB).getMu() << std::endl;


    return 0;
};
