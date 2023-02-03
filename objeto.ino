#include <Extension2.h>
entero MD1;
entero MD2;
MD2 := 3;
void setup(){
pinMode(MD1 , OUT );
pinMode(MD2 , OUT );

}
loop setup(){
FOWARD();
LEFT();
STOP();

}
