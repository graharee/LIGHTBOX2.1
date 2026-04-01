#ifndef _PIN_MUX_H_
#define _PIN_MUX_H_

#include "pins_driver.h"

/***********************************************************************************************************************
 * Definitions
 **********************************************************************************************************************/

/*!
 * @addtogroup pin_mux
 * @{
 */

/***********************************************************************************************************************
 * API
 **********************************************************************************************************************/

#if defined(__cplusplus)
extern "C" {
#endif


/*! @brief Definitions/Declarations for BOARD_InitPins Functional Group */
/*! @brief User definition pins */
#define VSYNC_PORT    PTD
#define VSYNC_PIN     1U
#define OE_PORT    PTE
#define OE_PIN     8U
#define CAN_RX_PORT    PTC
#define CAN_RX_PIN     2U
#define CAN_TX_PORT    PTC
#define CAN_TX_PIN     3U
#define DIP3_PORT    PTD
#define DIP3_PIN     3U
#define DIP2_PORT    PTD
#define DIP2_PIN     2U
#define DIP5_PORT    PTC
#define DIP5_PIN     7U
#define DIP4_PORT    PTC
#define DIP4_PIN     6U
#define DIP8_PORT    PTA
#define DIP8_PIN     13U
#define DIP7_PORT    PTA
#define DIP7_PIN     12U
#define DIP6_PORT    PTA
#define DIP6_PIN     11U
#define DIP1_PORT    PTE
#define DIP1_PIN     5U
/*! @brief User number of configured pins */
#define NUM_OF_CONFIGURED_PINS0 16
/*! @brief User configuration structure */
extern pin_settings_config_t g_pin_mux_InitConfigArr0[NUM_OF_CONFIGURED_PINS0];


#if defined(__cplusplus)
}
#endif

/*!
 * @}
 */
#endif /* _PIN_MUX_H_ */

/***********************************************************************************************************************
 * EOF
 **********************************************************************************************************************/

