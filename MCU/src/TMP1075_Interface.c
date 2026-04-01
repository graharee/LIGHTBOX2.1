


# include "TMP1075.h"
# include "TMP1075_Interface.h"
#include "sdk_project_config.h"

#define BUFF_SIZE (64u)



/*****************************************************************************************************************
 *                   Global Variables
 *****************************************************************************************************************/

TMP1075_Write_Single_Cmd_t config_write = {
    .POINTER_REG    =  tmp1075_cfgr_reg, // 0x01
    .DATA           =  0x00, // default value 00
};

TMP1075_Read_Single_Cmd_t temp_read = {
	.POINTER_REG    =  tmp1075_temp_reg,
};



TMP1075_Write_Word_Cmd_t llir_write = {
    .POINTER_REG    =  0x00, //
    .DATA_1         =  0x00, //
    .DATA_2         =  0x00  //
};

TMP1075_Write_Word_Cmd_t hlir_write = {
    .POINTER_REG    =  0x00, //
    .DATA_1         =  0x00, //
    .DATA_2         =  0x00  //
};

/*****************************************************************************************************************
 *                  Code Space
 *****************************************************************************************************************/

void TMP1075_Write_Config_1()
{
    uint8_t masterDataSend[2];
    TMP1075_WriteSingle(&config_write, masterDataSend);
    LPI2C_DRV_MasterSetSlaveAddr(INST_LPI2C0,tmp1075_driver_address,false);
    LPI2C_DRV_MasterSendDataBlocking(INST_LPI2C0, masterDataSend, 2, true, OSIF_WAIT_FOREVER);
}

void TMP1075_Write_LLIR() // function not finished
{
    uint8_t masterDataSend[3];
    TMP1075_WriteWord(&llir_write, masterDataSend);
    LPI2C_DRV_MasterSendDataBlocking(INST_LPI2C0, masterDataSend, BUFF_SIZE, true, OSIF_WAIT_FOREVER);
}

void TMP1075_Write_HLIR()  // function not finished
{
    uint8_t masterDataSend[4];
    TMP1075_WriteWord(&hlir_write, masterDataSend);
    LPI2C_DRV_MasterSendDataBlocking(INST_LPI2C0, masterDataSend, BUFF_SIZE, true, OSIF_WAIT_FOREVER);
}

float TMP1075_Read_Temp_Micro() {
    uint8_t masterDataSend[2];
    uint8_t masterDataReceive[2];
    int16_t rawTemperature;
    float temperatureCelsius;

    TMP1075_Read_Pointer(&temp_read, masterDataSend); // fill buffer with temp reg address

    LPI2C_DRV_MasterSetSlaveAddr(INST_LPI2C0, tmp1075_micro_address, false);
    LPI2C_DRV_MasterSendDataBlocking(INST_LPI2C0, masterDataSend, 1, true, OSIF_WAIT_FOREVER);
    LPI2C_DRV_MasterReceiveDataBlocking(INST_LPI2C0, masterDataReceive, 2, true, OSIF_WAIT_FOREVER);

    rawTemperature = (masterDataReceive[0] << 8) | masterDataReceive[1];
    rawTemperature >>= 4;

    if (rawTemperature & 0x800) { // check negative
        rawTemperature |= 0xF000;
    }

    temperatureCelsius = rawTemperature * 0.0625;

    return temperatureCelsius;
}

float TMP1075_Read_Temp_Driver() {
    uint8_t masterDataSend[2];
    uint8_t masterDataReceive[2];
    int16_t rawTemperature;
    float temperatureCelsius;

    TMP1075_Read_Pointer(&temp_read, masterDataSend); // fill buffer with temp reg address

    LPI2C_DRV_MasterSetSlaveAddr(INST_LPI2C0, tmp1075_driver_address, false);
    LPI2C_DRV_MasterSendDataBlocking(INST_LPI2C0, masterDataSend, 1, true, OSIF_WAIT_FOREVER);
    LPI2C_DRV_MasterReceiveDataBlocking(INST_LPI2C0, masterDataReceive, 2, true, OSIF_WAIT_FOREVER);

    rawTemperature = (masterDataReceive[0] << 8) | masterDataReceive[1];
    rawTemperature >>= 4;

    if (rawTemperature & 0x800) {  // check negative
        rawTemperature |= 0xF000;
    }

    temperatureCelsius = rawTemperature * 0.0625;

    return temperatureCelsius;
}

float TMP1075_Read_Temp_Back() {
    uint8_t masterDataSend[2];
    uint8_t masterDataReceive[2];
    int16_t rawTemperature;
    float temperatureCelsius;

    TMP1075_Read_Pointer(&temp_read, masterDataSend); // fill buffer with temp reg address


    LPI2C_DRV_MasterSetSlaveAddr(INST_LPI2C0, tmp1075_back_address, false);
    LPI2C_DRV_MasterSendDataBlocking(INST_LPI2C0, masterDataSend, 1, true, OSIF_WAIT_FOREVER);
    LPI2C_DRV_MasterReceiveDataBlocking(INST_LPI2C0, masterDataReceive, 2, true, OSIF_WAIT_FOREVER);

    rawTemperature = (masterDataReceive[0] << 8) | masterDataReceive[1];
    rawTemperature >>= 4;

    if (rawTemperature & 0x800) { // check negative
        rawTemperature |= 0xF000;
    }

    temperatureCelsius = rawTemperature * 0.0625;

    return temperatureCelsius;
}






