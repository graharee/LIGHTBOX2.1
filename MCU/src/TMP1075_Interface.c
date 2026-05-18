/******************************************************************
 *
 * TMP1075_Interface.c
 *
 * By: Reegan Graham
 *
 * Description:
 ******************************************************************/
/******************************************************************
 *                            Includes
 ******************************************************************/
#include "TMP1075.h"
#include "Utils.h"
#include "TMP1075_Interface.h"
#include "sdk_project_config.h"

/******************************************************************
 *                            Defines
 ******************************************************************/
#define TMP1075_TEMP_DATA_SIZE      2u
#define TMP1075_POINTER_SIZE        1u
#define TMP1075_WRITE_SINGLE_SIZE   2u
#define TMP1075_WRITE_WORD_SIZE     3u
#define TMP1075_NUM_SENSORS         1u

#define tmp1075_sensor_1_address   0x51
#define tmp1075_sensor_2_address   0x49
#define tmp1075_sensor_3_address   0x40
#define tmp1075_sensor_4_address   0x48
#define tmp1075_sensor_5_address   0x58
#define tmp1075_sensor_6_address   0x41
#define tmp1075_sensor_7_address   0x52

/******************************************************************
 *                       Global Variables
 ******************************************************************/
static uint8_t overTempFlag = 0u;
static uint8_t tempFault = 0u;

static const uint8_t tmp1075_sensor_addresses[TMP1075_NUM_SENSORS] =
{
    //tmp1075_sensor_1_address, // U2 -> 0b1010001, location: led side, middle top
    //tmp1075_sensor_2_address, // U3 -> 0b1001001, location: led side, middle
    tmp1075_sensor_3_address, // U4 -> 0b1000000, location: by driver u10
    //tmp1075_sensor_4_address, // U5 -> 0b1001000, location: led side, under u12
    //tmp1075_sensor_5_address, // U6 -> 0b1011000, location: led side, under u11
    //tmp1075_sensor_6_address, // U7 -> 0b1000001, location: led side, under u21
    //tmp1075_sensor_7_address  // U8 -> 0b1010010, location: by nxp
};

TMP1075_Write_Single_Cmd_t config_write =
{
    .POINTER_REG = tmp1075_cfgr_reg,
    .DATA        = 0x00,
};

TMP1075_Read_Single_Cmd_t temp_read =
{
    .POINTER_REG = tmp1075_temp_reg,
};

/******************************************************************
 *                 Private Function Protoypes
 ******************************************************************/
static float TMP1075_Read_Temp_From_Address(uint8_t sensorAddress);
static float TMP1075_Read_Board_Average_Temp(void);
static float TMP1075_Convert_Raw_To_Celsius(uint8_t msb, uint8_t lsb);

/******************************************************************
 *                       Code Space
 ******************************************************************/
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

static float TMP1075_Read_Board_Average_Temp(void)
{
    float tempSum = 0.0f;
    float tempAverage = 0.0f;

    for (uint8_t i = 0u; i < TMP1075_NUM_SENSORS; i++)
    {
        tempSum += TMP1075_Read_Temp_From_Address(tmp1075_sensor_addresses[i]);
    }

    tempAverage = tempSum / TMP1075_NUM_SENSORS;

    return tempAverage;
}

static float TMP1075_Read_Temp_From_Address(uint8_t sensorAddress)
{
    uint8_t masterDataSend[TMP1075_POINTER_SIZE] = {0};
    uint8_t masterDataReceive[TMP1075_TEMP_DATA_SIZE] = {0};
    status_t status;

    TMP1075_Read_Pointer(&temp_read, masterDataSend);

    LPI2C_DRV_MasterSetSlaveAddr(INST_LPI2C0, sensorAddress, false);

    status = LPI2C_DRV_MasterSendDataBlocking(
        INST_LPI2C0,
        masterDataSend,
        TMP1075_POINTER_SIZE,
        false,   // no STOP here
        100u);

    if (status != STATUS_SUCCESS)
    {
        return -999.0f;
    }

    status = LPI2C_DRV_MasterReceiveDataBlocking(
        INST_LPI2C0,
        masterDataReceive,
        TMP1075_TEMP_DATA_SIZE,
        true,    // STOP after read
        100u);

    if (status != STATUS_SUCCESS)
    {
        return -999.0f;
    }

    return TMP1075_Convert_Raw_To_Celsius(masterDataReceive[0], masterDataReceive[1]);
}

float TMP1075_Read_Avg_Temp(void)
{
    float avgTemp = TMP1075_Read_Board_Average_Temp();
    uint8_t fanPwm = 0u;

    if (avgTemp >= 70.0f)
    {
        fanPwm = 100u;
        tempFault = 1u;
        overTempFlag = 1u;
    }
    else if (avgTemp >= 45.0f)
    {
        fanPwm = 100u;
        overTempFlag = 1u;
    }
    else if (avgTemp >= 40.0f)
    {
        fanPwm = 80u;
        overTempFlag = 1u;
    }
    else if (avgTemp >= 35.0f)
    {
        fanPwm = 60u;
        overTempFlag = 1u;
    }
    else if (avgTemp >= 30.0f)
    {
        fanPwm = 40u;
        overTempFlag = 1u;
    }
    else if (avgTemp >= 25.0f)
    {
        fanPwm = 20u;
        overTempFlag = 1u;
    }
    else if ((avgTemp >= 22.0f) && (overTempFlag))
    {
        fanPwm = 20u;
        overTempFlag = 1u;
    }
    else
    {
        fanPwm = 0u;
        overTempFlag = 0u;
    }

    Fan_SetPWM(fanPwm);

    return avgTemp;
}