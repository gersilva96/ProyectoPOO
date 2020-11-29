#include <iostream>
#include <stdlib.h>
using namespace std;
#include "XmlRpc/XmlRpc.h"
using namespace XmlRpc;

//void saludar(XmlRpc::XmlRpcClient client);
//void despedir(XmlRpc::XmlRpcClient client);
string setAnguloArticulacion(XmlRpc::XmlRpcClient client, string art, string sentido, string angulo);
string setVelocidadArticulacion(XmlRpc::XmlRpcClient client, string art, string velocidad);
string setEstadoEfectorFinal(XmlRpc::XmlRpcClient client, string tiempo);
//void getNombreRobot(XmlRpc::XmlRpcClient client);
//void getNombreArticulacion(XmlRpc::XmlRpcClient client);
//void getNombreEfectorFinal(XmlRpc::XmlRpcClient client);
//void reporteRobot(XmlRpc::XmlRpcClient client);
//void reporteAcciones(XmlRpc::XmlRpcClient client);

int main(int argc, char *argv[]) {
  int port = 8000;
  bool inMenu = true;
  bool inModoManual = true;
  bool inArticulacion = true;
  bool inEfector = true;
  

  XmlRpcClient client("127.0.0.1", port);
  XmlRpcValue noArgs, result, result2;

  client.execute("saludar", noArgs, result);
  cout << result << endl << endl;
  client.execute("getNombreRobot", noArgs, result);
  cout << "El brazo robotico " << result << " está listo para usarse" << endl << endl;
    

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
      << "0: Salir" << endl << endl
      << "mode >> ";
      cin >> opc;
      cout << endl;
    } while (opc < 0 || opc > 4);
    switch (opc) {
      case 0://menu
        inMenu = false;
        client.execute("despedir", noArgs, result);
        cout << result << endl;
        break;
      case 1://menu
        cout << "Iniciar modo de prueba" << endl;
        break;
      case 2://menu
        inModoManual = true;
        while (inModoManual) {
          int opc2 = 1;
          do {
            if (opc2 < 1 || opc2 > 3) {
              cout << "Opción invalida..." << endl;
            }
            cout << "Opciones del modo manual:" << endl
            << "1: Modificar estado de alguna articulacion. " << endl
            << "2: Modificar estado del efector final. " << endl
            << "3: Salir del modo manual" << endl << endl
            << "mode >> manual >>  ";
            cin >> opc2;
            cout << endl;
          } 
          while (opc2 < 1 || opc2 > 3);
            switch (opc2) {
              case 1://modo manual
                inArticulacion = true;
                while (inArticulacion) {
                  int opc3 = 1;
                  do {
                    if (opc3 < 1 || opc3 > 4) {
                    cout << "Opción invalida..." << endl;
                    }
                    cout << "Opciones de la articulacion:" << endl
                    << "1: Modificar valores de la articulacion 'Base'. " << endl
                    << "2: Modificar valores de la articulacion 'Base-Codo'. " << endl
                    << "3: Modificar valores de la articulacion 'Codo-Efector Final'. " << endl
                    << "4: Volver" << endl << endl
                    << "mode >> manual >> art >> ";
                    cin >> opc3;
                    cout << endl;
                  } while (opc3 < 1 || opc3 > 4);
                  string angulo, velocidad, sentido;
                  switch (opc3) {
                    case 1://articulacion
                      cout << "\nIngrese ángulo: \n" << endl;
                      cin >> angulo;
                      cout << "\nIngrese velocidad: \n" << endl;
                      cin >> velocidad;
                      cout << "\nIngrese sentido: \n" << endl;
                      cin >> sentido;
                      cout << setVelocidadArticulacion(client, "1", velocidad) << endl;
                      cout << setAnguloArticulacion(client, "1", sentido, angulo) << endl;
                    break;
                    case 2://articulacion
                      cout << "\nIngrese ángulo: \n" << endl;
                      cin >> angulo;
                      cout << "\nIngrese velocidad: \n" << endl;
                      cin >> velocidad;
                      cout << "\nIngrese sentido: \n" << endl;
                      cin >> sentido;
                      cout << setVelocidadArticulacion(client, "2", velocidad) << endl;
                      cout << setAnguloArticulacion(client, "2", sentido, angulo) << endl;
                    break;
                    case 3://articulacion
                      cout << "\nIngrese ángulo: \n" << endl;
                      cin >> angulo;
                      cout << "\nIngrese velocidad: \n" << endl;
                      cin >> velocidad;
                      cout << "\nIngrese sentido: \n" << endl;
                      cin >> sentido;
                      cout << setVelocidadArticulacion(client, "3", velocidad) << endl;
                      cout << setAnguloArticulacion(client, "3", sentido, angulo) << endl;
                    break;
                    case 4://articulacion
                    inArticulacion = false;
                    cout << "\nVolviendo \n" << endl;
                    break;
                    default:
                    break;
                  }
                }
              break;
              case 2://modo manual
                inEfector = true;
                while (inEfector) {
                int opc4 = 1;
                do {
                  if (opc4 < 1 || opc4 > 2) {
                  cout << "Opción invalida..." << endl;
                  }
                  cout << "Opciones del modo manual:" << endl
                  << "1: Setear el efector. " << endl
                  << "2: Volver." << endl << endl
                  << "mode >> manual >> eff >>";
                  cin >> opc4;
                  cout << endl;
                } 
                while (opc4 < 1 || opc4 > 2);
                  string tiempo;
                  switch (opc4) {
                    case 1://efector
                      cout << "\nIngrese la cantidad de tiempo en segundos de actuación: \n" << endl;
                      cin >> tiempo;
                      cout << setEstadoEfectorFinal(client, tiempo) << endl;
                    break;
                    case 2://efector
                      inEfector = false;
                    break;
                    default:
                    break;
                  }
                }    
              break;
              case 3://modo manual
                inModoManual = false;
              break;
              default:
              break;
                  }
                  }
                break;
     
            }
  }
  return 0;
}

string setAnguloArticulacion(XmlRpc::XmlRpcClient client , string art, string sentido, string angulo) {
  XmlRpcValue result;
  XmlRpcValue params;
  params[0] = art;
  params[1] = sentido;
  params[2] = angulo;
  client.execute("setAnguloArticulacion", params, result);
  return result;
}

string setVelocidadArticulacion(XmlRpc::XmlRpcClient client, string art, string velocidad){
  XmlRpcValue result;
  XmlRpcValue params;
  params[0] = art;
  params[1] = velocidad;
  client.execute("setVelocidadArticulacion", params, result);
  return result;
}

string setEstadoEfectorFinal(XmlRpc::XmlRpcClient client, string tiempo){
  XmlRpcValue result;
  XmlRpcValue params;
  params[0] = tiempo;
  client.execute("setVelocidadArticulacion", params, result);
  return result;
}