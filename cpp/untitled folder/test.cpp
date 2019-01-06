#include <iostream>
using namespace std;

template <class T>
class node {
    public:
        T a[2], next, prev;
        T add();
        node();
};

template <class T>
node<T>::node() {
    cout << "Enter first number: ";
    cin>>a[0];
    cout << "Enter second Number: ";
    cin >> a[1];
}

template <class T>
T node<T>::add() {
    return a[0] + a[1];
}

int main() {
    node<float> first;
    cout << first.a[0] << " + " << first.a[1] << " is: " << first.add() << endl;
}

// int main(void) {
//     int x = 10, y = 20;
//     cout << add<int>(x, y) << endl;
//     float c = 20.1, r = 12.45;
//     cout << add<float>(c, r) << endl;
//     return 0;
// }