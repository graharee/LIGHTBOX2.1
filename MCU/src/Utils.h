#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>


#ifndef UTILS_H
#define UTILS_H

void Delay(volatile int cycles);
void Send_OE_Vsync(uint8_t deviceNumber);
uint32_t ReadDipSwitchState();

#endif // UTILS_H
