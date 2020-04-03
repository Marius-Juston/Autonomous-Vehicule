// Example.cpp : Defines the entry point for the application.
//
#include "gaussian.h"

Gaussian::Gaussian() {
    mu = 0;
    variance = 0;
}

float Gaussian::getMu() const {
    return mu;
}

void Gaussian::setMu(float newMu) {
    Gaussian::mu = newMu;
}

float Gaussian::getVariance() const {
    return variance;
}

void Gaussian::setVariance(float newVariance) {
    Gaussian::variance = newVariance;
}

Gaussian Gaussian::add(Gaussian other) {
    return {mu + other.getMu(), variance + other.getVariance()};
}

float Gaussian::evaluate(float x) {
    float numerator = exp(-0.5 * pow(x - mu, 2) / variance);
    float denominator = sqrt(2.0 * M_PI * variance);

    return numerator / denominator;
}

Gaussian Gaussian::mul(Gaussian other) {
    float denominator = variance + other.variance;
    float numerator = mu * other.variance + other.getMu() * variance;
    float newVariance = 1 / ((1 / variance) + (1 / other.variance));

    return {numerator / denominator, newVariance};
}

Gaussian::Gaussian(float mu, float variance) {
    Gaussian::mu = mu;
    Gaussian::variance = variance;
}
