#include <iostream>
#include <fstream>

using namespace std;

int main(){
    ofstream file ("test1.txt");
    for (int i=0;i<25000000;i++){
        int temp = rand() % 100;
        file << temp << " ";
    }
    return 0;
}