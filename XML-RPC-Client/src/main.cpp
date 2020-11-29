#include <iostream>
#include <stdlib.h>
using namespace std;
#include "XmlRpc/XmlRpc.h"
using namespace XmlRpc;
#include "ModoAutomatico.h"

string setAnguloArticulacion(XmlRpc::XmlRpcClient client, string art, string sentido, string angulo);
string setVelocidadArticulacion(XmlRpc::XmlRpcClient client, string art, string velocidad);
string setEstadoEfectorFinal(XmlRpc::XmlRpcClient client, string tiempo);
string reporteRobot(XmlRpc::XmlRpcClient client);
string reporteAcciones(XmlRpc::XmlRpcClient client);
string getNombreArticulacion(XmlRpc::XmlRpcClient client, string art);
void opcionesArticulacion(XmlRpc::XmlRpcClient client, int art);

int main(int argc, char *argv[]) {
    int port = 8000;
    bool inMenu = true;
    bool inModoManual, inArticulacion, inEfector, inReport;

    XmlRpcClient client("127.0.0.1", port);
    XmlRpcValue noArgs, result, result2;

    system("clear");
    client.execute("saludar", noArgs, result);
    cout << result << endl;
    client.execute("getNombreRobot", noArgs, result);
    cout << "El brazo robótico \"" << result << "\" está listo para usarse" << endl << endl;

    while (inMenu) {
        int opc = 1;
        do {
            if (opc < 1 || opc > 4) {
                cout << "Opción <<" << opc << ">> no encontrada" << endl << endl;
            }
            cout << "Menú:" << endl
                 << "1: Modo manual" << endl
                 << "2: Modo automático" << endl
                 << "3: Reportes" << endl
                 << "4: Salir" << endl
                 << endl
                 << ">> ";
            cin >> opc;
            cout << endl;
        } while (opc < 1 || opc > 4);
        switch (opc) {
            case 1: //menu
                inModoManual = true;
                while (inModoManual) {
                    int opc2 = 1;
                    do {
                        if (opc2 < 1 || opc2 > 3) {
                            cout << "Opción <<" << opc2 << ">> no encontrada" << endl << endl;
                        }
                        cout << "Opciones del modo manual:" << endl
                            << "1: Modificar estado de alguna articulacion. " << endl
                            << "2: Modificar estado del efector final. " << endl
                            << "3: Salir del modo manual" << endl
                            << endl
                            << ">> manual >> ";
                        cin >> opc2;
                        cout << endl;
                    } while (opc2 < 1 || opc2 > 3);
                    switch (opc2) {
                        case 1: //modo manual
                            inArticulacion = true;
                            while (inArticulacion) {
                                int opc3 = 1;
                                do {
                                    if (opc3 < 1 || opc3 > 4) {
                                        cout << "Opción <<" << opc3 << ">> no encontrada" << endl << endl;
                                    }
                                    cout << "Elegir la articulación:" << endl
                                        << "1: Modificar valores de la articulacion \'" << getNombreArticulacion(client, "0") << "\'. " << endl
                                        << "2: Modificar valores de la articulacion \'" << getNombreArticulacion(client, "1") << "\'. " << endl
                                        << "3: Modificar valores de la articulacion \'" << getNombreArticulacion(client, "2") << "\'. " << endl
                                        << "4: Volver" << endl
                                        << endl
                                        << ">> manual >> art >> ";
                                    cin >> opc3;
                                    cout << endl;
                                } while (opc3 < 1 || opc3 > 4);
                                switch (opc3) {
                                    case 1:
                                        opcionesArticulacion(client, 0);
                                        break;
                                    case 2:
                                        opcionesArticulacion(client, 1);
                                        break;
                                    case 3:
                                        opcionesArticulacion(client, 2);
                                        break;
                                    case 4:
                                        inArticulacion = false;
                                        break;
                                    default:
                                        break;
                                }
                            }
                            break;
                        case 2: //modo manual
                            inEfector = true;
                            while (inEfector) {
                                int opc4 = 1;
                                do {
                                    if (opc4 < 1 || opc4 > 2) {
                                        cout << "Opción <<" << opc4 << ">> no encontrada" << endl << endl;
                                    }
                                    cout << "Opciones del modo manual:" << endl
                                        << "1: Accionar el efector. " << endl
                                        << "2: Volver." << endl
                                        << endl
                                        << ">> manual >> eff >> ";
                                    cin >> opc4;
                                    cout << endl;
                                } while (opc4 < 1 || opc4 > 2);
                                string tiempo;
                                switch (opc4) {
                                    case 1: //efector
                                        cout << ">> manual >> eff >> Ingrese la cantidad de tiempo en segundos de actuación: ";
                                        cin >> tiempo;
                                        cout << setEstadoEfectorFinal(client, tiempo) << endl;
                                        break;
                                    case 2: //efector
                                        inEfector = false;
                                        break;
                                    default:
                                        break;
                                }
                            }
                            break;
                        case 3: //modo manual
                            inModoManual = false;
                            break;
                        default:
                            break;
                    }
                }
                break;
            case 2: //menu
                cout << "Iniciando modo automático..." << endl;
                cout << ModoAuto() << endl;
                break;
            case 3:
                inReport = true;
                while (inReport) {
                    int opc = 1;
                    do {
                        if (opc < 1 || opc > 3) {
                            cout << "Opción <<" << opc << ">> no encontrada" << endl << endl;
                        }
                        cout << "Reportes posibles:" << endl
                            << "1: Reporte del robot. " << endl
                            << "2: Reporte de acciones. " << endl
                            << "3: Salir del modo reportes" << endl << endl
                            << ">> report >> ";
                        cin >> opc;
                        cout << endl;
                    } while (opc < 1 || opc > 3);
                    switch (opc) {
                        case 1:
                            cout << reporteRobot(client) << endl;
                            break;
                        case 2:
                            cout << reporteAcciones(client) << endl;
                            break;
                        case 3:
                            inReport = false;
                            break;
                        default:
                            break;
                    }
                }
                break;
            case 4: //menu
                inMenu = false;
                client.execute("despedir", noArgs, result);
                cout << result << endl;
                break;
            default:
                break;
        }
    }
    cout << "******************Programa Cliente finalizado**********************" << endl;
    return 0;
}

string setAnguloArticulacion(XmlRpc::XmlRpcClient client, string art, string sentido, string angulo) {
    XmlRpcValue result;
    XmlRpcValue params;
    params[0] = art;
    params[1] = sentido;
    params[2] = angulo;
    client.execute("setAnguloArticulacion", params, result);
    return result;
}

string setVelocidadArticulacion(XmlRpc::XmlRpcClient client, string art, string velocidad) {
    XmlRpcValue result;
    XmlRpcValue params;
    params[0] = art;
    params[1] = velocidad;
    client.execute("setVelocidadArticulacion", params, result);
    return result;
}

string setEstadoEfectorFinal(XmlRpc::XmlRpcClient client, string tiempo) {
    XmlRpcValue result;
    XmlRpcValue params;
    params[0] = tiempo;
    client.execute("setVelocidadArticulacion", params, result);
    return result;
}

string reporteRobot(XmlRpc::XmlRpcClient client) {
    XmlRpcValue result, params;
    client.execute("reporteRobot", params, result);
    return result;
}

string reporteAcciones(XmlRpc::XmlRpcClient client) {
    XmlRpcValue result, params;
    client.execute("reporteAcciones", params, result);
    return result;
}

string getNombreArticulacion(XmlRpc::XmlRpcClient client, string art) {
    XmlRpcValue result, params;
    params[0] = art;
    client.execute("getNombreArticulacion", params, result);
    return result;
}

void opcionesArticulacion(XmlRpc::XmlRpcClient client, int art) {
    bool inOpcionesArt = true;
    string result;
    while (inOpcionesArt) {
        int opc = 1;
        do {
            if (opc < 1 || opc > 3) {
                cout << "Opción <<" << opc << ">> no encontrada" << endl << endl;
            }
            cout << "Opciones de la articulación \'" << getNombreArticulacion(client, to_string(art)) << "\':" << endl
                << "1: Rotar la articulación. " << endl
                << "2: Modificar la velocidad de los movimientos. " << endl
                << "3: Volver" << endl
                << endl
                << ">> manual >> art >> \'" << getNombreArticulacion(client, to_string(art)) << "\' >> ";
            cin >> opc;
            cout << endl;
        } while (opc < 1 || opc > 3);
        string velocidad, sentido, angulo;
        switch (opc) {
            case 1:
                while (sentido != "A" && sentido != "H") {
                    cout << ">> manual >> art >> \'" << getNombreArticulacion(client, to_string(art)) << "\' >> Ingrese el sentido de rotación: ";
                    cin >> sentido;
                }
                cout << ">> manual >> art >> \'" << getNombreArticulacion(client, to_string(art)) << "\' >> Ingrese el ángulo: ";
                cin >> angulo;
                cout << setAnguloArticulacion(client, to_string(art), sentido, angulo) << endl;
                break;
            case 2:
                cout << ">> manual >> art >> \'" << getNombreArticulacion(client, to_string(art)) << "\' >> Ingrese la velocidad a setear: ";
                cin >> velocidad;
                cout << setVelocidadArticulacion(client, to_string(art), velocidad) << endl;
                break;
            case 3:
                inOpcionesArt = false;
                break;
            default:
                break;
        }
    }
}
