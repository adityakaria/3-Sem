#include <bits/stdc++.h>
using namespace std;

char source = 'S', dest = 'T', inter = 'I';
void findSol(int n, char source, char dest, char inter);

int main(void) {
    int n;
    cout << "Enter number of Disks";
    cin >> n;

    findSol(n, source, dest, inter);
    return 0;
}

void findSol(int n, char source, char dest, char inter) {
    if (n == 1) {
        cout << "Move disk " << n << " from " << source << " to " << dest << endl;
    }
    else {
        findSol(n-1, source, inter, dest);
        cout << "Move disk " << n << " from " << source << " to " << dest << endl;
        findSol(n-1, inter, dest, source);
    }
}