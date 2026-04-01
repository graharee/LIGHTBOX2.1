#include "MBI6353Q.h"

void MBI6353Q_CreateBurstCmd(const MBI6353Q_Burst_Cmd_t* mbi6353q_burst_cmd, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_burst_cmd->s_device_address_frame, sizeof(uint8_t)*2);
    memcpy(&u8p_buffer[2], &mbi6353q_burst_cmd->s_num_data, sizeof(uint8_t)*2);
    memcpy(&u8p_buffer[4], &mbi6353q_burst_cmd->s_reg_address_frame, sizeof(uint8_t)*2);
}

void MBI6353Q_CreateSingleCmd(const MBI6353Q_Single_Cmd_t* mbi6353q_single_cmd, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_single_cmd->s_device_address_frame, sizeof(uint8_t)*2);
    memcpy(&u8p_buffer[2], &mbi6353q_single_cmd->s_reg_address_frame, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig1(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config1_reg,sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig2(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config2_reg, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig3(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config3_reg, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig4(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config4_reg, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig5(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config5_reg, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig6(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config6_reg, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig7(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config7_reg, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig8(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config8_reg, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig9(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config9_reg, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig10(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config10_reg, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig11(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config11_reg, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig12(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config12_reg, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig13(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config13_reg, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig14(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config14_reg, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig15(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config15_reg, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteConfig16(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_config16_reg, sizeof(uint8_t)*2);
}

void MBI6353Q_WriteBrightness(const MBI6353Q_Register_t* mbi6353q_data, uint8_t* u8p_buffer)
{
    memcpy(&u8p_buffer[0], &mbi6353q_data->s_brightness_reg, sizeof(uint8_t)*2);
}





//memcpy(&u8p_buffer[4], &mbi6353q_cmd->u_regMap.s_config1_reg, sizeof(uint8_t)*2);


