#include <iostream>
#include <string>

using namespace std;

int main() {
    string nome;
    int idade;
    string cidade;

    cout << "Qual é o seu nome? ";
    cin >> nome;

    cout << "Quantos anos você tem? ";
    cin >> idade;

    cout << "Aonde você mora? ";
    cin >> cidade;

    cout << nome << " tem " << idade << " anos e mora em " << cidade << "\n";

    return 0;
}