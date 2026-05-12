/******************************************************************
 * 
 * CAN_Interface.c
 * 
 * By: Reegan Graham
 * 
 * Description:
 ******************************************************************/
/******************************************************************
 *                             Includes
 ******************************************************************/
#include "can_interface.h"
#include "MBI6353Q.h"
#include "MBI6353Q_Interface.h"
#include "Utils.h"
#include "TMP1075.h"
#include "TMP1075_Interface.h"

/******************************************************************
 *                             Defines
 ******************************************************************/
#define LED_ON      0x03FFu
#define LED_OFF     0x0000u
#define NUM_LEDS    42u
#define MIN_CURRENT_MA     4u
#define MAX_CURRENT_MA     100u
#define PWM_MAX_VALUE      0x03FFu
#define PWM_MIN_PERCENT    0u
#define PWM_MAX_PERCENT    100u
#define DRIVER_NUM         0u
#define COMMAND_INDEX      1u
#define DATA_INDEX         2u

/******************************************************************
 *                             Globals
 ******************************************************************/
static const uint8_t ledRegs[NUM_LEDS] =
{
    mbi6353q_bright_reg29, // LED 1
    mbi6353q_bright_reg34, // LED 2
    mbi6353q_bright_reg40, // LED 3
    mbi6353q_bright_reg42, // LED 4
    mbi6353q_bright_reg25, // LED 5
    mbi6353q_bright_reg28, // LED 6
    mbi6353q_bright_reg33, // LED 7
    mbi6353q_bright_reg39, // LED 8
    mbi6353q_bright_reg41, // LED 9
    mbi6353q_bright_reg24, // LED 10
    mbi6353q_bright_reg27, // LED 11
    mbi6353q_bright_reg31, // LED 12
    mbi6353q_bright_reg38, // LED 13
    mbi6353q_bright_reg44, // LED 14
    mbi6353q_bright_reg23, // LED 15
    mbi6353q_bright_reg26, // LED 16
    mbi6353q_bright_reg30, // LED 17
    mbi6353q_bright_reg37, // LED 18
    mbi6353q_bright_reg45, // LED 19
    mbi6353q_bright_reg21, // LED 20
    mbi6353q_bright_reg22, // LED 21
    mbi6353q_bright_reg36, // LED 22
    mbi6353q_bright_reg46, // LED 23
    mbi6353q_bright_reg19, // LED 24
    mbi6353q_bright_reg20, // LED 25
    mbi6353q_bright_reg18, // LED 26
    mbi6353q_bright_reg35, // LED 27
    mbi6353q_bright_reg47, // LED 28
    mbi6353q_bright_reg13, // LED 29
    mbi6353q_bright_reg14, // LED 30
    mbi6353q_bright_reg16, // LED 31
    mbi6353q_bright_reg17, // LED 32
    mbi6353q_bright_reg04, // LED 33
    mbi6353q_bright_reg12, // LED 34
    mbi6353q_bright_reg11, // LED 35
    mbi6353q_bright_reg10, // LED 36
    mbi6353q_bright_reg09, // LED 37
    mbi6353q_bright_reg03, // LED 38
    mbi6353q_bright_reg08, // LED 39
    mbi6353q_bright_reg06, // LED 40
    mbi6353q_bright_reg05, // LED 41
    mbi6353q_bright_reg02  // LED 42
};

static uint8_t first_can_msg = 0u;

/******************************************************************
 *                          Code Space
 ******************************************************************/
/******************************************************************
 * Name: CAN_InitInterface
 * Paramters: rx_msg_id (uint32_t) - CAN message ID
 * Returns: NONE
 * Description: Initializing CAN 
 ******************************************************************/
void CAN_InitInterface(uint32_t rx_msg_id) 
{
    CAN_Init(&can_pal1_instance, &can_pal1_Config0);

    can_buff_config_t buffCfg =  
    {
        .enableFD = false,
        .enableBRS = true,
        .fdPadding = 0U,
        .idType = CAN_MSG_ID_STD,
        .isRemote = false
    };

    CAN_ConfigRxBuff(&can_pal1_instance, RX_MAILBOX, &buffCfg, rx_msg_id);
}

/******************************************************************
 * Name: CAN_ProcessReceivedMessage
 * Paramters: rx_msg_id (uint32_t) - CAN message ID
 * Returns: NONE
 * Description: Processing CAN message 
 ******************************************************************/
void CAN_ProcessReceivedMessage(uint32_t rx_msg_id) 
{
    can_message_t recvMsg;

    CAN_Receive(&can_pal1_instance, RX_MAILBOX, &recvMsg);
    while(CAN_GetTransferStatus(&can_pal1_instance, RX_MAILBOX) == STATUS_BUSY);

    if (recvMsg.id != rx_msg_id) 
    {
        /* Ignore messages not intended for this device */
        return;
    }

    first_can_msg++;

    if (first_can_msg == 1) // if first message set default divide
    {
        MBI6353Q_SetCurrentDivide(1, mbi6353q_default);
        MBI6353Q_SetCurrentDivide(2, mbi6353q_default);
        MBI6353Q_SetCurrentDivide(3, mbi6353q_default);
        MBI6353Q_SetCurrentDivide(4, mbi6353q_default);
    }

    if ((recvMsg.data[COMMAND_INDEX] >= CAN_MESSAGE_1_ON) && (recvMsg.data[COMMAND_INDEX] <= CAN_MESSAGE_42_ON))
    {
        uint8_t led = recvMsg.data[COMMAND_INDEX];
        CAN_SetLedBrightness(recvMsg.data[DRIVER_NUM], led, LED_ON);
        return;
    }
    else if ((recvMsg.data[COMMAND_INDEX] >= CAN_MESSAGE_1_OFF) && (recvMsg.data[COMMAND_INDEX] <= CAN_MESSAGE_42_OFF))
    {
        uint8_t led = recvMsg.data[COMMAND_INDEX] - CAN_MESSAGE_1_OFF + 1u;
        CAN_SetLedBrightness(recvMsg.data[DRIVER_NUM], led, LED_OFF);
        return;
    }

    switch (recvMsg.data[COMMAND_INDEX]) 
    {
        case CAN_MESSAGE_ALL_OFF:
            MBI6353Q_WriteAllBrightness(recvMsg.data[DRIVER_NUM], LED_OFF);
            Send_OE_Vsync(recvMsg.data[DRIVER_NUM]);
            break;
        case CAN_MESSAGE_ALL_ON:
            MBI6353Q_WriteAllBrightness(recvMsg.data[DRIVER_NUM], LED_ON);
            Send_OE_Vsync(recvMsg.data[DRIVER_NUM]);
            break;
        case CAN_MESSAGE_SET_CURRENT:
            MBI6353Q_SetCurrent(recvMsg.data[DRIVER_NUM], CAN_ConvertCurrentToGCG2(recvMsg.data[DRIVER_NUM], recvMsg.data[DATA_INDEX]));
            break;
        case CAN_MESSAGE_SET_PWM:
            MBI6353Q_WriteAllBrightness(recvMsg.data[DRIVER_NUM], CAN_ConvertPWM(recvMsg.data[DATA_INDEX]));
            Send_OE_Vsync(recvMsg.data[DRIVER_NUM]);
            break;
        // case CAN_MESSAGE_INCREASE_BRIGHTNESS_1:
        //     MBI6353Q_StepBrightness(1);
        //     break;
        // case CAN_MESSAGE_INCREASE_BRIGHTNESS_5:
        //     MBI6353Q_StepBrightness(5);
        //     break;
        // case CAN_MESSAGE_INCREASE_BRIGHTNESS_10:
        //     MBI6353Q_StepBrightness(10);
        //     break;
        // case CAN_MESSAGE_INCREASE_BRIGHTNESS_50:
        //     MBI6353Q_StepBrightness(50);
        //     break;
        // case CAN_MESSAGE_INCREASE_BRIGHTNESS_100:
        //     MBI6353Q_StepBrightness(100);
        //     break;
        // case CAN_MESSAGE_DECREASE_BRIGHTNESS_1:
        //     MBI6353Q_StepBrightness(-1);
        //     break;
        // case CAN_MESSAGE_DECREASE_BRIGHTNESS_5:
        //     MBI6353Q_StepBrightness(-5);
        //     break;
        // case CAN_MESSAGE_DECREASE_BRIGHTNESS_10:
        //     MBI6353Q_StepBrightness(-10);
        //     break;
        // case CAN_MESSAGE_DECREASE_BRIGHTNESS_50:
        //     MBI6353Q_StepBrightness(-50);
        //     break;
        // case CAN_MESSAGE_DECREASE_BRIGHTNESS_100:
        //     MBI6353Q_StepBrightness(-100);
        //     break;
		case CAN_MESSAGE_AVG_TEMP:
		    TMP1075_Read_Temp_Micro();
		    break;
		// case CAN_MESSAGE_DRIVER_TEMP:
		//     TMP1075_Read_Temp_Driver();
		//     break;
		// case CAN_MESSAGE_BACK_TEMP:
		//     TMP1075_Read_Temp_Back();
		//     break;
        default:
            break;
    }
}

/******************************************************************
 * Name: CAN_SetLedBrightness
 * Paramters: led (uint8_t) - LED ID
 *            brightness (uint16_t) - brightness level
 * Returns: NONE
 * Description: Set LED brightness 
 ******************************************************************/
void CAN_SetLedBrightness(uint8_t deviceNumber, uint8_t led, uint16_t brightness)
{
    if (led < 1 || led > NUM_LEDS)
    {
        return; /* out of range error */
    }

    MBI6353Q_WriteSingleBrightness(deviceNumber, ledRegs[led - 1], brightness);

    Send_OE_Vsync(deviceNumber);
}

/******************************************************************
 * Name: CAN_ConvertCurrentToGCG2
 * Paramters: current_mA (uint8_t) - current value in mA
 * Returns: current value in hex for the GCG2 register
 * Description: Convert mA to hex for the GCG2 register
 * NOTE: equation found on page 15 of the MBI6353 datasheet
 ******************************************************************/
uint8_t CAN_ConvertCurrentToGCG2(uint8_t deviceNumber, uint8_t current_mA)
{
    float gcg1, gcg2;

    if (current_mA < MIN_CURRENT_MA || current_mA > MAX_CURRENT_MA)
    {
        return 0u; /* current out of range */
    }

    if (current_mA <= 12u)
    {
        gcg1 = 0.125f;
        MBI6353Q_SetCurrentDivide(deviceNumber, mbi6353q_eighth);
    }
    else if (current_mA < 25u)
    {
        gcg1 = 0.25f;
        MBI6353Q_SetCurrentDivide(deviceNumber, mbi6353q_quarter);
    }
    else if (current_mA < 50u)
    {
        gcg1 = 0.5f;
        MBI6353Q_SetCurrentDivide(deviceNumber, mbi6353q_half);
    }
    else
    {
        gcg1 = 1.0f;
        MBI6353Q_SetCurrentDivide(deviceNumber, mbi6353q_default);
    }

    Send_OE_Vsync(deviceNumber);
    gcg2 = ((((float)current_mA / gcg1) - 25.0f) * 255.0f) / 75.0f;

    return (uint8_t)(gcg2 + 0.5f); 
}

/******************************************************************
 * Name: CAN_ConvertPWM
 * Paramters: pwm (uint8_t) - wanted pwm value
 * Returns: pwm value in hex 
 * Description: Convert pwm value to hex
 * Example: [node][SET_PWM][percent]
 ******************************************************************/
uint16_t CAN_ConvertPWM(uint8_t percent)
{
    if (percent > PWM_MAX_PERCENT)
    {
        percent = PWM_MAX_PERCENT;
    }

    return (uint16_t)(((uint32_t)percent * PWM_MAX_VALUE + 50u) / 100u);
}