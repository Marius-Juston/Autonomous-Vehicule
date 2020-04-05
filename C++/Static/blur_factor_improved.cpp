#include "blur_factor_improved.hpp"

using namespace std;

vector<vector<float> > blur_factor_improved() {

    // 2D vector reprenting the blur filter
    static float blurring = 0.12, corner = blurring / 12.0f, adjacent = blurring / 6.0f;

    static vector<vector<float> > window = {{corner,   adjacent,        corner},
                                            {adjacent, 1.0f - blurring, adjacent},
                                            {corner,   adjacent,        corner}};

    return window;
}

