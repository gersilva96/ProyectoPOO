
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
  bool inModoManual = true;

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
      << "1: Iniciar modo de prueba" << endl
      << "2: Modo manual" << endl
      << "3: Ver reporte" << endl
      << "4: Ayuda de comandos" << endl
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
        while (inModoManual) {
          int opc2 = 1;
          do {
            if (opc2 < 0 || opc2 > 4) {
              cout << "Opción invalida..." << endl;
            }
            cout << "Opciones del modo manual:" << endl
            << "1: Rotar articulacion de la base " << endl
            << "2: Rotar articulacion media " << endl
            << "3: Rotar articulacion superior" << endl
            << "4: Activar efector final" << endl
            << "0: Salir del modo manual" << endl << endl
            << "Ingrese opción: ";
            cin >> opc2;
            cout << endl;
          } 
          while (opc2 < 0 || opc2 > 4);
            switch (opc2) {
              case 0:
                inModoManual = false;
                cout << "\nVolviendo al menu principal...\n" << endl;
              break;
                case 1:
                cout << "Rotando articulacion de la base\n" << endl;
              break;
              case 2:
                cout << "Rotando articulacion media" << endl;
              break;
              case 3:
                cout << "Rotando articulacion superior" << endl;
              break;
              case 4:
                cout << "Activando efector final" << endl;
              break;  
              default:
              break;
    }
  }
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