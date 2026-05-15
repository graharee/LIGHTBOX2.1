#ifndef CAN_INTERFACE_H
#define CAN_INTERFACE_H

#include <stdint.h>
#include <stdbool.h>
#include "sdk_project_config.h"

#define CAN_MESSAGE_ALL_ON  (255UL) // 0xFF
#define CAN_MESSAGE_ALL_OFF (0UL)   // 0x00

#define CAN_MESSAGE_1_ON  (1UL)  // 0x01
#define CAN_MESSAGE_42_ON (42UL) // 0x2A

#define CAN_MESSAGE_1_OFF  (43UL) // 0x2B
#define CAN_MESSAGE_42_OFF (84UL) // 0x54

#define CAN_MESSAGE_SET_CURRENT  (85UL)  // 0x55 
#define CAN_MESSAGE_SET_PWM      (86UL)  // 0x56 
#define CAN_MESSAGE_AVG_TEMP     (120UL) // 0x78

#define TX_MAILBOX  (2UL)
#define TX_MSG_ID   (1UL)
#define RX_MAILBOX  (0UL)
#define RX_MSG_ID   (2UL)

void CAN_InitInterface(uint32_t rx_msg_id);
void CAN_ProcessReceivedMessage(uint32_t rx_msg_id);
void CAN_SetLedBrightness(uint8_t deviceNumber, uint8_t led, uint16_t brightness);
uint8_t CAN_ConvertCurrentToGCG2(uint8_t deviceNumber, uint8_t current_mA);
uint16_t CAN_ConvertPWM(uint8_t percent);
void CAN_Send_Avg_Temp(void);
void CAN_ReportFaults(void);

#endif // CAN_INTERFACE_H
