#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include "MBI6353Q.h"
#include "MBI6353Q_Interface.h"
#include "sdk_project_config.h"
#include "can_interface.h"
#include "Utils.h"
#include "TMP1075.h"
#include "TMP1075_Interface.h"




int main(void) {
	lpi2c_master_state_t lpi2c1MasterState;
    CLOCK_SYS_Init(g_clockManConfigsArr, CLOCK_MANAGER_CONFIG_CNT, g_clockManCallbacksArr, CLOCK_MANAGER_CALLBACK_CNT);
    CLOCK_SYS_UpdateConfiguration(0U, CLOCK_MANAGER_POLICY_AGREEMENT);
    PINS_DRV_Init(NUM_OF_CONFIGURED_PINS0, g_pin_mux_InitConfigArr0);
    LPSPI_DRV_MasterInit(INST_LPSPI_1, &lpspi_1State, &lpspi_0_MasterConfig0);
    LPSPI_DRV_MasterSetDelay(INST_LPSPI_1, 45u, 1u, 1u);
    LPI2C_DRV_MasterInit(INST_LPI2C0, &lpi2c0_MasterConfig0, &lpi2c1MasterState);

    uint32_t rx_msg_id;

    rx_msg_id = ReadDipSwitchState();
    CAN_InitInterface(rx_msg_id);

    // Initialize LED driver and Turn lights off at power-on
    MBI6353Q_SendInitMsgs();
    MBI6353Q_WriteAllBrightness(0x0);
    Send_OE_Vsync();


    while(1) {
        CAN_ProcessReceivedMessage(rx_msg_id);
        Delay(100000);
    }

    return 0;
}
