#include "TMP1075.h"
#include "TMP1075_Interface.h"
#include "sdk_project_config.h"

#define TMP1075_TEMP_DATA_SIZE   (2u)
#define TMP1075_POINTER_SIZE     (1u)
#define TMP1075_WRITE_SINGLE_SIZE (2u)
#define TMP1075_WRITE_WORD_SIZE   (3u)

/*****************************************************************************************************************
 *                   Global Variables
 *****************************************************************************************************************/

TMP1075_Write_Single_Cmd_t config_write =
{
    .POINTER_REG = tmp1075_cfgr_reg,
    .DATA        = 0x00,
};

TMP1075_Read_Single_Cmd_t temp_read =
{
    .POINTER_REG = tmp1075_temp_reg,
};

TMP1075_Write_Word_Cmd_t llir_write =
{
    .POINTER_REG = 0x00,
    .DATA_1      = 0x00,
    .DATA_2      = 0x00,
};

TMP1075_Write_Word_Cmd_t hlir_write =
{
    .POINTER_REG = 0x00,
    .DATA_1      = 0x00,
    .DATA_2      = 0x00,
};

/*****************************************************************************************************************
 *                  Private Helper Functions
 *****************************************************************************************************************/

static float TMP1075_Convert_Raw_To_Celsius(uint8_t msb, uint8_t lsb)
{
    int16_t rawTemperature;
    float temperatureCelsius;

    rawTemperature = (int16_t)((msb << 8) | lsb);

    rawTemperature >>= 4;

    if ((rawTemperature & 0x0800) != 0u)
    {
        rawTemperature |= 0xF000;
    }

    temperatureCelsius = rawTemperature * 0.0625f;

    return temperatureCelsius;
}

static float TMP1075_Read_Temp_From_Address(uint8_t sensorAddress)
{
    uint8_t masterDataSend[TMP1075_WRITE_SINGLE_SIZE];
    uint8_t masterDataReceive[TMP1075_TEMP_DATA_SIZE];

    TMP1075_Read_Pointer(&temp_read, masterDataSend);

    LPI2C_DRV_MasterSetSlaveAddr(INST_LPI2C0, sensorAddress, false);

    LPI2C_DRV_MasterSendDataBlocking(
        INST_LPI2C0,
        masterDataSend,
        TMP1075_POINTER_SIZE,
        true,
        OSIF_WAIT_FOREVER
    );

    LPI2C_DRV_MasterReceiveDataBlocking(
        INST_LPI2C0,
        masterDataReceive,
        TMP1075_TEMP_DATA_SIZE,
        true,
        OSIF_WAIT_FOREVER
    );

    return TMP1075_Convert_Raw_To_Celsius(masterDataReceive[0], masterDataReceive[1]);
}

/*****************************************************************************************************************
 *                  Code Space
 *****************************************************************************************************************/

void TMP1075_Write_Config_1(void)
{
    uint8_t masterDataSend[TMP1075_WRITE_SINGLE_SIZE];

    TMP1075_WriteSingle(&config_write, masterDataSend);

    LPI2C_DRV_MasterSetSlaveAddr(INST_LPI2C0, tmp1075_driver_address, false);

    LPI2C_DRV_MasterSendDataBlocking(
        INST_LPI2C0,
        masterDataSend,
        TMP1075_WRITE_SINGLE_SIZE,
        true,
        OSIF_WAIT_FOREVER
    );
}

void TMP1075_Write_LLIR(void)
{
    uint8_t masterDataSend[TMP1075_WRITE_WORD_SIZE];

    TMP1075_WriteWord(&llir_write, masterDataSend);

    LPI2C_DRV_MasterSetSlaveAddr(INST_LPI2C0, tmp1075_driver_address, false);

    LPI2C_DRV_MasterSendDataBlocking(
        INST_LPI2C0,
        masterDataSend,
        TMP1075_WRITE_WORD_SIZE,
        true,
        OSIF_WAIT_FOREVER
    );
}

void TMP1075_Write_HLIR(void)
{
    uint8_t masterDataSend[TMP1075_WRITE_WORD_SIZE];

    TMP1075_WriteWord(&hlir_write, masterDataSend);

    LPI2C_DRV_MasterSetSlaveAddr(INST_LPI2C0, tmp1075_driver_address, false);

    LPI2C_DRV_MasterSendDataBlocking(
        INST_LPI2C0,
        masterDataSend,
        TMP1075_WRITE_WORD_SIZE,
        true,
        OSIF_WAIT_FOREVER
    );
}

float TMP1075_Read_Temp_Micro(void)
{
    return TMP1075_Read_Temp_From_Address(tmp1075_micro_address);
}

float TMP1075_Read_Temp_Driver(void)
{
    return TMP1075_Read_Temp_From_Address(tmp1075_driver_address);
}

float TMP1075_Read_Temp_Back(void)
{
    return TMP1075_Read_Temp_From_Address(tmp1075_back_address);
}