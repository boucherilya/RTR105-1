// 180.c Sagatave funkcijas integrēšanai ar taisnstūru metodi

#include <stdio.h>

#include <math.h>


// Lietotāja pētāmā funkcija

double f1 (double x) {
 
    return sqrt(x*x);

}



int main () {
 
    // k - iterācijas numurs pēc kārtas

    int k;
 
   // a, b – argumentu intervāls

    // I1 – iepriekšējais Integrālis,

    // I2 – tekošais Integrālis, kur 'eps' ir rezultāta

    double a=-2, b=2, I1 = 0. ,I2, h;

    double eps=0.001;
 
   // precizitāte angliski saukta "varepsilon"

    double n = 0.000001;
 
   // Tādā veidā aprēķina integrāļa tuvinājumu

    I2 = (b-a) * ( f1(a) + f1(b) ) / 2;

    // Tādā veidā, salīdzinot funkcijas summas tekošās

    while ( fabs(I2-I1) > eps) {
 
        // vērtības precizitāti ar pieļaujamo eps vērtību,

        n=n*2; 	// palielina intervālu skaitu 2 reizes,

        h=(b-a)/n; // nosaka intervāla platuma vērtību,

        I1=I2; // saglabā tekošo vērtību mainīgajā I1

        I2=0; // Tekošā summas (integrāļa) vērtība tiek nonullēta

        for (k=0; k < n; k++)

            I2 = I2 + h * f1( a + (k + .5) * h); // Summa no visiem laukumiņiem dod integrāļa tuvināto vērtību

    }
 
   char str[12];

    sprintf(str, "%f", I2);


    printf(str); // Izvadam rezultātus gadījumā, ja divu aprēķināto

    // integrāļu vērtības ir tik tuvas, ka ir mazākas

    // par mainīgā 'eps' vērtību.


}
