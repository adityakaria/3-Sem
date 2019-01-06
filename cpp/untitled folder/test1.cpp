#include<iostream>
#include<vector>
using namespace std;

template <typename T>
void printVector(vector<T> words) {
    for(int i = 0; i < words.size(); i++) {
        cout << words[i] << " ";
    }
    cout<< endl<<words.size();
    words.empty()?cout<<"True"<<endl :cout<<"False"<<endl;
}

int main(void) {
    cout<<"Enter number of elements: ";
    int n;
    cin>>n;
    vector<string> words(n);
    for(int i = 0; i < words.size(); i++) {
        cin >> words[i];
    }
    
    printVector<string>(words);

    words.resize(20);
    printVector<string>(words);
    words.push_back("Hi! I'm uninvited!");
    printVector<string>(words);

    vector<string> v = words;
    printVector<string>(v);

    vector<int> vec;
    for (int j = 0; j < 5; j++)
    vec.push_back(j+1);
    printVector<int>(vec);

    return 0;
}