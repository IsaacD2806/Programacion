#include <iostream>

enum Semáforo
{
    ROJO,
    AMARILLO,
    VERDE
};

// void no devuelve nada, solo ejecuta la acción de imprimir
void imprimirAviso(Semáforo color)
{
    if (color == ROJO)
    {
        std::cout << "¡ALTO! No puedes pasar." << std::endl;
    }
    else if (color == AMARILLO) {
        std::cout <<"Espera";
    }
    else {
        std::cout <<"Puedes pasar";
    }
}

int main()
{
    Semáforo miLuz = VERDE;
    imprimirAviso(miLuz); // Salida: ¡ALTO! No puedes pasar.
    return 0;
}