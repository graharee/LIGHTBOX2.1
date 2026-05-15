#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>


#ifndef UTILS_H
#define UTILS_H

void Delay(volatile int cycles);
void Send_OE_Vsync(uint8_t deviceNumber);
uint32_t ReadDipSwitchState();
void Fan_SetPWM(uint8_t percent);

#endif // UTILS_H
