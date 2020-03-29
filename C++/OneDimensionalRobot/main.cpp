#include <iostream>
#include <vector>

using namespace std;

int getIndex(int x, int size);

vector<float> move(vector<float> p, int movement, float pExact, float pOvershoot, float pUndershoot);

vector<float> sense(vector<float> p, char measurement, vector<char> world, float pHit, float pMiss);

void show(const vector<float> &p);

int main() {
    int worldSize = 5;

    vector<float> p(worldSize, 1.0 / worldSize);

    vector<char> world = {'g', 'r', 'r', 'g', 'g'};
    vector<char> measurements = {'r', 'g'};
    vector<int> motions = {1, 1};

    float pHit = .6;
    float pMiss = .2;
    float pExact = .8;
    float pOvershoot = .1;
    float pUndershoot = .1;

    show(p);

    for (int i = 0; i < measurements.size(); ++i) {
        p = sense(p, measurements[i], world, pHit, pMiss);
        p = move(p, motions[i], pExact, pOvershoot, pUndershoot);
    }

    show(p);

    return 0;
}

void show(const vector<float> &p) {
    for (float e: p) {
        cout << e << ' ';
    }
    cout << endl;
}

vector<float> sense(vector<float> p, char measurement, vector<char> world, float pHit, float pMiss) {
    int size = p.size();
    vector<float> q(size);

    float sum = 0;
    float hit;
    float prob;

    for (int i = 0; i < size; ++i) {
        hit = measurement == world[i];
        prob = p[i] * (hit * pHit + (1 - hit) * pMiss);

        q[i] = prob;
        sum += prob;
    }

    for (float &j : q) {
        j = j / sum;
    }

    return q;
}

vector<float> move(vector<float> p, int movement, float pExact, float pOvershoot, float pUndershoot) {
    int size = p.size();
    vector<float> q(size);

    for (int i = 0; i < size; ++i) {
        float s = pExact * p[getIndex(i - movement, size)];
        s += (pOvershoot * p[getIndex(i - movement - 1, size)]);
        s += (pUndershoot * p[getIndex(i - movement + 1, size)]);

        q[i] = s;
    }

    return q;
}

int getIndex(int x, int size) {
    return (size + x % size) % size;
}
