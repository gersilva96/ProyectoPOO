
#include <iostream>
#include <stdlib.h>
using namespace std;
#include "XmlRpc/XmlRpc.h"
using namespace XmlRpc;

int main(int argc, char *argv[]) {
  int port = 8000;

  XmlRpcClient client("127.0.0.1", port);
  XmlRpcValue noArgs, result, result2;

  // XmlRpcValue oneArg;
  // oneArg[0] = "sayHello";

  client.execute("saludar", noArgs, result);
  cout << result << endl << endl;

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

  return 0;
}
