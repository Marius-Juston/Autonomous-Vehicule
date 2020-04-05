// Example.h : Include file for standard system include files,
// or project specific include files.

#pragma once

#define _USE_MATH_DEFINES

#include <iostream>
#include <cmath>

class Gaussian {
private:
    float mu, variance;
public:
    Gaussian();

    Gaussian(float mu, float variance);

    float getVariance() const;

    float getMu() const;

    void setMu(float newMu);

    void setVariance(float newVariance);

    float evaluate(float x);

    Gaussian mul(Gaussian other);

    Gaussian add(Gaussian other);
};