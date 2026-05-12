/*****************************************************************************************************************
 *      Magna International Inc. ("Magna") CONFIDENTIAL
 *      Unpublished Copyright (c) 2019-2024 Magna International Inc., All Rights Reserved.
 *      This file is subject to the terms and conditions defined in file 'license.txt', which is part of this
 *      source code package.
 *****************************************************************************************************************/
#ifndef MBI6353Q_H
#define MBI6353Q_H

/**********************************************************************
 *                              Includes
 **********************************************************************/
#include <stdint.h>
#include <string.h>

/**********************************************************************
 *                         Global Variables
 **********************************************************************/
typedef enum
{
    mbi6353q_config1 = 0x00u,
    mbi6353q_config2 = 0x01u,
    mbi6353q_config3 = 0x02u,
    mbi6353q_config4 = 0x03u,
    mbi6353q_config5 = 0x04u,
    mbi6353q_config6 = 0x05u,
    mbi6353q_config7 = 0x06u,
    mbi6353q_config8 = 0x07u,
    mbi6353q_config9 = 0x08u,
    mbi6353q_config10 = 0x90u,
    mbi6353q_config11 = 0x0Au,
    mbi6353q_config12 = 0x0Bu,
    mbi6353q_config13 = 0x0Cu,
    mbi6353q_config14 = 0x0Du,
    mbi6353q_config15 = 0x0Eu,
    mbi6353q_config16 = 0x0Fu,
    mbi6353q_bright_reg48 = 0x20u,
    mbi6353q_bright_reg47 = 0x21u,
    mbi6353q_bright_reg46 = 0x22u,
    mbi6353q_bright_reg45 = 0x23u,
    mbi6353q_bright_reg44 = 0x24u,
    mbi6353q_bright_reg43 = 0x25u,
    mbi6353q_bright_reg42 = 0x26u,
    mbi6353q_bright_reg41 = 0x27u,
    mbi6353q_bright_reg40 = 0x28u,
    mbi6353q_bright_reg39 = 0x29u,
    mbi6353q_bright_reg38 = 0x2Au,
    mbi6353q_bright_reg37 = 0x2Bu,
    mbi6353q_bright_reg36 = 0x2Cu,
    mbi6353q_bright_reg35 = 0x2Du,
    mbi6353q_bright_reg34 = 0x2Eu,
    mbi6353q_bright_reg33 = 0x2Fu,
    mbi6353q_bright_reg32 = 0x30u,
    mbi6353q_bright_reg31 = 0x31u,
    mbi6353q_bright_reg30 = 0x32u,
    mbi6353q_bright_reg29 = 0x33u,
    mbi6353q_bright_reg28 = 0x34u,
    mbi6353q_bright_reg27 = 0x35u,
    mbi6353q_bright_reg26 = 0x36u,
    mbi6353q_bright_reg25 = 0x37u,
    mbi6353q_bright_reg24 = 0x38u,
    mbi6353q_bright_reg23 = 0x39u,
    mbi6353q_bright_reg22 = 0x3Au,
    mbi6353q_bright_reg21 = 0x3Bu,
    mbi6353q_bright_reg20 = 0x3Cu,
    mbi6353q_bright_reg19 = 0x3Du,
    mbi6353q_bright_reg18 = 0x3Eu,
    mbi6353q_bright_reg17 = 0x3Fu,
    mbi6353q_bright_reg16 = 0x40u,
    mbi6353q_bright_reg15 = 0x41u,
    mbi6353q_bright_reg14 = 0x42u,
    mbi6353q_bright_reg13 = 0x43u,
    mbi6353q_bright_reg12 = 0x44u,
    mbi6353q_bright_reg11 = 0x45u,
    mbi6353q_bright_reg10 = 0x46u,
    mbi6353q_bright_reg09 = 0x47u,
    mbi6353q_bright_reg08 = 0x48u,
    mbi6353q_bright_reg07 = 0x49u,
    mbi6353q_bright_reg06 = 0x4Au,
    mbi6353q_bright_reg05 = 0x4Bu,
    mbi6353q_bright_reg04 = 0x4Cu,
    mbi6353q_bright_reg03 = 0x4Du,
    mbi6353q_bright_reg02 = 0x4Eu,
    mbi6353q_bright_reg01 = 0x4Fu,
    mbi6353q_SCAN2_reg48 = 0x50u,
    mbi6353q_SCAN3_reg48 = 0x80u,
    mbi6353q_SCAN4_reg48 = 0xB0u,
    mbi6353q_fault_reg = 0x3FEu,
    mbi6353q_mask1 = 0x401u,
    mbi6353q_mask2 = 0x402u,
    mbi6353q_mask3 = 0x403u,
    mbi6353q_lock = 0xB00u,
    mbi6353q_open_error = 0xD00u,
    mbi6353q_short_error = 0xD01u,
    mbi6353q_result_mask0 = 0xD03u,
    mbi6353q_result_mask1 = 0xD04u,
    mbi6353q_result_mask2 = 0xD05u,
} MBI6353Q_RegAddr_t;

/*--------------------------------config 1 reg-------------------------------*/

typedef enum
{
    mbi6353q_eighth = 0x0u,
    mbi6353q_quarter = 0x1u,
    mbi6353q_half = 0x2u,
    mbi6353q_default = 0x3u,
} MBI6353Q_GCG1_DIVISION_t;

typedef enum
{
    mbi6353q_scramble1 = 0x00u,
    mbi6353q_scramble8 = 0x01u,
    mbi6353q_scramble16 = 0x02u,
    mbi6353q_scramble32 = 0x03u,
} MBI6353Q_NUM_SCRAMBLE_t;

typedef enum
{
    mbi6353q_scan1 = 0x00u,
    mbi6353q_scan2 = 0x01u,
    mbi6353q_scan3 = 0x02u,
    mbi6353q_scan4 = 0x03u,
} MBI6353Q_NUM_SCAN_t;

typedef enum
{
    mbi6353q_continuous = 0x00u,
    mbi6353q_one_shot = 0x01u,
} MBI6353Q_DISPLAY_MODE_t;

typedef enum
{
    mbi6353q_pwm_only = 0x00u,
    mbi6353q_thresh4 = 0x02u,
    mbi6353q_thresh8 = 0x03u,
    mbi6353q_thresh16 = 0x04u,
    mbi6353q_thresh32 = 0x05u,
    mbi6353q_thresh64 = 0x06u,
    mbi6353q_thresh128 = 0x07u,
    mbi6353q_thresh256 = 0x08u,
    mbi6353q_thresh512 = 0x09u,
    mbi6353q_thresh1024 = 0x0Au,
    mbi6353q_pam_mode = 0x0Fu,
} MBI6353Q_THRESH_t;

typedef struct
{
    uint16_t THRESHOLD : 4;
    uint16_t DISPLAY_MODE : 1;
    uint16_t NUM_SCAN : 2;
    uint16_t RESERVE_7 : 1;
    uint16_t NUM_SCRAMBLE : 2;
    uint16_t CURRENT_DIVIDE : 2;
    uint16_t RESERVE_15_12 : 4;
} MBI6353Q_CONFIG1_REG_t;

/*--------------------------config 2-4 reg---------------------------- */
typedef struct
{
    uint16_t RESERVED : 16;
} MBI6353Q_CONFIG2_REG_t;

typedef struct
{
    uint16_t RESERVED : 16;
} MBI6353Q_CONFIG3_REG_t;

typedef struct
{
    uint16_t RESERVED : 16;
} MBI6353Q_CONFIG4_REG_t;

/*----------------------------config 5 reg------------------------*/

typedef enum
{
		mbi6353q_25mA = 0x00u,
	    mbi6353q_25_29mA = 0x01u,
	    mbi6353q_25_58mA = 0x02u,
	    mbi6353q_25_87mA = 0x03u,
	    mbi6353q_26_16mA = 0x04u,
	    mbi6353q_26_45mA = 0x05u,
	    mbi6353q_26_74mA = 0x06u,
	    mbi6353q_27mA = 0x07u,
	    mbi6353q_27_29mA = 0x08u,
	    mbi6353q_27_58mA = 0x09u,
	    mbi6353q_27_87mA = 0x0Au,
	    mbi6353q_28_16mA = 0x0Bu,
	    mbi6353q_28_45mA = 0x0Cu,
	    mbi6353q_28_74mA = 0x0Du,
	    mbi6353q_29mA = 0x0Eu,
	    mbi6353q_29_29mA = 0x0Fu,
	    mbi6353q_29_58mA = 0x10u,
	    mbi6353q_29_87mA = 0x11u,
	    mbi6353q_30_16mA = 0x12u,
	    mbi6353q_30_45mA = 0x13u,
	    mbi6353q_30_74mA = 0x14u,
	    mbi6353q_31mA = 0x15u,
	    mbi6353q_31_29mA = 0x16u,
	    mbi6353q_31_58mA = 0x17u,
	    mbi6353q_31_87mA = 0x18u,
	    mbi6353q_32_16mA = 0x19u,
	    mbi6353q_33_45mA = 0x1Au,
	    mbi6353q_34_74mA = 0x1Bu,
	    mbi6353q_35mA = 0x1Cu,
	    mbi6353q_36_29mA = 0x1Du,
	    mbi6353q_37_58mA = 0x1Eu,
	    mbi6353q_37_87mA = 0x1Fu,
	    mbi6353q_38_16mA = 0x20u,
	    mbi6353q_38_45mA = 0x21u,
	    mbi6353q_38_74mA = 0x22u,
	    mbi6353q_39mA = 0x23u,
	    mbi6353q_39_29mA = 0x24u,
	    mbi6353q_39_58mA = 0x25u,
	    mbi6353q_39_87mA = 0x26u,
	    mbi6353q_40_16mA = 0x27u,
	    mbi6353q_40_45mA = 0x28u,
	    mbi6353q_40_74mA = 0x29u,
	    mbi6353q_41mA = 0x2Au,
	    mbi6353q_41_29mA = 0x2Bu,
	    mbi6353q_41_58mA = 0x2Cu,
	    mbi6353q_41_87mA = 0x2Du,
	    mbi6353q_42_16mA = 0x2Eu,
	    mbi6353q_42_45mA = 0x2Fu,
	    mbi6353q_42_74mA = 0x30u,
	    mbi6353q_43mA = 0x31u,
	    mbi6353q_43_29mA = 0x32u,
	    mbi6353q_43_58mA = 0x33u,
	    mbi6353q_43_87mA = 0x34u,
	    mbi6353q_44_16mA = 0x35u,
	    mbi6353q_44_45mA = 0x36u,
	    mbi6353q_44_74mA = 0x37u,
	    mbi6353q_45mA = 0x38u,
	    mbi6353q_45_29mA = 0x39u,
	    mbi6353q_45_58mA = 0x3Au,
	    mbi6353q_45_87mA = 0x3Bu,
	    mbi6353q_46_16mA = 0x3Cu,
	    mbi6353q_46_45mA = 0x3Du,
	    mbi6353q_46_74mA = 0x3Eu,
	    mbi6353q_47mA = 0x3Fu,
	    mbi6353q_47_29mA = 0x40u,
	    mbi6353q_47_58mA = 0x41u,
	    mbi6353q_47_87mA = 0x42u,
	    mbi6353q_48_16mA = 0x43u,
	    mbi6353q_48_45mA = 0x44u,
	    mbi6353q_48_74mA = 0x45u,
	    mbi6353q_49mA = 0x46u,
	    mbi6353q_49_29mA = 0x47u,
	    mbi6353q_49_58mA = 0x48u,
	    mbi6353q_49_87mA = 0x49u,
	    mbi6353q_50_16mA = 0x4Au,
	    mbi6353q_50_45mA = 0x4Bu,
	    mbi6353q_50_74mA = 0x4Cu,
	    mbi6353q_51mA = 0x4Du,
	    mbi6353q_51_29mA = 0x4Eu,
	    mbi6353q_51_58mA = 0x4Fu,
	    mbi6353q_51_87mA = 0x50u,
	    mbi6353q_52_16mA = 0x51u,
	    mbi6353q_52_45mA = 0x52u,
	    mbi6353q_52_74mA = 0x53u,
	    mbi6353q_53mA = 0x54u,
	    mbi6353q_53_29mA = 0x55u,
	    mbi6353q_53_58mA = 0x56u,
	    mbi6353q_53_87mA = 0x57u,
	    mbi6353q_54_16mA = 0x58u,
	    mbi6353q_54_45mA = 0x59u,
	    mbi6353q_54_74mA = 0x5Au,
	    mbi6353q_55mA = 0x5Bu,
	    mbi6353q_55_29mA = 0x5Cu,
	    mbi6353q_55_58mA = 0x5Du,
	    mbi6353q_55_87mA = 0x5Eu,
	    mbi6353q_56_16mA = 0x5Fu,
	    mbi6353q_56_45mA = 0x60u,
	    mbi6353q_56_74mA = 0x61u,
	    mbi6353q_57mA = 0x62u,
	    mbi6353q_57_29mA = 0x63u,
	    mbi6353q_57_58mA = 0x64u,
	    mbi6353q_57_87mA = 0x65u,
	    mbi6353q_58_16mA = 0x66u,
	    mbi6353q_58_45mA = 0x67u,
	    mbi6353q_58_74mA = 0x68u,
	    mbi6353q_59mA = 0x69u,
	    mbi6353q_59_29mA = 0x6Au,
	    mbi6353q_59_58mA = 0x6Bu,
	    mbi6353q_59_87mA = 0x6Cu,
	    mbi6353q_60_16mA = 0x6Du,
	    mbi6353q_60_45mA = 0x6Eu,
	    mbi6353q_60_74mA = 0x6Fu,
	    mbi6353q_61mA = 0x70u,
	    mbi6353q_61_29mA = 0x71u,
	    mbi6353q_61_58mA = 0x72u,
	    mbi6353q_61_87mA = 0x73u,
	    mbi6353q_62_16mA = 0x74u,
	    mbi6353q_62_45mA = 0x75u,
	    mbi6353q_62_74mA = 0x76u,
	    mbi6353q_63mA = 0x77u,
	    mbi6353q_63_29mA = 0x78u,
	    mbi6353q_63_58mA = 0x79u,
	    mbi6353q_63_87mA = 0x7Au,
	    mbi6353q_64_16mA = 0x7Bu,
	    mbi6353q_64_45mA = 0x7Cu,
	    mbi6353q_64_74mA = 0x7Du,
	    mbi6353q_65mA = 0x7Eu,
	    mbi6353q_65_29mA = 0x7Fu,
	    mbi6353q_65_58mA = 0x80u,
	    mbi6353q_65_87mA = 0x81u,
	    mbi6353q_66_16mA = 0x82u,
	    mbi6353q_66_45mA = 0x83u,
	    mbi6353q_66_74mA = 0x84u,
	    mbi6353q_67mA = 0x85u,
	    mbi6353q_67_29mA = 0x86u,
	    mbi6353q_67_58mA = 0x87u,
	    mbi6353q_67_87mA = 0x88u,
	    mbi6353q_68_16mA = 0x89u,
	    mbi6353q_68_45mA = 0x8Au,
	    mbi6353q_68_74mA = 0x8Bu,
	    mbi6353q_69mA = 0x8Cu,
	    mbi6353q_69_29mA = 0x8Du,
	    mbi6353q_69_58mA = 0x8Eu,
	    mbi6353q_69_87mA = 0x8Fu,
	    mbi6353q_70_16mA = 0x90u,
	    mbi6353q_70_45mA = 0x91u,
	    mbi6353q_70_74mA = 0x92u,
	    mbi6353q_71mA = 0x93u,
	    mbi6353q_71_29mA = 0x94u,
	    mbi6353q_71_58mA = 0x95u,
	    mbi6353q_71_87mA = 0x96u,
	    mbi6353q_72_16mA = 0x97u,
	    mbi6353q_72_45mA = 0x98u,
	    mbi6353q_70mA = 0x99u, // added this 4/23/2026
	    mbi6353q_73mA = 0x9Au,
	    mbi6353q_73_29mA = 0x9Bu,
	    mbi6353q_73_58mA = 0x9Cu,
	    mbi6353q_73_87mA = 0x9Du,
	    mbi6353q_74_16mA = 0x9Eu,
	    mbi6353q_74_45mA = 0x9Fu,
	    mbi6353q_74_74mA = 0xA0u,
	    mbi6353q_75mA = 0xA1u,
	    mbi6353q_75_29mA = 0xA2u,
	    mbi6353q_75_58mA = 0xA3u,
	    mbi6353q_75_87mA = 0xA4u,
	    mbi6353q_76_16mA = 0xA5u,
	    mbi6353q_76_45mA = 0xA6u,
	    mbi6353q_76_74mA = 0xA7u,
	    mbi6353q_77mA = 0xA8u,
	    mbi6353q_77_29mA = 0xA9u,
	    mbi6353q_77_58mA = 0xAAu,
	    mbi6353q_77_87mA = 0xABu,
	    mbi6353q_78_16mA = 0xACu,
	    mbi6353q_78_45mA = 0xADu,
	    mbi6353q_78_74mA = 0xAEu,
	    mbi6353q_79mA = 0xAFu,
	    mbi6353q_79_29mA = 0xB0u,
	    mbi6353q_79_58mA = 0xB1u,
	    mbi6353q_79_87mA = 0xB2u,
	    mbi6353q_80_16mA = 0xB3u,
	    mbi6353q_80_45mA = 0xB4u,
	    mbi6353q_80_74mA = 0xB5u,
	    mbi6353q_81mA = 0xB6u,
	    mbi6353q_81_29mA = 0xB7u,
	    mbi6353q_81_58mA = 0xB8u,
	    mbi6353q_81_87mA = 0xB9u,
	    mbi6353q_82_16mA = 0xBAu,
	    mbi6353q_82_45mA = 0xBBu,
	    mbi6353q_82_74mA = 0xBCu,
	    mbi6353q_83mA = 0xBDu,
	    mbi6353q_83_29mA = 0xBEu,
	    mbi6353q_83_58mA = 0xBFu,
	    mbi6353q_83_87mA = 0xC0u,
	    mbi6353q_84_16mA = 0xC1u,
	    mbi6353q_84_45mA = 0xC2u,
	    mbi6353q_84_74mA = 0xC3u,
	    mbi6353q_85mA = 0xC4u,
	    mbi6353q_85_29mA = 0xC5u,
	    mbi6353q_85_58mA = 0xC6u,
	    mbi6353q_85_87mA = 0xC7u,
	    mbi6353q_86_16mA = 0xC8u,
	    mbi6353q_86_45mA = 0xC9u,
	    mbi6353q_86_74mA = 0xCAu,
	    mbi6353q_87mA = 0xCBu,
	    mbi6353q_87_29mA = 0xCCu,
	    mbi6353q_87_58mA = 0xCDu,
	    mbi6353q_87_87mA = 0xCEu,
	    mbi6353q_88_16mA = 0xCFu,
	    mbi6353q_88_45mA = 0xD0u,
	    mbi6353q_88_74mA = 0xD1u,
	    mbi6353q_89mA = 0xD2u,
	    mbi6353q_89_29mA = 0xD3u,
	    mbi6353q_89_58mA = 0xD4u,
	    mbi6353q_89_87mA = 0xD5u,
	    mbi6353q_90_16mA = 0xD6u,
	    mbi6353q_90_45mA = 0xD7u,
	    mbi6353q_90_74mA = 0xD8u,
	    mbi6353q_91mA = 0xD9u,//very warm
	    mbi6353q_91_29mA = 0xDAu,
	    mbi6353q_91_58mA = 0xDBu,
	    mbi6353q_91_87mA = 0xDCu,
	    mbi6353q_92_16mA = 0xDDu,
	    mbi6353q_92_45mA = 0xDEu,
	    mbi6353q_92_74mA = 0xDFu,
	    mbi6353q_93mA = 0xE0u,
	    mbi6353q_93_29mA = 0xE1u,
	    mbi6353q_93_58mA = 0xE2u,
	    mbi6353q_93_87mA = 0xE3u,
	    mbi6353q_94_16mA = 0xE4u,
	    mbi6353q_94_45mA = 0xE5u,
	    mbi6353q_94_74mA = 0xE6u,
	    mbi6353q_95mA = 0xE7u,
	    mbi6353q_95_29mA = 0xE8u,
	    mbi6353q_95_58mA = 0xE9u,
	    mbi6353q_95_87mA = 0xEAu,
	    mbi6353q_96_16mA = 0xEBu,
	    mbi6353q_96_45mA = 0xECu,
	    mbi6353q_96_74mA = 0xEDu,
	    mbi6353q_97mA = 0xEEu,
	    mbi6353q_97_29mA = 0xEFu,
	    mbi6353q_97_58mA = 0xF0u,
	    mbi6353q_97_87mA = 0xF1u,
	    mbi6353q_98_16mA = 0xF2u,
	    mbi6353q_98_45mA = 0xF3u,
	    mbi6353q_98_74mA = 0xF4u,
	    mbi6353q_99mA = 0xF5u,
	    // ..........
	    mbi6353q_100mA = 0xFFu,
} MBI6353Q_GCG2_CURRENT_t;

typedef enum
{
    mbi6353q_hlm_disable = 0x00u,
    mbi6353q_hlm_enable = 0x01u,
} MBI6353Q_HLM_t;

typedef enum
{
    mbi6353q_lowSpeedRise = 0x00u,
    mbi6353q_rising1 = 0x01u,
    mbi6353q_rising2 = 0x02u,
    mbi6353q_rising3 = 0x03u,
    mbi6353q_rising4 = 0x04u,
    mbi6353q_rising5 = 0x05u,
    mbi6353q_rising6 = 0x06u,
    mbi6353q_highSpeedRise = 0x07u,
} MBI6353Q_RISING_t;

typedef enum
{
    mbi6353q_lowSpeedFall = 0x00u,
    mbi6353q_falling1 = 0x01u,
    mbi6353q_falling2 = 0x02u,
    mbi6353q_falling3 = 0x03u,
    mbi6353q_falling4 = 0x04u,
    mbi6353q_falling5 = 0x05u,
    mbi6353q_falling6 = 0x06u,
    mbi6353q_highSpeedFall = 0x07u,
} MBI6353Q_FALLING_t;

typedef struct
{
    uint16_t FALLING : 3;
    uint16_t RISING : 3;
    uint16_t RESERVE_7 : 1;
    uint16_t HLM_ENABLE : 1;
    uint8_t SET_CURRENT : 8;
} MBI6353Q_CONFIG5_REG_t;

/*------------------------config 6-8 reg-------------------------*/

typedef struct
{
    uint16_t RESERVED : 16;
} MBI6353Q_CONFIG6_REG_t;

typedef struct
{
    uint16_t RESERVED : 16;
} MBI6353Q_CONFIG7_REG_t;

typedef struct
{
    uint16_t RESERVED : 16;
} MBI6353Q_CONFIG8_REG_t;

/*---------------------------config 9 reg---------------------------*/

typedef enum
{
    mbi6353q_fbo_disable = 0x00u,
    mbi6353q_fbo_enable = 0x01u,
} MBI6353Q_FBO_t;

typedef enum
{
    mbi6353q_open_detect_off = 0x00u,
    mbi6353q_open_detect_on = 0x01u,
} MBI6353Q_OPEN_DETECT_ENABLE_t;

typedef enum
{
    mbi6353q_short_detect_off = 0x00u,
    mbi6353q_short_detect_on = 0x01u,
} MBI6353Q_SHORT_DETECT_ENABLE_t;

typedef enum
{
    mbi6353q_error1 = 0x00u,
    mbi6353q_error2 = 0x01u,
    mbi6353q_error3 = 0x02u,
    mbi6353q_error4 = 0x03u,
    mbi6353q_error5 = 0x04u,
    mbi6353q_error6 = 0x05u,
    mbi6353q_error7 = 0x06u,
    mbi6353q_error8 = 0x07u,
} MBI6353Q_NUM_ERROR_t;

typedef enum
{
    mbi6353q_fbo_update1 = 0x00u,
    mbi6353q_fbo_update2 = 0x01u,
    mbi6353q_fbo_update3 = 0x02u,
    mbi6353q_fbo_update4 = 0x03u,
} MBI6353Q_FBO_PERIOD_t;

typedef enum
{
    mbi6353q_mask_disable = 0x00u,
    mbi6353q_mask_enable = 0x01u,
} MBI6353Q_LED_ERROR_MASK_t;

typedef enum
{
    mbi6353q_interrupt_disable = 0x00,
    mbi6353q_interrupt_enable = 0x01,
} MBI6353Q_INTTERUPT_PIN_t;

typedef enum
{
    mbi6353q_open_detect1 = 0x00,
    mbi6353q_open_detect2 = 0x01,
    mbi6353q_open_detect3 = 0x02,
    mbi6353q_open_detect4 = 0x03,
} MBI6353Q_OPEN_DETECT_VOLTAGE_t;

typedef enum
{
    mbi6353q_short_detect1 = 0x00u,
    mbi6353q_short_detect2 = 0x01u,
    mbi6353q_short_detect3 = 0x02u,
    mbi6353q_short_detect4 = 0x03u,
} MBI6353Q_SHORT_DETECT_VOLTAGE_t;

typedef struct
{
    uint16_t SHORT_DETECT_V : 2;
    uint16_t OPEN_DETECT_V : 2;
    uint16_t RESERVE_4 : 1;
    uint16_t INTERRUPT_PIN : 1;
    uint16_t ERROR_MASK : 1;
    uint16_t RESERVE_7 : 1;
    uint16_t FBO_PERIOD : 2;
    uint16_t NUM_ERROR : 3;
    uint16_t SHORT_DETECT_ENABLE : 1;
    uint16_t OPEN_DETECT_ENABLE : 1;
    uint16_t FBO_ENABLE : 1;
} MBI6353Q_CONFIG9_REG_t;

/*-----------------------config 10-15 reg------------------------*/
typedef struct
{
    uint16_t RESERVED : 16;
} MBI6353Q_CONFIG10_REG_t;

typedef struct
{
    uint16_t RESERVED : 16;
} MBI6353Q_CONFIG11_REG_t;

typedef struct
{
    uint16_t RESERVED : 16;
} MBI6353Q_CONFIG12_REG_t;

typedef struct
{
    uint16_t RESERVED : 16;
} MBI6353Q_CONFIG13_REG_t;

typedef struct
{
    uint16_t RESERVED : 16;
} MBI6353Q_CONFIG14_REG_t;

typedef struct
{
    uint16_t RESERVED : 16;
} MBI6353Q_CONFIG15_REG_t;

/*------------------------config 16 reg---------------------------*/

typedef enum
{
    mbi6353q_chip_sleep_off = 0x00u,
    mbi6353q_chip_sleep_on = 0x01u,
} MBI6353Q_CHIP_SLEEP_t;

typedef enum
{
    mbi6353q_timing_rst_off = 0x00u,
    mbi6353q_timing_rst_on = 0x01u,
} MBI6353Q_TIMING_RST_t;

typedef struct
{
    uint16_t RESERVE_4_0 : 5;
    uint16_t TIMING_RST : 1;
    uint16_t RESERVE_8_6 : 3;
    uint16_t CHIP_SLEEP : 1;
    uint16_t RESERVE_15_10 : 6;
} MBI6353Q_CONFIG16_REG_t;
/*------------------------- brightness control------------------------------*/
typedef enum
{
    mbi6353q_iout_100 = 0x00,
    mbi6353q_iout_200 = 0x01,
    mbi6353q_iout_300 = 0x02,
    mbi6353q_iout_400 = 0x03,
} MBI6353Q_HIGH_LUMINANCE_t;

typedef struct
{
    uint16_t BCS1 : 12;
    uint16_t HIGH_LUMINANCE : 2;
    uint16_t RESERVED_15_14 : 2;
} MBI6353Q_BRIGHTNESS_REG_t;

/*------------------------fault status reg---------------------------------*/

typedef enum
{
    mbi6353q_reg_unlock = 0x00u,
    mbi6353q_reg_lock = 0x01u,
} MBI6353Q_REG_LOCK_t;

typedef enum
{
    mbi6353q_checksum_pass = 0x00u,
    mbi6353q_checksum_fail = 0x01u,
} MBI6353Q_CHECKSUM_t;

typedef enum
{
    mbi6353q_short_pass = 0x00u,
    mbi6353q_short_fail = 0x01u
} MBI6353Q_SHORT_FAULT_t;

typedef enum
{
    mbi6353q_open_pass = 0x00u,
    mbi6353q_open_fail = 0x01u,
} MBI6353Q_OPEN_FAULT_t;

typedef enum
{
    mbi6353q_thermal_ok = 0x00u,
    mbi6353q_thermal_shutdown = 0x01u,
} MBI6353Q_THERMAL_SHUTDOWN_t;

typedef struct
{
    uint16_t THERMAL_SHUTDOWN : 1;
    uint16_t OPEN_FAULT : 1;
    uint16_t SHORT_FAULT : 1;
    uint16_t CHECKSUM : 1;
    uint16_t REG_LOCK : 1;
    uint16_t RESERVED_15_5 : 11;
} MBI6353Q_FAULT_STATUS_REG_t;

/*----------------------mask regs--------------------*/

typedef enum
{
    mbi6353q_no_mask = 0x00u,
    mbi6353q_mask = 0x01u,
} MBI6353Q_MASK_t;

typedef struct
{
    uint16_t MASK0 : 16; // CHANNEL 48-33
    uint16_t MASK1 : 16; // CHANNEL 32-17
    uint16_t MASK2 : 16; // CHANNEL 16-1
} MBI6353Q_MASK_REG_t;

/*-------------------error result regs--------------------*/

typedef enum
{
    mbi6353q_error = 0x00u,
    mbi6353q_no_error = 0x01u,
} MBI6353Q_ERROR_DETECT_t;

typedef struct
{
    uint16_t ERROR_MASK0 : 16;
    uint16_t ERROR_MASK1 : 16;
    uint16_t ERROR_MASK2 : 16;
} MBI6353Q_ERROR_REG_t;

/*---------------------------Control Message---------------------------------*/

typedef enum
{
    mbi6353q_all_device = 0x01u,
    mbi6353q_single_device = 0x00u,
} MBI6353Q_BROADCAST_t;

typedef enum
{
    mbi6353q_single_data = 0x01u,
    mbi6353q_burst_data = 0x00,
} MBI6353Q_SINGLE_DATA_t;

typedef enum
{
    mbi6353q_write_all = 0x00u,
    mbi6353q_device_1 = 0x01u,
    mbi6353q_device_2 = 0x02u,
    mbi6353q_device_3 = 0x03u,
    mbi6353q_device_4 = 0x04u,
} MBI6353Q_DEVICE_ADDRESS_t;

typedef struct
{
    uint16_t RESERVED_7_0 : 8;
    uint16_t DEVICE_ADDRESS : 6;
    uint16_t SINGLE_DATA : 1;
    uint16_t BROADCAST : 1;

} MBI6353Q_DEVICE_ADDRESS_FRAME_t;

typedef enum
{
    mbi6353q_read = 0x01u,
    mbi6353q_write = 0x00u,
} MBI6353Q_READ_WRITE_t;

typedef struct
{
    uint16_t REG_ADDRESS : 15;
    uint16_t READ_WRITE : 1;
} MBI6353Q_REG_ADDRESS_FRAME_t;

typedef struct
{
    uint16_t NUM_DATA : 16;
} MBI6353Q_NUM_DATA_FRAME_t;

typedef struct
{
    uint16_t CHECKSUM_CMD : 16;
} MBI6353Q_CHECKSUM_CMD_t;

typedef struct
{
    uint16_t DATA : 16;
} MBI6353Q_DATA_FRAME_t;

typedef union
{
    MBI6353Q_CONFIG1_REG_t s_config1_reg;
    MBI6353Q_CONFIG2_REG_t s_config2_reg;
    MBI6353Q_CONFIG3_REG_t s_config3_reg;
    MBI6353Q_CONFIG4_REG_t s_config4_reg;
    MBI6353Q_CONFIG5_REG_t s_config5_reg;
    MBI6353Q_CONFIG6_REG_t s_config6_reg;
    MBI6353Q_CONFIG7_REG_t s_config7_reg;
    MBI6353Q_CONFIG8_REG_t s_config8_reg;
    MBI6353Q_CONFIG9_REG_t s_config9_reg;
    MBI6353Q_CONFIG10_REG_t s_config10_reg;
    MBI6353Q_CONFIG11_REG_t s_config11_reg;
    MBI6353Q_CONFIG12_REG_t s_config12_reg;
    MBI6353Q_CONFIG13_REG_t s_config13_reg;
    MBI6353Q_CONFIG14_REG_t s_config14_reg;
    MBI6353Q_CONFIG15_REG_t s_config15_reg;
    MBI6353Q_CONFIG16_REG_t s_config16_reg;
    MBI6353Q_BRIGHTNESS_REG_t s_brightness_reg;
    MBI6353Q_FAULT_STATUS_REG_t s_fault_status_reg;
    MBI6353Q_MASK_REG_t s_mask_reg;
    MBI6353Q_ERROR_REG_t s_error_reg;
} MBI6353Q_Register_t;

typedef struct
{
    MBI6353Q_DEVICE_ADDRESS_FRAME_t s_device_address_frame;
    MBI6353Q_DATA_FRAME_t s_num_data;
    MBI6353Q_REG_ADDRESS_FRAME_t s_reg_address_frame;

} MBI6353Q_Burst_Cmd_t;

typedef struct
{
    MBI6353Q_DEVICE_ADDRESS_FRAME_t s_device_address_frame;
    MBI6353Q_REG_ADDRESS_FRAME_t s_reg_address_frame;
} MBI6353Q_Single_Cmd_t;

//

/**********************************************************************
 *                        Function Prototypes
 **********************************************************************/
void MBI6353Q_CreateBurstCmd(const MBI6353Q_Burst_Cmd_t *mbi6353q_burst_cmd, uint8_t *u8p_buffer);
void MBI6353Q_CreateSingleCmd(const MBI6353Q_Single_Cmd_t* mbi6353q_single_cmd, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig1(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig2(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig3(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig4(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig5(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig6(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig7(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig8(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig9(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig10(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig11(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig12(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig13(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig14(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig15(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteConfig16(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);
void MBI6353Q_WriteBrightness(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer);

#endif
/**********************************************************************
 *                           End of File
 **********************************************************************/
