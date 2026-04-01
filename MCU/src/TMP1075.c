#include "TMP1075.h"
#include <string.h>

void TMP1075_WriteWord(TMP1075_Write_Word_Cmd_t* tmp1075_write_word_cmd, uint8_t* u8p_buffer)
{
    u8p_buffer[0] = tmp1075_write_word_cmd->POINTER_REG;
    u8p_buffer[1] = tmp1075_write_word_cmd->DATA_1;
    u8p_buffer[2] = tmp1075_write_word_cmd->DATA_2;
}

void TMP1075_WriteSingle(TMP1075_Write_Single_Cmd_t* tmp1075_write_single_cmd, uint8_t* u8p_buffer)
{
    u8p_buffer[0] = tmp1075_write_single_cmd->POINTER_REG;
    u8p_buffer[1] = tmp1075_write_single_cmd->DATA;
}

void TMP1075_Read_Pointer(TMP1075_Write_Single_Cmd_t* tmp1075_write_single_cmd, uint8_t* u8p_buffer)
{
    u8p_buffer[0] = tmp1075_write_single_cmd->POINTER_REG;
}


