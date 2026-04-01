#ifndef TMP1075_H
#define TMP1075_H

#include <stdint.h>
#include <string.h>


/*------------------Reg_map---------------------------*/

typedef enum {
    tmp1075_temp_reg = 0x00u,    // Temperature register
    tmp1075_cfgr_reg = 0x01u,    // Configuration register
    tmp1075_llim_reg = 0x02u,    // TLOW register
    tmp1075_hlim_reg = 0x03u,   // THIGH register
    tmp1075_dieid_reg= 0x0Fu // Device ID register (not available on TMP1075N)
} TMP1075_RegAddr_t;


/*----------------Dev Address -----------------------------*/
typedef enum{
	tmp1075_micro_address = 0x52,
	tmp1075_driver_address = 0x40,
	tmp1075_back_address = 0x58,
}TMP1075_DevAddr_t;

/*-------------------------Temp-Register-------------------*/

// read only 
// 0000h reset

typedef struct 
{
   uint16_t RESERVED  : 4;
   uint16_t READ_TEMP : 12; 
}TMP1075_TEMP_REG_t;


/*-------------------------Config - Register --------------*/

//read/write
// 00FFh reset

typedef enum
{
    tmp1075_one_shot_start = 0x01,
}TMP1075_ONE_SHOT_t;

typedef enum
{
    tmp1075_CONVERSION_27_5_ms = 0x00,
    tmp1075_CONVERSION_55_ms   = 0x01,
    tmp1075_CONVERSION_110_ms  = 0x02,
    tmp1075_CONVERSION_220_ms  = 0x03,
} TMP1075_CONVERSION_RATE_t;

typedef enum
{
    tmp1075_FAULT_QUEUE_1 = 0x00,
    tmp1075_FAULT_QUEUE_2 = 0x01,
    tmp1075_FAULT_QUEUE_4 = 0x02,
    tmp1075_FAULT_QUEUE_6 = 0x03,
} TMP1075_FAULT_QUEUE_t;

typedef enum
{
    tmp1075_ALERT_POL_LOW  = 0x00, // ALERT active low
    tmp1075_ALERT_POL_HIGH = 0x01, // ALERT active high
} TMP1075_ALERT_POL_t;

typedef enum
{
    tmp1075_THERMOSTAT_MODE_COMPARATOR = 0x00, // Comparator mode
    tmp1075_THERMOSTAT_MODE_INTERRUPT  = 0x01, // Interrupt mode
} TMP1075_THERMOSTAT_MODE_t;

typedef enum
{
    tmp1075_SHUTDOWN_MODE_DISABLE = 0x00, // Continuous conversion
    tmp1075_SHUTDOWN_MODE_ENABLE  = 0x01, // Shutdown mode
} TMP1075_SHUTDOWN_MODE_t;

typedef struct
{
    uint16_t RES : 8;       // Reserved bits
    uint16_t SD  : 1;       // Shutdown mode
    uint16_t TM  : 1;       // Thermostat mode
    uint16_t POL : 1;       // ALERT pin polarity
    uint16_t F   : 2;       // Fault queue select bits [F1:F0]
    uint16_t R   : 2;       // Conversion rate select bits [R1:R0]
    uint16_t OS  : 1;       // One-shot conversion start
} TMP1075_ConfigReg_t;

/*---------------------------llim-register---------------*/

// read/write

typedef struct
{
    uint16_t RESERVED : 4;
    uint16_t LLIM     : 12;
}TMP1075_LLIM_REG_t;

/*--------------------------hlim-register---------------------*/

typedef struct
{
    uint16_t RESERVED : 4;
    uint16_t HLIM     : 12;
}TMP1075_HLIM_REG_t;


/*------------------------------dieid--------------------------*/

typedef struct
{
   uint16_t DIEID   : 16; 
}TMP1075_DIEID_REG_t;

/*------------------------Control Messages -------------------------*/


typedef struct 
{
    uint8_t POINTER_REG    : 8;
    uint8_t DATA_1         : 8;
    uint8_t DATA_2         : 8;
}TMP1075_Write_Word_Cmd_t;

typedef struct 
{
    uint8_t POINTER_REG    : 8;
    uint8_t DATA           : 8;
}TMP1075_Write_Single_Cmd_t;

typedef struct 
{
    uint8_t POINTER_REG         : 8;
}TMP1075_Read_Single_Cmd_t;

void TMP1075_WriteWord(TMP1075_Write_Word_Cmd_t* tmp1075_write_word_cmd, uint8_t* u8p_buffer);
void TMP1075_WriteSingle(TMP1075_Write_Single_Cmd_t* tmp1075_write_single_cmd, uint8_t* u8p_buffer);
void TMP1075_Read_Pointer(TMP1075_Write_Single_Cmd_t* tmp1075_write_single_cmd, uint8_t* u8p_buffer);

#endif


