#include <bits/stdc++.h>
#include <iostream>
#define MAX 256
using namespace std;

int main(void) {
    vector<string> men, women;
    char name[20];
    
    // Open file
    ifstream infile;
    infile.open("input.txt");
    
    // No of members from each gender
    int n;
    cin >> n;

    // Read men and women names
    for (int i = 0; i < n; i++) {
        infile >> name;
        men.push_back(name);
    }
    for (int i = 0; i < n; i++) {
        infile >> name;
        women.push_back(name);
    }

    // Read their preferences
    map<string, vector<string> > menPref, womenPref;

    for (int i = 0; i < n; i++) {
        vector<string> pref;
        for (int j = 0; j < n; j++) {
            infile >> name;
            pref.push_back(name);
        }
        menPref.insert(make_pair(men.at(i), pref));
    }
    for (int i = 0; i < n; i++) {
        vector<string> pref;
        for (int j = 0; j < n; j++) {
            infile >> name;
            pref.push_back(name);
        }
        womenPref.insert(make_pair(women.at(i), pref));
    }

    // Make Free man queue
    queue<string> freeMan;
    for (int i = 0; i < n; i++) {
        freeMan.push(men.at(i));
    }
    
    map<string, string> marriage;
    while(!(freeMan.empty())) {
        string name = freeMan.front();
        vector<string> pref = menPref.at(name);
        
    }


}