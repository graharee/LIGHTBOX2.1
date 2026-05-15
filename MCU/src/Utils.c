#include "utils.h"
#include "sdk_project_config.h" // Assuming this header provides the necessary pin configurations
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#define FTM_DUTY_MAX 0x8000U

void Delay(volatile int cycles) {
    while(cycles--);
}

void Send_OE_Vsync(uint8_t deviceNumber)
{
    switch (deviceNumber)
    {
        case 1:
            PINS_DRV_SetPins(VSYNC_PORT, 1u << VSYNC_PIN);
            Delay(17);
            PINS_DRV_ClearPins(OE_PORT, 1u << OE_PIN);
            Delay(17);
            PINS_DRV_ClearPins(VSYNC_PORT, 1u << VSYNC_PIN);
            PINS_DRV_SetPins(OE_PORT, 1u << OE_PIN);
            Delay(17);
            break;

        case 2:
            PINS_DRV_SetPins(PTD, 1u << 0);
            Delay(17);
            PINS_DRV_ClearPins(PTD, 1u << 5);
            Delay(17);
            PINS_DRV_ClearPins(PTD, 1u << 0);
            PINS_DRV_SetPins(PTD, 1u << 5);
            Delay(17);
            break;

        case 3:
            PINS_DRV_SetPins(PTD, 1u << 16);
            Delay(17);
            PINS_DRV_ClearPins(PTC, 1u << 1);
            Delay(17);
            PINS_DRV_ClearPins(PTD, 1u << 16);
            PINS_DRV_SetPins(PTC, 1u << 1);
            Delay(17);
            break;

        case 4:
            PINS_DRV_SetPins(PTE, 1u << 9);
            Delay(17);
            PINS_DRV_ClearPins(PTC, 1u << 16);
            Delay(17);
            PINS_DRV_ClearPins(PTE, 1u << 9);
            PINS_DRV_SetPins(PTC, 1u << 16);
            Delay(17);
            break;

        default:
            break;
    }
}

uint32_t ReadDipSwitchState() {
    uint32_t state = 0;

    // Read each dip switch and set the corresponding bit in state
    if (PINS_DRV_ReadPins(DIP1_PORT) & (1 << DIP1_PIN)) {
        state |= (1 << 0); // Switch 1
    }
    if (PINS_DRV_ReadPins(DIP2_PORT) & (1 << DIP2_PIN)) {
        state |= (1 << 1); // Switch 2
    }
    if (PINS_DRV_ReadPins(DIP3_PORT) & (1 << DIP3_PIN)) { // switch 2
        state |= (1 << 2); // Switch 3
    }
    if (PINS_DRV_ReadPins(DIP4_PORT) & (1 << DIP4_PIN)) {
        state |= (1 << 3); // Switch 4
    }
    if (PINS_DRV_ReadPins(DIP5_PORT) & (1 << DIP5_PIN)) {
        state |= (1 << 4); // Switch 5
    }
    if (PINS_DRV_ReadPins(DIP6_PORT) & (1 << DIP6_PIN)) {
        state |= (1 << 5); // Switch 6
    }
    if (PINS_DRV_ReadPins(DIP7_PORT) & (1 << DIP7_PIN)) {
        state |= (1 << 6); // Switch 7
    }
    if (PINS_DRV_ReadPins(DIP8_PORT) & (1 << DIP8_PIN)) {
        state |= (1 << 7); // Switch 8
    }

    return state;
}

void Fan_SetPWM(uint8_t percent)
{
    if (percent > 100U)
    {
        percent = 100U;
    }

    uint16_t duty = (uint16_t)(((uint32_t)percent * FTM_DUTY_MAX) / 100U);

    FTM_DRV_UpdatePwmChannel(
        INST_FLEXTIMER_PWM_1,
        0U,
        FTM_PWM_UPDATE_IN_DUTY_CYCLE,
        duty,
        0U,
        true
    );
}
