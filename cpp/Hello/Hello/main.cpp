//
//  main.cpp
//  Hello
//
//  Created by Aditya J Karia on 12/10/18.
//  Copyright © 2018 Aditya J Karia. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[])
{
    int n;
    
    std::cout << "Enter value of n:\n";
    std::cin >> n;
    for (int i = 0; i < n; i++)
    {
        std::cout << i << "\t";
    }
    std::cout << "\nHello, World!\n";
    
    
    return 0;
}
