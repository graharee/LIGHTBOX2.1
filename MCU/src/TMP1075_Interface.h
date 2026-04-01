#ifndef TMP1075_INTERFACE_H
#define TMP1075_INTERFACE_H

void TMP1075_Write_Config_1(void);
void TMP1075_Write_LLIR(void);
void TMP1075_Write_HLIR(void);
float TMP1075_Read_Temp_Micro(void);
float TMP1075_Read_Temp_Driver(void);
float TMP1075_Read_Temp_Back(void);

#endif
