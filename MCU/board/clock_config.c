/**
* @page misra_violations MISRA-C:2012 violations
*
* @section [global]
* Violates MISRA 2012 Required Rule 9.4, Duplicate initialization of object element.
* It's the only way to initialize an array that is member of struct.
*
* @section [global]
* Violates MISRA 2012 Advisory Rule 8.7, External variable could be made static.
* The external variables will be used in other source files in application code.
*/

/* TEXT BELOW IS USED AS SETTING FOR TOOLS *************************************
!!GlobalInfo
product: Clocks v13.0
processor: S32K116
package_id: S32K116_LQFP48
mcu_data: s32sdk_s32k1xx_rtm_401
processor_version: 0.0.0
 * BE CAREFUL MODIFYING THIS COMMENT - IT IS YAML SETTINGS FOR TOOLS **********/

#include "clock_config.h"

/*******************************************************************************
 * Definitions
 ******************************************************************************/

/*******************************************************************************
 * Variables
 ******************************************************************************/

/* TEXT BELOW IS USED AS SETTING FOR TOOLS *************************************
!!Configuration
name: BOARD_BootClockRUN
called_from_default_init: true
outputs:
- {id: ADC0_CLK.outFreq, value: 8 MHz}
- {id: BUS_CLK.outFreq, value: 48 MHz}
- {id: CLKOUT.outFreq, value: 48 MHz}
- {id: CMP0_CLK.outFreq, value: 48 MHz}
- {id: CORE_CLK.outFreq, value: 48 MHz}
- {id: CRC0_CLK.outFreq, value: 48 MHz}
- {id: DMA0_CLK.outFreq, value: 48 MHz}
- {id: DMAMUX0_CLK.outFreq, value: 48 MHz}
- {id: EIM0_CLK.outFreq, value: 48 MHz}
- {id: ERM0_CLK.outFreq, value: 48 MHz}
- {id: FIRCDIV1_CLK.outFreq, value: 48 MHz}
- {id: FIRCDIV2_CLK.outFreq, value: 48 MHz}
- {id: FLASH_CLK.outFreq, value: 24 MHz}
- {id: FLEXCAN0_CLK.outFreq, value: 48 MHz}
- {id: FTFC0_CLK.outFreq, value: 24 MHz}
- {id: FTM0_CLK.outFreq, value: 8 MHz}
- {id: FTM1_CLK.outFreq, value: 8 MHz}
- {id: FlexIO0_CLK.outFreq, value: 8 MHz}
- {id: LPI2C0_CLK.outFreq, value: 8 MHz}
- {id: LPIT0_CLK.outFreq, value: 8 MHz}
- {id: LPSPI0_CLK.outFreq, value: 8 MHz}
- {id: LPTMR0_CLK.outFreq, value: 8 MHz}
- {id: LPUART0_CLK.outFreq, value: 8 MHz}
- {id: LPUART1_CLK.outFreq, value: 8 MHz}
- {id: MPU0_CLK.outFreq, value: 48 MHz}
- {id: MSCM0_CLK.outFreq, value: 48 MHz}
- {id: PDB0_CLK.outFreq, value: 48 MHz}
- {id: PORTA_CLK.outFreq, value: 48 MHz}
- {id: PORTB_CLK.outFreq, value: 48 MHz}
- {id: PORTC_CLK.outFreq, value: 48 MHz}
- {id: PORTD_CLK.outFreq, value: 48 MHz}
- {id: PORTE_CLK.outFreq, value: 48 MHz}
- {id: RTC0_CLK.outFreq, value: 48 MHz}
- {id: SCGCLKOUT.outFreq, value: 48 MHz}
- {id: SIRCDIV1_CLK.outFreq, value: 8 MHz}
- {id: SIRCDIV2_CLK.outFreq, value: 8 MHz}
- {id: SYS_CLK.outFreq, value: 48 MHz}
- {id: TRACE_CLK.outFreq, value: 48 MHz}
sources:
- {id: PMC.LPO.outFreq, value: 128 kHz}
- {id: RTC.RTC_CLK_EXT_IN.outFreq, value: 32.768 kHz}
- {id: SCG.SOSC.outFreq, value: 8 MHz}
 * BE CAREFUL MODIFYING THIS COMMENT - IT IS YAML SETTINGS FOR TOOLS **********/

/* *************************************************************************
* Configuration structure for peripheral clock configuration 0
* ************************************************************************* */
/*! @brief peripheral clock configuration 0 */
peripheral_clock_config_t peripheralClockConfig0[NUM_OF_PERIPHERAL_CLOCKS_0] = {
    {
        .clockName = ADC0_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_SIRC_DIV2,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = LPSPI0_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_SIRC_DIV2,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = LPUART0_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_SIRC_DIV2,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = LPUART1_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_SIRC_DIV2,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = LPI2C0_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_SIRC_DIV2,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = LPIT0_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_SIRC_DIV2,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = LPTMR0_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_SIRC_DIV2,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = FTM0_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_SIRC_DIV1,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = FTM1_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_SIRC_DIV1,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = FLEXIO0_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_SIRC_DIV2,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = CMP0_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_OFF,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = CRC0_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_OFF,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = DMAMUX0_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_OFF,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = FTFC0_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_OFF,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = PDB0_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_OFF,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = RTC0_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_OFF,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = FlexCAN0_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_OFF,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = PORTA_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_OFF,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = PORTB_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_OFF,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = PORTC_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_OFF,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = PORTD_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_OFF,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
    {
        .clockName = PORTE_CLK,
        .clkGate = true,
        .clkSrc = CLK_SRC_OFF,
        .frac = MULTIPLY_BY_ONE,
        .divider = DIVIDE_BY_ONE,
    },
};
/* *************************************************************************
* Configuration structure for Clock Configuration 0
* ************************************************************************* */
/*! @brief User Configuration structure clock_managerCfg_0 */
clock_manager_user_config_t clockMan1_InitConfig0 = {
    .scgConfig = 
    {
        .sircConfig = 
        {
            .initialize = true,
            .enableInStop = true,                 /* Enable SIRC in stop mode */
            .enableInLowPower = true,             /* Enable SIRC in low power mode */
            .locked = false,                      /* unlocked */
            .range = SCG_SIRC_RANGE_HIGH,         /* Slow IRC high range clock (8 MHz) */
            .div1 = SCG_ASYNC_CLOCK_DIV_BY_1,     /* Slow IRC Clock Divider 1: divided by 1 */
            .div2 = SCG_ASYNC_CLOCK_DIV_BY_1,     /* Slow IRC Clock Divider 3: divided by 1 */
        },
        .fircConfig = 
        {
            .initialize = true,
            .regulator = true,                    /* FIRC regulator is enabled */
            .locked = false,                      /* unlocked */
            .range = SCG_FIRC_RANGE_48M,           /*!< RANGE      */
            .div1 = SCG_ASYNC_CLOCK_DIV_BY_1,     /* Fast IRC Clock Divider 1: divided by 1 */
            .div2 = SCG_ASYNC_CLOCK_DIV_BY_1,     /* Fast IRC Clock Divider 3: divided by 1 */
        },
        .rtcConfig = 
        {
            .initialize = false,
        },
        .soscConfig = 
        {
            .initialize = false,
        },
        .clockOutConfig = 
        {
            .initialize = true,
            .source = SCG_CLOCKOUT_SRC_FIRC,      /* Fast IRC. */
        },
        .clockModeConfig = 
        {
            .initialize = true,
            .rccrConfig = 
            {
                .src = SCG_SYSTEM_CLOCK_SRC_FIRC, /* Fast IRC */
                .divCore = SCG_SYSTEM_CLOCK_DIV_BY_1,/* Core Clock Divider: divided by 1 */
                .divBus = SCG_SYSTEM_CLOCK_DIV_BY_1,/* Bus Clock Divider: divided by 1 */
                .divSlow = SCG_SYSTEM_CLOCK_DIV_BY_2,/* Slow Clock Divider: divided by 2 */
            },
            .vccrConfig = 
            {
                .src = SCG_SYSTEM_CLOCK_SRC_SIRC, /* Slow IRC */
                .divCore = SCG_SYSTEM_CLOCK_DIV_BY_2,/* Core Clock Divider: divided by 2 */
                .divBus = SCG_SYSTEM_CLOCK_DIV_BY_1,/* Bus Clock Divider: divided by 1 */
                .divSlow = SCG_SYSTEM_CLOCK_DIV_BY_4,/* Slow Clock Divider: divided by 4 */
            },
        },
    },
    .pccConfig = 
    {
        .peripheralClocks = peripheralClockConfig0, /*!< Peripheral clock control configurations  */
        .count = NUM_OF_PERIPHERAL_CLOCKS_0, /*!< Number of the peripheral clock control configurations  */
    },
    .simConfig = 
    {
        .clockOutConfig = 
        {
            .initialize = true, /*!< Initialize    */
            .enable = true,                       /* enabled */
            .source = SIM_CLKOUT_SEL_SYSTEM_SCG_CLKOUT,/* SCG CLKOUT clock select: SCG slow clock */
            .divider = SIM_CLKOUT_DIV_BY_1,       /* Divided by 1 */
        },
        .lpoClockConfig = 
        {
            .initialize = true, /*!< Initialize    */
            .enableLpo1k = true, /*!< LPO1KCLKEN    */
            .enableLpo32k = true, /*!< LPO32KCLKEN   */
            .sourceLpoClk = SIM_LPO_CLK_SEL_LPO_128K,/* 128 kHz LPO clock */
            .sourceRtcClk = SIM_RTCCLK_SEL_SOSCDIV1_CLK,/* SOSCDIV1 clock */
        },
        .platGateConfig = 
        {
            .initialize = true, /*!< Initialize    */
            .enableEim = true, /*!< CGCEIM        */
            .enableErm = true, /*!< CGCERM        */
            .enableDma = true, /*!< CGCDMA        */
            .enableMpu = true, /*!< CGCMPU        */
            .enableMscm = true, /*!< CGCMSCM       */
        },
        .tclkConfig = 
        {
            .initialize = false, /*!< Initialize    */
        },
        .traceClockConfig = 
        {
            .initialize = true, /*!< Initialize    */
            .divEnable = true, /*!< TRACEDIVEN    */
            .source = CLOCK_TRACE_SRC_CORE_CLK, /*!< TRACECLK_SEL  */
            .divider = 0U, /*!< TRACEDIV      */
            .divFraction = false, /*!< TRACEFRAC     */
        },
    },
    .pmcConfig = 
    {
        .lpoClockConfig = 
        {
         .initialize = false,  /*!< Initialize    */
        },
    },
};

/*! @brief Array of pointers to User configuration structures */
clock_manager_user_config_t const * g_clockManConfigsArr[] = {
&clockMan1_InitConfig0
};

/*! @brief Array of pointers to User defined Callbacks configuration structures */
/* The tool do not support generate Callbacks configuration. It's always empty. */
clock_manager_callback_user_config_t * g_clockManCallbacksArr[] = {(void*)0};


