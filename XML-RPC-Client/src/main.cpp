
#include <iostream>
#include <stdlib.h>
using namespace std;
#include "XmlRpc/XmlRpc.h"
using namespace XmlRpc;

void sumar(XmlRpc::XmlRpcClient client);
void restar(XmlRpc::XmlRpcClient client);
void multiplicar(XmlRpc::XmlRpcClient client);
void dividir(XmlRpc::XmlRpcClient client);

int main(int argc, char *argv[]) {
  int port = 8000;
  bool inMenu = true;

  XmlRpcClient client("127.0.0.1", port);
  XmlRpcValue noArgs, result, result2;

  client.execute("saludar", noArgs, result);
  cout << result << endl << endl;

  while (inMenu) {
    int opc = 1;
    do {
      if (opc < 0 || opc > 4) {
        cout << "Opción invalida..." << endl;
      }
      cout << "Menú:" << endl
      << "1: Sumar dos números" << endl
      << "2: Restar dos números" << endl
      << "3: Multiplicar dos números" << endl
      << "4: Dividir dos números" << endl
      << "0: Salir" << endl << endl
      << "Ingrese opción: ";
      cin >> opc;
      cout << endl;
    } while (opc < 0 || opc > 4);
    switch (opc) {
      case 0:
        inMenu = false;
        client.execute("despedir", noArgs, result);
        cout << result << endl;
        break;
      case 1:
        sumar(client);
        break;
      case 2:
        restar(client);
        break;
      case 3:
        multiplicar(client);
        break;
      case 4:
        dividir(client);
        break;
      default:
        break;
    }
  }

  // XmlRpcValue oneArg;
  // oneArg[0] = "sayHello";

  return 0;
}

void sumar(XmlRpc::XmlRpcClient client) {
  XmlRpcValue result;
  int a;
  int b;

  cout << "Ingrese el primero: ";
  cin >> a;
	cout << "Ingrese el segundo: ";
  cin >> b;

  XmlRpcValue numbers;
  numbers[0] = a;
  numbers[1] = b;

  client.execute("sumar", numbers, result);
  cout << endl << "La suma es: " << result << endl << endl;
}

void restar(XmlRpc::XmlRpcClient client) {
  XmlRpcValue result;
  int a;
  int b;

  cout << "Ingrese el primero: ";
  cin >> a;
	cout << "Ingrese el segundo: ";
  cin >> b;

  XmlRpcValue numbers;
  numbers[0] = a;
  numbers[1] = b;

  client.execute("restar", numbers, result);
  cout << endl << "La resta es: " << result << endl << endl;
}

void multiplicar(XmlRpc::XmlRpcClient client) {
  XmlRpcValue result;
  int a;
  int b;

  cout << "Ingrese el primero: ";
  cin >> a;
	cout << "Ingrese el segundo: ";
  cin >> b;

  XmlRpcValue numbers;
  numbers[0] = a;
  numbers[1] = b;

  client.execute("multiplicar", numbers, result);
  cout << endl << "La multiplicación es: " << result << endl << endl;
}

void dividir(XmlRpc::XmlRpcClient client) {
  XmlRpcValue result;
  int a;
  int b;

  cout << "Ingrese el primero: ";
  cin >> a;
	cout << "Ingrese el segundo: ";
  cin >> b;

  XmlRpcValue numbers;
  numbers[0] = a;
  numbers[1] = b;

  client.execute("dividir", numbers, result);
  cout << endl << "La división es: " << result << endl << endl;
}