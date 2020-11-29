#include <iostream>
#include <stdlib.h>
using namespace std;
#include "XmlRpc/XmlRpc.h"
using namespace XmlRpc;

string setAnguloArticulacionMM(XmlRpc::XmlRpcClient client, string art, string sentido, string angulo);
string setVelocidadArticulacionMM(XmlRpc::XmlRpcClient client, string art, string velocidad);
string setEstadoEfectorFinalMM(XmlRpc::XmlRpcClient client, string tiempo);
string reporteRobotMM(XmlRpc::XmlRpcClient client);


string ModoAuto() {
  int port = 8000;
  
  XmlRpcClient client("127.0.0.1", port);
  XmlRpcValue noArgs, result, result2;

  cout << setVelocidadArticulacionMM(client, "1", "0.3") << endl;
  cout << setAnguloArticulacionMM(client, "1", "A", "30") << endl;

  cout << setVelocidadArticulacionMM(client, "2", "0.1") << endl;
  cout << setAnguloArticulacionMM(client, "2", "A", "15") << endl;

  cout << setVelocidadArticulacionMM(client, "2", "0.1") << endl;
  cout << setAnguloArticulacionMM(client, "2", "H", "10") << endl;

  //cout << setVelocidadArticulacionMM(client, "3", "0.3") << endl;
  //cout << setAnguloArticulacionMM(client, "3", "A", "30") << endl;

  //cout << setEstadoEfectorFinalMM(client, "6") << endl;
    
  string mensaje = "Finalizo el modo de prueba.";

  return mensaje;
}

string setAnguloArticulacionMM(XmlRpc::XmlRpcClient client , string art, string sentido, string angulo) {
  XmlRpcValue result;
  XmlRpcValue params;
  params[0] = art;
  params[1] = sentido;
  params[2] = angulo;
  client.execute("setAnguloArticulacion", params, result);
  return result;
}

string setVelocidadArticulacionMM(XmlRpc::XmlRpcClient client, string art, string velocidad){
  XmlRpcValue result;
  XmlRpcValue params;
  params[0] = art;
  params[1] = velocidad;
  client.execute("setVelocidadArticulacion", params, result);
  return result;
}

string setEstadoEfectorFinalMM(XmlRpc::XmlRpcClient client, string tiempo){
  XmlRpcValue result;
  XmlRpcValue params;
  params[0] = tiempo;
  client.execute("setVelocidadArticulacion", params, result);
  return result;
}


