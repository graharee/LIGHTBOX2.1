
#ifndef MBI6353Q_INTERFACE_H
#define MBI6353Q_INTERFACE_H

/**********************************************************************
 *                              Includes
 **********************************************************************/
#include "MBI6353Q.h"

/**********************************************************************
 *                              Defines                                                                                  
 **********************************************************************/
#define DATA_SIZE 2

 /**********************************************************************
 *                         Global Variables
 **********************************************************************/

/**********************************************************************
 *                        Function Prototypes
 **********************************************************************/

void Config1Init(uint8_t* u8p_buffer);
void Config2Init(uint8_t* u8p_buffer);
void Config3Init(uint8_t* u8p_buffer);
void Config4Init(uint8_t* u8p_buffer);
void Config5Init(uint8_t* u8p_buffer);
void Config6Init(uint8_t* u8p_buffer);
void Config7Init(uint8_t* u8p_buffer);
void Config8Init(uint8_t* u8p_buffer);
void Config9Init(uint8_t* u8p_buffer);
void Config10Init(uint8_t* u8p_buffer);
void Config11Init(uint8_t* u8p_buffer);
void Config12Init(uint8_t* u8p_buffer);
void Config13Init(uint8_t* u8p_buffer);
void Config14Init(uint8_t* u8p_buffer);
void Config15Init(uint8_t* u8p_buffer);
void Config16Init(uint8_t* u8p_buffer);

void ReadConfigCommand(uint8_t *u8p_buffer);
void MaskCommand(uint8_t *u8p_buffer);
void ConfigCommand(uint8_t *u8p_buffer);
void BrightnessCommand(uint8_t *u8p_buffer);

void BrightnessInit(uint8_t *u8p_buffer);

void MBI6353Q_SendInitMsgs(void);
void MBI6353Q_ReadConfig(void);
uint8_t MBI6353Q_ReadRegister(MBI6353Q_RegAddr_t reg_address);

void MBI6353Q_WriteSingleBrightness(MBI6353Q_RegAddr_t reg_address, uint16_t brightness);
void MBI6353Q_WriteAllBrightness(uint16_t brightness);
void MBI6353Q_SetCurrent(uint16_t current);
void MBI6353Q_SetCurrentDivide(uint8_t currentDivide);
void MBI6353Q_StepBrightness(int16_t step);






#endif
/**********************************************************************
 *                           End of File                                                                                
 **********************************************************************/
