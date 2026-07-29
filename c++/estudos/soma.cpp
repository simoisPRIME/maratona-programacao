#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main() {
    int x, y;

    cout << "Valor de x: ";
    cin >> x;

    cout << "Valor de y: ";
    cin >> y;

    int soma = x + y;
    int subtracao = x - y;
    int multiplicacao = x * y;

    cout << "Soma: " << soma << "\n";
    cout << "Subtracao: " << subtracao << "\n";
    cout << "Multiplicacao: " << multiplicacao << "\n";

    return 0;

}