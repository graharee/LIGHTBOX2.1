#include "can_interface.h"
#include "MBI6353Q.h"
#include "MBI6353Q_Interface.h"
#include "Utils.h"
#include "TMP1075.h"
#include "TMP1075_Interface.h"



void CAN_InitInterface(uint32_t rx_msg_id) {
    CAN_Init(&can_pal1_instance, &can_pal1_Config0);

    can_buff_config_t buffCfg =  {
        .enableFD = false,
        .enableBRS = true,
        .fdPadding = 0U,
        .idType = CAN_MSG_ID_STD,
        .isRemote = false
    };

    CAN_ConfigRxBuff(&can_pal1_instance, RX_MAILBOX, &buffCfg, rx_msg_id);
}

void CAN_ProcessReceivedMessage(uint32_t rx_msg_id) {
    can_message_t recvMsg;

    CAN_Receive(&can_pal1_instance, RX_MAILBOX, &recvMsg);
    while(CAN_GetTransferStatus(&can_pal1_instance, RX_MAILBOX) == STATUS_BUSY);

    if (recvMsg.id != rx_msg_id) {
        // Ignore messages not intended for this device
        return;
    }


    switch (recvMsg.data[0]) {
            case CAN_MESSAGE_ALL_OFF:
                MBI6353Q_WriteAllBrightness(0x0000);
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_ALL_ON:
                MBI6353Q_WriteAllBrightness(0x03FF);
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_1_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg29, 0x03FF); //1
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_1_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg29, 0x0000); //1
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_2_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg34, 0x03FF); //2
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_2_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg34, 0x0000); //2
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_3_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg40, 0x03FF); //3
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_3_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg40, 0x0000); //3
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_4_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg42, 0x03FF); //4
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_4_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg42, 0x0000); //4
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_5_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg25, 0x03FF); //5
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_5_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg25, 0x0000); //5
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_6_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg28, 0x03FF); //6
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_6_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg28, 0x0000); //6
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_7_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg33, 0x03FF); //7
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_7_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg33, 0x0000); //7
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_8_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg39, 0x03FF); //8
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_8_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg39, 0x0000); //8
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_9_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg41, 0x03FF); //9
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_9_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg41, 0x0000); //9
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_10_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg24, 0x03FF); //10
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_10_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg24, 0x0000); //10
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_11_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg27, 0x03FF); //11
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_11_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg27, 0x0000); //11
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_12_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg31, 0x03FF); //12
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_12_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg31, 0x0000); //12
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_13_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg38, 0x03FF); //13
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_13_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg38, 0x0000); //13
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_14_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg44, 0x03FF); //14
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_14_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg44, 0x0000); //14
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_15_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg23, 0x03FF); //15
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_15_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg23, 0x0000); //15
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_16_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg26, 0x03FF); //16
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_16_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg26, 0x0000); //16
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_17_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg30, 0x03FF); //17
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_17_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg30, 0x0000); //17
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_18_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg37, 0x03FF); //18
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_18_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg37, 0x0000); //18
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_19_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg45, 0x03FF); //19
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_19_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg45, 0x0000); //19
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_20_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg21, 0x03FF); //20
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_20_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg21, 0x0000); //20
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_21_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg22, 0x03FF); //21
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_21_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg22, 0x0000); //21
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_22_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg36, 0x03FF); //22
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_22_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg36, 0x0000); //22
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_23_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg46, 0x03FF); //23
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_23_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg46, 0x0000); //23
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_24_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg19, 0x03FF); //24
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_24_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg19, 0x0000); //24
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_25_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg20, 0x03FF); //25
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_25_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg20, 0x0000); //25
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_26_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg18, 0x03FF); //26
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_26_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg18, 0x0000); //26
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_27_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg35, 0x03FF); //27
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_27_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg35, 0x0000); //27
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_28_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg47, 0x03FF); //28
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_28_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg47, 0x0000); //28
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_29_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg13, 0x03FF); //29
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_29_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg13, 0x0000); //29
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_30_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg14, 0x03FF); //30
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_30_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg14, 0x0000); //30
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_31_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg16, 0x03FF); //31
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_31_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg16, 0x0000); //31
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_32_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg17, 0x03FF); //32
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_32_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg17, 0x0000); //32
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_33_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg04, 0x03FF); //33
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_33_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg04, 0x0000); //33
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_34_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg12, 0x03FF); //34
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_34_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg12, 0x0000); //34
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_35_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg11, 0x03FF); //35
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_35_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg11, 0x0000); //35
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_36_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg10, 0x03FF); //36
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_36_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg10, 0x0000); //36
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_37_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg09, 0x03FF); //37
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_37_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg09, 0x0000); //37
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_38_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg03, 0x03FF); //38
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_38_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg03, 0x0000); //38
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_39_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg08, 0x03FF); //39
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_39_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg08, 0x0000); //39
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_40_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg06, 0x03FF); //40
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_40_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg06, 0x0000); //40
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_41_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg05, 0x03FF); //41
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_41_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg05, 0x0000); //41
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_42_ON:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg02, 0x03FF); //42
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_42_OFF:
                MBI6353Q_WriteSingleBrightness(mbi6353q_bright_reg02, 0x0000); //42
                Send_OE_Vsync();
                break;
            case CAN_MESSAGE_25mA:
				  MBI6353Q_SetCurrent(mbi6353q_25mA);
				  break;
			case CAN_MESSAGE_31mA:
				  MBI6353Q_SetCurrent(mbi6353q_31mA);
				  break;
			case CAN_MESSAGE_35mA:
				  MBI6353Q_SetCurrent(mbi6353q_35mA);
				  break;
			case CAN_MESSAGE_41mA:
				  MBI6353Q_SetCurrent(mbi6353q_41mA);
				  break;
			case CAN_MESSAGE_45mA:
				  MBI6353Q_SetCurrent(mbi6353q_45mA);
				  break;
			case CAN_MESSAGE_51mA:
				  MBI6353Q_SetCurrent(mbi6353q_51mA);
				  break;
			case CAN_MESSAGE_55mA:
				  MBI6353Q_SetCurrent(mbi6353q_55mA);
				  break;
			case CAN_MESSAGE_61mA:
				  MBI6353Q_SetCurrent(mbi6353q_61mA);
				  break;
			case CAN_MESSAGE_65mA:
				  MBI6353Q_SetCurrent(mbi6353q_65mA);
				  break;
            case CAN_MESSAGE_70mA: // added here 4/23/2026
				  MBI6353Q_SetCurrent(mbi6353q_70mA);
				  break;
			case CAN_MESSAGE_71mA:
				  MBI6353Q_SetCurrent(mbi6353q_71mA);
				  break;
			case CAN_MESSAGE_75mA:
				  MBI6353Q_SetCurrent(mbi6353q_75mA);
				  break;
			case CAN_MESSAGE_81mA:
				  MBI6353Q_SetCurrent(mbi6353q_81mA);
				  break;
			case CAN_MESSAGE_85mA:
				  MBI6353Q_SetCurrent(mbi6353q_85mA);
				  break;
			case CAN_MESSAGE_95mA:
				  MBI6353Q_SetCurrent(mbi6353q_95mA);
				  break;
			case CAN_MESSAGE_100mA:
				  MBI6353Q_SetCurrent(mbi6353q_100mA);
				  break;
            case CAN_MESSAGE_DIV_EIGHTH:
                MBI6353Q_SetCurrentDivide(mbi6353q_eighth);
                break;
            case CAN_MESSAGE_DIV_HALF:
                MBI6353Q_SetCurrentDivide(mbi6353q_half);
                break;
            case CAN_MESSAGE_DIV_QUARTER:
                MBI6353Q_SetCurrentDivide(mbi6353q_quarter);
                break;
            case CAN_MESSAGE_DIV_DEFAULT:
                MBI6353Q_SetCurrentDivide(mbi6353q_default);
                break;
            case CAN_MESSAGE_INCREASE_BRIGHTNESS_1:
                MBI6353Q_StepBrightness(1);
                break;
            case CAN_MESSAGE_INCREASE_BRIGHTNESS_5:
                MBI6353Q_StepBrightness(5);
                break;
            case CAN_MESSAGE_INCREASE_BRIGHTNESS_10:
                MBI6353Q_StepBrightness(10);
                break;
            case CAN_MESSAGE_INCREASE_BRIGHTNESS_50:
                MBI6353Q_StepBrightness(50);
                break;
            case CAN_MESSAGE_INCREASE_BRIGHTNESS_100:
                MBI6353Q_StepBrightness(100);
                break;
            case CAN_MESSAGE_DECREASE_BRIGHTNESS_1:
                MBI6353Q_StepBrightness(-1);
                break;
            case CAN_MESSAGE_DECREASE_BRIGHTNESS_5:
                MBI6353Q_StepBrightness(-5);
                break;
            case CAN_MESSAGE_DECREASE_BRIGHTNESS_10:
                MBI6353Q_StepBrightness(-10);
                break;
            case CAN_MESSAGE_DECREASE_BRIGHTNESS_50:
                MBI6353Q_StepBrightness(-50);
                break;
            case CAN_MESSAGE_DECREASE_BRIGHTNESS_100:
                MBI6353Q_StepBrightness(-100);
                break;
            case CAN_MESSAGE_PWM_LOW:
     			MBI6353Q_WriteAllBrightness(0x0009); // 1/8 of 0x03FF
     			Send_OE_Vsync();
     			break;
            case CAN_MESSAGE_PWM_88:
			   MBI6353Q_WriteAllBrightness(0x0069); // 1/8 of 0x03FF
			   Send_OE_Vsync();
			   break;
		   case CAN_MESSAGE_PWM_105:
			   MBI6353Q_WriteAllBrightness(0x0064); // 1/4 of 0x03FF
			   Send_OE_Vsync();
			   break;
		   case CAN_MESSAGE_PWM_148:
			   MBI6353Q_WriteAllBrightness(0x0063); // 1/2 of 0x03FF
			   Send_OE_Vsync();
			   break;
		   case CAN_MESSAGE_PWM_288:
			   MBI6353Q_WriteAllBrightness(0x006B); // 3/4 of 0x03FF
			   Send_OE_Vsync();
			   break;
		   case CAN_MESSAGE_MICRO_TEMP:
			   TMP1075_Read_Temp_Micro();
			   break;
		   case CAN_MESSAGE_DRIVER_TEMP:
			   TMP1075_Read_Temp_Driver();
			   break;
		   case CAN_MESSAGE_BACK_TEMP:
			   TMP1075_Read_Temp_Back();
			   break;


            default:
                break;
        }
    }
