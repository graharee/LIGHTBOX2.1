################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/CAN_interface.c \
../src/MBI6353Q.c \
../src/MBI6353Q_Interface.c \
../src/TMP1075.c \
../src/TMP1075_Interface.c \
../src/Utils.c \
../src/main.c 

OBJS += \
./src/CAN_interface.o \
./src/MBI6353Q.o \
./src/MBI6353Q_Interface.o \
./src/TMP1075.o \
./src/TMP1075_Interface.o \
./src/Utils.o \
./src/main.o 

C_DEPS += \
./src/CAN_interface.d \
./src/MBI6353Q.d \
./src/MBI6353Q_Interface.d \
./src/TMP1075.d \
./src/TMP1075_Interface.d \
./src/Utils.d \
./src/main.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Standard S32DS C Compiler'
	arm-none-eabi-gcc "@src/CAN_interface.args" -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


