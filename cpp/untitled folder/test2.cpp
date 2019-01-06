#include <iostream>
#include <deque>
using namespace std;

int main(void) {
    deque<int> d(5);

    for (int i = 0; i < d.size(); i++) {
        d[i] = i+1;
    }

    d.push_back(10);
    d.push_front(0);

    for (int i = 0; i < d.size(); i++) {
        cout << d[i] << endl;
    }
}