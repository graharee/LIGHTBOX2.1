/*****************************************************************************************************************
 *      Magna International Inc. ("Magna") CONFIDENTIAL
 *      Unpublished Copyright (c) 2019-2020 Magna International Inc., All Rights Reserved.
 *      This file is subject to the terms and conditions defined in file 'license.txt', which is part of this
 *      source code package.
 *****************************************************************************************************************/

/**********************************************************************
 *                              Includes
 **********************************************************************/

#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#include "MBI6353Q.h"
#include "MBI6353Q_Interface.h"
#include "sdk_project_config.h"

/**********************************************************************
 *                        Function Prototypes
 **********************************************************************/
static void MBI6353Q_SelectDriver(uint8_t deviceNumber);
static void MBI6353Q_DeselectDriver(uint8_t deviceNumber);
static void MBI6353Q_AllDriversDeselect(void);

/*****************************************************************************************************************
 *                  Defines
 *****************************************************************************************************************/
#define TIMEOUT 200U
#define BURST_CMD_SIZE 6U
#define SINGLE_CMD_SIZE 4U
#define DATA_SIZE 2U
#define MASK_SIZE 16U
#define CONFIG_SIZE 42U
#define SINGLE_READ_SIZE 12U
#define SINGLE_WRITE_SIZE 10U
#define BRIGHTNESS_SIZE 202U
#define READ_CONFIG_SIZE 44U

#define MAX_BRIGHTNESS 0x03FF
#define MIN_BRIGHTNESS 0x0000

/*****************************************************************************************************************
 *                   Global Variables
 *****************************************************************************************************************/

static const MBI6353Q_Burst_Cmd_t mask_command = {
    .s_device_address_frame = {
        .RESERVED_7_0 = 0,
        .DEVICE_ADDRESS = mbi6353q_write_all,
        .SINGLE_DATA = mbi6353q_burst_data,
        .BROADCAST = mbi6353q_all_device,
    },
    .s_num_data = {
        .DATA = 0x03,
    },
    .s_reg_address_frame = {
        .REG_ADDRESS = mbi6353q_mask1,
        .READ_WRITE = mbi6353q_write,
    }};

static const MBI6353Q_Burst_Cmd_t config_command = {
    .s_device_address_frame = {
        .RESERVED_7_0 = 0,
        .DEVICE_ADDRESS = mbi6353q_write_all,
        .SINGLE_DATA = mbi6353q_burst_data,
        .BROADCAST = mbi6353q_all_device,
    },
    .s_num_data = {
        .DATA = 0x0010,
    },
    .s_reg_address_frame = {
        .REG_ADDRESS = mbi6353q_config1,
        .READ_WRITE = mbi6353q_write,

    }};


static const MBI6353Q_Burst_Cmd_t brightness_command = {
    .s_device_address_frame = {
        .RESERVED_7_0 = 0,
        .DEVICE_ADDRESS = 0x00, // 0111111  questionable device address (63)
        .SINGLE_DATA = mbi6353q_burst_data,
        .BROADCAST = mbi6353q_all_device,
    },
    .s_num_data = {
        .DATA = 0x0030, // 48 brightness codes
    },
    .s_reg_address_frame = {
        .REG_ADDRESS = mbi6353q_bright_reg48,
        .READ_WRITE = mbi6353q_write,
    }};

static const MBI6353Q_Burst_Cmd_t read_config = {
    .s_device_address_frame = {
        .RESERVED_7_0 = 0,
        .DEVICE_ADDRESS = mbi6353q_device_1,
        .SINGLE_DATA = mbi6353q_burst_data,
        .BROADCAST = mbi6353q_single_device,
    },
    .s_num_data = {
        .DATA = 0x0010, // 16 registers
    },
    .s_reg_address_frame = {
        .REG_ADDRESS = mbi6353q_config1,
        .READ_WRITE = mbi6353q_read,
    }};

/*------------------------------CONFIG REGISTERS ---------------------------*/

// Eval default [0F0F]
static const MBI6353Q_Register_t config1 = {
    .s_config1_reg = {
        .THRESHOLD = mbi6353q_pam_mode,      //  1111
        .DISPLAY_MODE = mbi6353q_continuous, //  0
        .NUM_SCAN = mbi6353q_scan1,          //  00
        .RESERVE_7 = 0x00,                   //  0
        .NUM_SCRAMBLE = mbi6353q_scramble32, //  11
        .CURRENT_DIVIDE = mbi6353q_default,  //  11
        .RESERVE_15_12 = 0x00,               //  0000
    }};

// Macro default [0014]
static const MBI6353Q_Register_t config2 = {
    .s_config2_reg = {
        .RESERVED = 0x0014,
    }};

// Macro default [000D]
static const MBI6353Q_Register_t config3 = {
    .s_config3_reg = {
        .RESERVED = 0x000D,
    }};

// Macro default [0606]
static const MBI6353Q_Register_t config4 = {
    .s_config4_reg = {
        .RESERVED = 0x0606,
    }};

// Macro default [003F]
static const MBI6353Q_Register_t config5 = {
    .s_config5_reg = {
        .FALLING = mbi6353q_highSpeedRise,  // 111
        .RISING = mbi6353q_highSpeedFall,   // 111
        .RESERVE_7 = 0x00,                  // 0
        .HLM_ENABLE = mbi6353q_hlm_disable, // 0
        .SET_CURRENT = mbi6353q_25mA        // 00000000
    }};

// Macro Default [0000]
static const MBI6353Q_Register_t config6 = {
    .s_config6_reg = {
        .RESERVED = 0x0000,
    }};

// Macro Default [2440]
static const MBI6353Q_Register_t config7 = {
    .s_config7_reg = {
        .RESERVED = 0x2440,
    }};

// Macro Default [0000]
static const MBI6353Q_Register_t config8 = {
    .s_config8_reg = {
        .RESERVED = 0x0000,
    }};

// Macro Default [7C20]
static const MBI6353Q_Register_t config9 = {
    .s_config9_reg = {
        .SHORT_DETECT_V = mbi6353q_short_detect1,        // [00    [0000] = 0
        .OPEN_DETECT_V = mbi6353q_open_detect1,          // 00]
        .RESERVE_4 = 0x00,                               // [0     [0010] = 2
        .INTERRUPT_PIN = mbi6353q_interrupt_enable,      // 1
        .ERROR_MASK = mbi6353q_mask_disable,             // 0
        .RESERVE_7 = 0x00,                               // 0]
        .FBO_PERIOD = mbi6353q_fbo_update1,              // [00    [1100] = C
        .NUM_ERROR = mbi6353q_error8,                    // 11][1
        .SHORT_DETECT_ENABLE = mbi6353q_short_detect_on, // 1
        .OPEN_DETECT_ENABLE = mbi6353q_open_detect_on,   // 1
        .FBO_ENABLE = mbi6353q_fbo_disable               //  0]         [0111] = 7
    }};

// Macro Default [01CA]
static const MBI6353Q_Register_t config10 = {
    .s_config10_reg = {
        .RESERVED = 0x01CA,
    }};

// Macro Default [00FF]
static const MBI6353Q_Register_t config11 = {
    .s_config11_reg = {
        .RESERVED = 0x00FF,
    }};

// Macro Default [339F]
static const MBI6353Q_Register_t config12 = {
    .s_config12_reg = {
        .RESERVED = 0x339F,
    }};

// Macro Default [8200]
static const MBI6353Q_Register_t config13 = {
    .s_config13_reg = {
        .RESERVED = 0x8200,
    }};

// Macro Default [0000]
static const MBI6353Q_Register_t config14 = {
    .s_config14_reg = {
        .RESERVED = 0x0000,
    }};

// Macro Default [0000]
static const MBI6353Q_Register_t config15 = {
    .s_config15_reg = {
        .RESERVED = 0x0000,
    }};

// Macro Default [003C] // bits 3 4 5 6 = 1
static const MBI6353Q_Register_t config16 = {
    .s_config16_reg = {
        .RESERVE_4_0 = 0x1C,
        .TIMING_RST = mbi6353q_timing_rst_on,
        .RESERVE_8_6 = 0x00,
        .CHIP_SLEEP = mbi6353q_chip_sleep_off,
        .RESERVE_15_10 = 0x00,
    }};





//static const MBI6353Q_Register_t faultStatusInit = {
//    .s_fault_status_reg = {
//        .RESERVED_15_5 = 0x0000,
//        .REG_LOCK = mbi6353q_reg_unlock,
//        .CHECKSUM = mbi6353q_checksum_pass,
//        .SHORT_FAULT = mbi6353q_short_pass,
//        .OPEN_FAULT = mbi6353q_open_pass,
//        .THERMAL_SHUTDOWN = mbi6353q_thermal_ok,
//    }};

/*****************************************************************************************************************
 *                  Code Space
 *****************************************************************************************************************/
void Config1Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig1(&config1, u8p_buffer);
}

void Config2Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig2(&config2, u8p_buffer);
}

void Config3Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig3(&config3, u8p_buffer);
}

void Config4Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig4(&config4, u8p_buffer);
}

void Config5Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig5(&config5, u8p_buffer);
}

void Config6Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig6(&config6, u8p_buffer);
}

void Config7Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig7(&config7, u8p_buffer);
}

void Config8Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig8(&config8, u8p_buffer);
}

void Config9Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig9(&config9, u8p_buffer);
}

void Config10Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig10(&config10, u8p_buffer);
}

void Config11Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig11(&config11, u8p_buffer);
}

void Config12Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig12(&config12, u8p_buffer);
}

void Config13Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig13(&config13, u8p_buffer);
}

void Config14Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig14(&config14, u8p_buffer);
}

void Config15Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig15(&config15, u8p_buffer);
}

void Config16Init(uint8_t *u8p_buffer)
{
    MBI6353Q_WriteConfig16(&config16, u8p_buffer);
}


void MaskCommand(uint8_t *u8p_buffer)
{
    MBI6353Q_CreateBurstCmd(&mask_command, u8p_buffer);
}

void ConfigCommand(uint8_t *u8p_buffer)
{
    MBI6353Q_CreateBurstCmd(&config_command, u8p_buffer);
}

void BrightnessCommand(uint8_t *u8p_buffer)
{
    MBI6353Q_Burst_Cmd_t cmd = brightness_command;

    cmd.s_device_address_frame.DEVICE_ADDRESS = 0x01;
    cmd.s_device_address_frame.BROADCAST = mbi6353q_single_device;

    MBI6353Q_CreateBurstCmd(&cmd, u8p_buffer);
}

// uint8_t MBI6353Q_ReadRegister(MBI6353Q_DEVICE_ADDRESS_t deviceNumber, MBI6353Q_RegAddr_t reg_address)
// {
//     uint8_t sendSingleRead[SINGLE_READ_SIZE] = {0};
//     uint16_t receiveSingleRead[SINGLE_READ_SIZE] = {0};

//     MBI6353Q_Single_Cmd_t read_register = {
//         .s_device_address_frame = {
//             .RESERVED_7_0 = 0,
//             .DEVICE_ADDRESS = deviceNumber,
//             .SINGLE_DATA = mbi6353q_single_data,
//             .BROADCAST = mbi6353q_single_device,
//         },
//         .s_reg_address_frame = {
//             .REG_ADDRESS = reg_address,
//             .READ_WRITE = mbi6353q_read,
//         }};

//     MBI6353Q_CreateSingleCmd(&read_register, sendSingleRead);
//     LPSPI_DRV_MasterTransferBlocking(INST_LPSPI_1, sendSingleRead, receiveSingleRead, SINGLE_READ_SIZE, TIMEOUT);

//     return receiveSingleRead;
// }

void MBI6353Q_WriteSingleBrightness(uint8_t deviceNumber, MBI6353Q_RegAddr_t reg_address, uint16_t brightness)
{
    uint8_t sendSingleWrite[SINGLE_WRITE_SIZE] = {0};
    uint8_t receiveSingleWrite[SINGLE_WRITE_SIZE] = {0};

    MBI6353Q_Single_Cmd_t write_register = {
        .s_device_address_frame = {
            .RESERVED_7_0 = 0,
            .DEVICE_ADDRESS = 0x01,
            .SINGLE_DATA = mbi6353q_single_data,
            .BROADCAST = mbi6353q_single_device,
        },
        .s_reg_address_frame = {
            .REG_ADDRESS = reg_address,
            .READ_WRITE = mbi6353q_write,
        }};

    MBI6353Q_CreateSingleCmd(&write_register, sendSingleWrite);
    memcpy(&sendSingleWrite[4], &brightness, DATA_SIZE);
    MBI6353Q_SelectDriver(deviceNumber);
    LPSPI_DRV_MasterTransferBlocking(INST_LPSPI_1, sendSingleWrite, receiveSingleWrite, SINGLE_WRITE_SIZE, TIMEOUT);
    MBI6353Q_DeselectDriver(deviceNumber);
}

void MBI6353Q_SetCurrent(uint8_t deviceNumber, uint16_t current)
{
    uint8_t sendSingleWrite[SINGLE_WRITE_SIZE] = {0};
    uint8_t receiveSingleWrite[SINGLE_WRITE_SIZE] = {0};

    MBI6353Q_Single_Cmd_t write_register = {
        .s_device_address_frame = {
            .RESERVED_7_0 = 0,
            .DEVICE_ADDRESS = 0x01,
            .SINGLE_DATA = mbi6353q_single_data,
            .BROADCAST = mbi6353q_single_device,
        },
        .s_reg_address_frame = {
            .REG_ADDRESS = mbi6353q_config5,
            .READ_WRITE = mbi6353q_write,
        }};

    MBI6353Q_Register_t setConfig5 = {
        .s_config5_reg = {
            .FALLING = mbi6353q_highSpeedRise,  // 111
            .RISING = mbi6353q_highSpeedFall,   // 111
            .RESERVE_7 = 0x00,                  // 0
            .HLM_ENABLE = mbi6353q_hlm_disable, // 0
            .SET_CURRENT = current        // 00000000
        }};

    MBI6353Q_CreateSingleCmd(&write_register, sendSingleWrite);
    memcpy(&sendSingleWrite[4], &setConfig5.s_config5_reg, DATA_SIZE);
    MBI6353Q_SelectDriver(deviceNumber);
    LPSPI_DRV_MasterTransferBlocking(INST_LPSPI_1, sendSingleWrite, receiveSingleWrite, SINGLE_WRITE_SIZE, TIMEOUT);
    MBI6353Q_DeselectDriver(deviceNumber);
}

void MBI6353Q_SetCurrentDivide(uint8_t deviceNumber, uint8_t currentDivide)
{
    uint8_t sendSingleWrite[SINGLE_WRITE_SIZE] = {0};
    uint8_t receiveSingleWrite[SINGLE_WRITE_SIZE] = {0};

    MBI6353Q_Single_Cmd_t write_register = {
        .s_device_address_frame = {
            .RESERVED_7_0 = 0,
            .DEVICE_ADDRESS = 0x01,
            .SINGLE_DATA = mbi6353q_single_data,
            .BROADCAST = mbi6353q_single_device,
        },
        .s_reg_address_frame = {
            .REG_ADDRESS = mbi6353q_config1,
            .READ_WRITE = mbi6353q_write,
        }};

    MBI6353Q_Register_t setConfig1 = {
        .s_config1_reg = {
            .THRESHOLD = mbi6353q_pam_mode,         //  1111
            .DISPLAY_MODE = mbi6353q_continuous,    //  0
            .NUM_SCAN = mbi6353q_scan1,             //  00
            .RESERVE_7 = 0x0,                       //  0
            .NUM_SCRAMBLE = mbi6353q_scramble32,    //  11
            .CURRENT_DIVIDE = currentDivide,        //  Current divide value to set
            .RESERVE_15_12 = 0x00,                   //  0000
        }};

    MBI6353Q_CreateSingleCmd(&write_register, sendSingleWrite);
    memcpy(&sendSingleWrite[4], &setConfig1.s_config1_reg, DATA_SIZE);
    MBI6353Q_SelectDriver(deviceNumber);
    LPSPI_DRV_MasterTransferBlocking(INST_LPSPI_1, sendSingleWrite, receiveSingleWrite, SINGLE_WRITE_SIZE, TIMEOUT);
    MBI6353Q_DeselectDriver(deviceNumber);
}

void ReadConfigCommand(uint8_t *u8p_buffer)
{
    MBI6353Q_CreateBurstCmd(&read_config, u8p_buffer);
}

void MBI6353Q_ReadConfig()
{
    uint8_t sendReadCommand[READ_CONFIG_SIZE] = {0};
    uint8_t readCommand[BURST_CMD_SIZE] = {0};
    ReadConfigCommand(readCommand);
    memcpy(sendReadCommand, readCommand, BURST_CMD_SIZE);
    LPSPI_DRV_MasterTransferBlocking(INST_LPSPI_1, sendReadCommand, readCommand, READ_CONFIG_SIZE, TIMEOUT);
}

void MBI6353Q_SendInitMsgs(void)
{
    for (uint8_t deviceNumber = 1; deviceNumber <= 4; deviceNumber++)
    {
        uint8_t sendMaskCommand[MASK_SIZE] = {0};
        uint8_t sendConfigCommand[CONFIG_SIZE] = {0};
        uint8_t maskRecieve[MASK_SIZE] = {0};
        uint8_t configReceive[CONFIG_SIZE] = {0};
        uint8_t command1[BURST_CMD_SIZE] = {0};
        uint8_t command2[BURST_CMD_SIZE] = {0};

        uint8_t config1[DATA_SIZE] = {0};
        uint8_t config2[DATA_SIZE] = {0};
        uint8_t config3[DATA_SIZE] = {0};
        uint8_t config4[DATA_SIZE] = {0};
        uint8_t config5[DATA_SIZE] = {0};
        uint8_t config6[DATA_SIZE] = {0};
        uint8_t config7[DATA_SIZE] = {0};
        uint8_t config8[DATA_SIZE] = {0};
        uint8_t config9[DATA_SIZE] = {0};
        uint8_t config10[DATA_SIZE] = {0};
        uint8_t config11[DATA_SIZE] = {0};
        uint8_t config12[DATA_SIZE] = {0};
        uint8_t config13[DATA_SIZE] = {0};
        uint8_t config14[DATA_SIZE] = {0};
        uint8_t config15[DATA_SIZE] = {0};
        uint8_t config16[DATA_SIZE] = {0};

        MaskCommand(command1);
        ConfigCommand(command2);

        Config1Init(config1);
        Config2Init(config2);
        Config3Init(config3);
        Config4Init(config4);
        Config5Init(config5);
        Config6Init(config6);
        Config7Init(config7);
        Config8Init(config8);
        Config9Init(config9);
        Config10Init(config10);
        Config11Init(config11);
        Config12Init(config12);
        Config13Init(config13);
        Config14Init(config14);
        Config15Init(config15);
        Config16Init(config16);

        memcpy(sendMaskCommand, command1, BURST_CMD_SIZE);

        memcpy(sendConfigCommand, command2, BURST_CMD_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE, config1, DATA_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE + DATA_SIZE * 1, config2, DATA_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE + DATA_SIZE * 2, config3, DATA_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE + DATA_SIZE * 3, config4, DATA_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE + DATA_SIZE * 4, config5, DATA_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE + DATA_SIZE * 5, config6, DATA_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE + DATA_SIZE * 6, config7, DATA_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE + DATA_SIZE * 7, config8, DATA_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE + DATA_SIZE * 8, config9, DATA_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE + DATA_SIZE * 9, config10, DATA_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE + DATA_SIZE * 10, config11, DATA_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE + DATA_SIZE * 11, config12, DATA_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE + DATA_SIZE * 12, config13, DATA_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE + DATA_SIZE * 13, config14, DATA_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE + DATA_SIZE * 14, config15, DATA_SIZE);
        memcpy(sendConfigCommand + BURST_CMD_SIZE + DATA_SIZE * 15, config16, DATA_SIZE);

        MBI6353Q_SelectDriver(deviceNumber);

        LPSPI_DRV_MasterTransferBlocking(
            INST_LPSPI_1,
            sendMaskCommand,
            maskRecieve,
            MASK_SIZE,
            TIMEOUT);

        LPSPI_DRV_MasterTransferBlocking(
            INST_LPSPI_1,
            sendConfigCommand,
            configReceive,
            CONFIG_SIZE,
            TIMEOUT);

        MBI6353Q_DeselectDriver(deviceNumber);
    }
}

void MBI6353Q_WriteAllBrightness(uint8_t deviceNumber, uint16_t brightness)
{
    uint8_t sendBrightnessCommand[BRIGHTNESS_SIZE] = {0};
    uint8_t brightnessReceive[BRIGHTNESS_SIZE] = {0};
    uint8_t commandBuffer[BURST_CMD_SIZE] = {0};
    uint8_t brightnessBuffer[DATA_SIZE] = {0};

    // Initialize brightness command
    BrightnessCommand(commandBuffer);

    MBI6353Q_Register_t brightnessReg = {
    .s_brightness_reg = {
        .RESERVED_15_14 = 0x00,
        .HIGH_LUMINANCE = 0X00, // maybe define
        .BCS1 = brightness,         // brightness code
    }};

    MBI6353Q_WriteBrightness(&brightnessReg, brightnessBuffer);

    // Fill sendBrightnessCommand
    memcpy(sendBrightnessCommand, commandBuffer, BURST_CMD_SIZE);
    for (uint8_t i = BURST_CMD_SIZE; i < BRIGHTNESS_SIZE - 4; i += DATA_SIZE)
    {
        memcpy(sendBrightnessCommand + i, brightnessBuffer, DATA_SIZE);
    }

    MBI6353Q_SelectDriver(deviceNumber);
    // Send brightness command
    LPSPI_DRV_MasterTransferBlocking(INST_LPSPI_1, sendBrightnessCommand, brightnessReceive, BRIGHTNESS_SIZE, TIMEOUT);
    MBI6353Q_DeselectDriver(deviceNumber);
}

// void MBI6353Q_StepBrightness(int16_t step) {  // note this function wasn't working properly. check the read values.
//     uint8_t sendBrightnessCommand[BRIGHTNESS_SIZE] = {0};
//     uint8_t brightnessReceive[BRIGHTNESS_SIZE] = {0};
//     uint8_t commandBuffer[BURST_CMD_SIZE] = {0};
//     uint8_t brightnessBuffer[DATA_SIZE] = {0};

//     uint16_t brightness = MBI6353Q_ReadRegister(mbi6353q_bright_reg29); // Read the value of the first register.
//     brightness = (uint16_t)(brightness + step);

//     // Ensure brightness stays within the valid range
//     if (brightness > MAX_BRIGHTNESS) {
//         brightness = MAX_BRIGHTNESS;
//     } else if (brightness < MIN_BRIGHTNESS) {
//         brightness = MIN_BRIGHTNESS;
//     }

//     // Initialize brightness command
//     //BrightnessCommand(commandBuffer);

//     MBI6353Q_Register_t brightnessReg = {
//         .s_brightness_reg = {
//             .RESERVED_15_14 = 0x00,
//             .HIGH_LUMINANCE = 0X00, // maybe define
//             .BCS1 = brightness,         // brightness code
//         }
//     };

//     MBI6353Q_WriteBrightness(&brightnessReg, brightnessBuffer);

//     // Fill sendBrightnessCommand
//     memcpy(sendBrightnessCommand, commandBuffer, BURST_CMD_SIZE);
//     for (uint8_t i = BURST_CMD_SIZE; i < BRIGHTNESS_SIZE - 4; i += DATA_SIZE) {
//         memcpy(sendBrightnessCommand + i, brightness, DATA_SIZE);
//     }

//     // Send brightness command
//     LPSPI_DRV_MasterTransferBlocking(INST_LPSPI_1, sendBrightnessCommand, brightnessReceive, BRIGHTNESS_SIZE, TIMEOUT);
// }

static void MBI6353Q_AllDriversDeselect(void)
{
    PINS_DRV_SetPins(PTB, (1u << 5)); // CS_1 high
    PINS_DRV_SetPins(PTB, (1u << 0)); // CS_2 high
    PINS_DRV_SetPins(PTB, (1u << 1)); // CS_3 high
    PINS_DRV_SetPins(PTE, (1u << 4)); // CS_4 high
}

static void MBI6353Q_SelectDriver(uint8_t deviceNumber)
{
    MBI6353Q_AllDriversDeselect(); // force everyone high first

    switch (deviceNumber)
    {
        case 1:
            PINS_DRV_ClearPins(PTB, (1u << 5));
            break;

        case 2:
            PINS_DRV_ClearPins(PTB, (1u << 0));
            break;

        case 3:
            PINS_DRV_ClearPins(PTB, (1u << 1));
            break;

        case 4:
            PINS_DRV_ClearPins(PTE, (1u << 4));
            break;

        default:
            break;
    }
}

static void MBI6353Q_DeselectDriver(uint8_t deviceNumber)
{
    (void)deviceNumber;
    MBI6353Q_AllDriversDeselect();
}


