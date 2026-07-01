# # """
# # calibration/visible_light_algorithm.py

# # Visible light target algorithm for the Lightbox GUI.

# # The GUI gives this file:
# #     - target mlux value
# #     - mode: "glare" or "ambient"

# # This file returns the CAN command recipe needed to create that light level.
# # """

# # from config.app_config import (
# #     DRIVER_HEADLIGHT,
# #     DRIVER_SUNLIGHT,
# # )


# # COMMAND_CURRENT = "current"
# # COMMAND_ALL_PWM = "all_pwm"
# # COMMAND_SINGLE_PWM = "single_pwm"

# # MODE_GLARE = "glare"
# # MODE_AMBIENT = "ambient"

# # HEADLIGHT_FORMATION_LOWEST = {
# #     0x02: [1, 23, 34],
# #     0x03: [4, 20, 38],
# #     0x04: [20, 23],
# #     0x05: [20, 23],
# #     0x06: [5, 23, 39],
# #     0x07: [9, 20, 42],
# # }

# # GLARE_PCB_IDS = [0x02, 0x03, 0x04, 0x05, 0x06, 0x07]
# # AMBIENT_PCB_IDS = [0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D]

# # MIN_GLARE_ALL_LED_MLUX = 120
# # MIN_AMBIENT_ALL_LED_MLUX = 120  # TODO: update after measurement

# # MAX_VISIBLE_MLUX = 300_000


# # LOW_LIGHT_RECIPES = {
# #     MODE_GLARE: {
# #         1: [
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 1,
# #                 "value": 13,
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 13,
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 34,
# #                 "value": 13,
# #             },

# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 4,
# #                 "value": 13,
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 13,
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 38,
# #                 "value": 13,
# #             },

# #             {
# #                 "can_id": 0x04,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x04,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 13,
# #             },
# #             {
# #                 "can_id": 0x04,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 13,
# #             },
# #             {
# #                 "can_id": 0x05,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x05,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 13,
# #             },
# #             {
# #                 "can_id": 0x05,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 13,
# #             },

# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 5,
# #                 "value": 13,
# #             },
# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 13,
# #             },
# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 39,
# #                 "value": 13,
# #             },

# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 9,
# #                 "value": 13,
# #             },
# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 13,
# #             },
# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 42,
# #                 "value": 13,
# #             },
# #         ],

# #         2: [
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 1,
# #                 "value": 26,
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 26,
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 34,
# #                 "value": 26,
# #             },

# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 4,
# #                 "value": 26,
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 26,
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 38,
# #                 "value": 26,
# #             },

# #             {
# #                 "can_id": 0x04,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x04,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 26,
# #             },
# #             {
# #                 "can_id": 0x04,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 26,
# #             },
# #             {
# #                 "can_id": 0x05,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x05,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 26,
# #             },
# #             {
# #                 "can_id": 0x05,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 26,
# #             },

# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 5,
# #                 "value": 26,
# #             },
# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 26,
# #             },
# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 39,
# #                 "value": 26,
# #             },

# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 9,
# #                 "value": 26,
# #             },
# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 26,
# #             },
# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 42,
# #                 "value": 26,
# #             },
# #         ],

# #         3: [
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 1,
# #                 "value": 39,
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 39,
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 34,
# #                 "value": 39,
# #             },

# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 4,
# #                 "value": 39,
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 39,
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 38,
# #                 "value": 39,
# #             },

# #             {
# #                 "can_id": 0x04,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x04,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 39,
# #             },
# #             {
# #                 "can_id": 0x04,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 39,
# #             },
# #             {
# #                 "can_id": 0x05,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x05,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 39,
# #             },
# #             {
# #                 "can_id": 0x05,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 39,
# #             },

# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 5,
# #                 "value": 39,
# #             },
# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 39,
# #             },
# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 39,
# #                 "value": 39,
# #             },

# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 9,
# #                 "value": 39,
# #             },
# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 39,
# #             },
# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 42,
# #                 "value": 39,
# #             },
# #         ],

# #         4: [
# #                 {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 1,
# #                 "value": 52,
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 52,
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 34,
# #                 "value": 52,
# #             },

# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 4,
# #                 "value": 52,
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 52,
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 38,
# #                 "value": 52,
# #             },

# #             {
# #                 "can_id": 0x04,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x04,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 52,
# #             },
# #             {
# #                 "can_id": 0x04,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 52,
# #             },
# #             {
# #                 "can_id": 0x05,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x05,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 52,
# #             },
# #             {
# #                 "can_id": 0x05,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 52,
# #             },

# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 5,
# #                 "value": 52,
# #             },
# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 52,
# #             },
# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 39,
# #                 "value": 52,
# #             },

# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 9,
# #                 "value": 52,
# #             },
# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 52,
# #             },
# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 42,
# #                 "value": 52,
# #             },
# #         ],

# #         10: [
# #                 {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 1,
# #                 "value": 100,
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 100,
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 34,
# #                 "value": 100,
# #             },

# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 4,
# #                 "value": 100,
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 100,
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 38,
# #                 "value": 100,
# #             },

# #             {
# #                 "can_id": 0x04,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x04,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 100,
# #             },
# #             {
# #                 "can_id": 0x04,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 100,
# #             },
# #             {
# #                 "can_id": 0x05,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x05,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 100,
# #             },
# #             {
# #                 "can_id": 0x05,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 100,
# #             },

# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 5,
# #                 "value": 100,
# #             },
# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 23,
# #                 "value": 100,
# #             },
# #             {
# #                 "can_id": 0x06,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 39,
# #                 "value": 100,
# #             },

# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4
# #             },
# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 9,
# #                 "value": 100,
# #             },
# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 20,
# #                 "value": 100,
# #             },
# #             {
# #                 "can_id": 0x07,
# #                 "type": COMMAND_SINGLE_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "led": 42,
# #                 "value": 100,
# #             },
# #         ],

# #         20: [
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4,
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_ALL_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 1,
# #             },
# #         ],

# #         40: [
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4,
# #             },
# #             {
# #                 "can_id": 0x02,
# #                 "type": COMMAND_ALL_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 1,
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 4,
# #             },
# #             {
# #                 "can_id": 0x03,
# #                 "type": COMMAND_ALL_PWM,
# #                 "driver": DRIVER_HEADLIGHT,
# #                 "value": 1,
# #             },
# #         ],
# #     },

# #     MODE_AMBIENT: {
# #         # TODO: fill in once ambient low-light measurements are taken.
# #     },
# # }


# # NORMAL_LIGHT_POINTS = {
# #     MODE_GLARE: {
# #         120: {
# #             "driver": DRIVER_HEADLIGHT,
# #             "current_ma": 4,
# #             "pwm": 1,
# #         },

# #         500: {
# #             "driver": DRIVER_HEADLIGHT,
# #             "current_ma": 4,
# #             "pwm": 2,
# #         },

# #         1_000: {
# #             "driver": DRIVER_HEADLIGHT,
# #             "current_ma": 7,
# #             "pwm":3,
# #         },

# #         10_000: {
# #             "driver": DRIVER_HEADLIGHT,
# #             "current_ma": 8,
# #             "pwm": 13,
# #         },

# #         100_000: {
# #             "driver": DRIVER_HEADLIGHT,
# #             "current_ma": 49,
# #             "pwm": 27,
# #         },

# #         300_000: { # confirmed
# #             "driver": DRIVER_HEADLIGHT,
# #             "current_ma": 49,
# #             "pwm": 75,
# #         },
# #     },

# #     MODE_AMBIENT: {
# #         120: {
# #             "driver": DRIVER_HEADLIGHT,
# #             "current_ma": 4,
# #             "pwm": 1,
# #         },

# #         500: {
# #             "driver": DRIVER_HEADLIGHT,
# #             "current_ma": 4,
# #             "pwm": 3,
# #         },

# #         1_000: {
# #             "driver": DRIVER_HEADLIGHT,
# #             "current_ma": 4,
# #             "pwm": 6,
# #         },

# #         10_000: {
# #             "driver": DRIVER_HEADLIGHT,
# #             "current_ma": 8,
# #             "pwm": 25,
# #         },

# #         100_000: {
# #             "driver": DRIVER_HEADLIGHT,
# #             "current_ma": 20,
# #             "pwm": 60,
# #         },

# #         300_000: {
# #             "driver": DRIVER_HEADLIGHT,
# #             "current_ma": 30,
# #             "pwm": 50,
# #         },
# #     },
# # }


# # def normalize_mlux(mlux: int) -> int:
# #     """
# #     Clamp and round DOWN to the nearest valid increment.

# #     1-1000 mlux         -> 1 mlux steps
# #     1000-5000 mlux      -> 5 mlux steps
# #     5000-25000 mlux     -> 10 mlux steps
# #     25000-100000 mlux   -> 50 mlux steps
# #     100000-300000 mlux  -> 1000 mlux steps
# #     """

# #     mlux = max(1, min(mlux, MAX_VISIBLE_MLUX))

# #     if mlux <= 1_000:
# #         step = 1
# #     elif mlux <= 5_000:
# #         step = 5
# #     elif mlux <= 25_000:
# #         step = 10
# #     elif mlux <= 100_000:
# #         step = 50
# #     else:
# #         step = 1_000

# #     return (mlux // step) * step


# # def get_pcb_ids_for_mode(mode: str):
# #     if mode == MODE_GLARE:
# #         return GLARE_PCB_IDS

# #     if mode == MODE_AMBIENT:
# #         return AMBIENT_PCB_IDS

# #     raise ValueError(f"Invalid visible light mode: {mode}")


# # def get_min_all_led_mlux_for_mode(mode: str):
# #     if mode == MODE_GLARE:
# #         return MIN_GLARE_ALL_LED_MLUX

# #     if mode == MODE_AMBIENT:
# #         return MIN_AMBIENT_ALL_LED_MLUX

# #     raise ValueError(f"Invalid visible light mode: {mode}")


# # def interpolate_value(x, x0, y0, x1, y1):
# #     if x0 == x1:
# #         return y0

# #     ratio = (x - x0) / (x1 - x0)
# #     return y0 + ratio * (y1 - y0)


# # def find_surrounding_points(target_mlux: int, points: dict):
# #     mlux_points = sorted(points.keys())

# #     if target_mlux <= mlux_points[0]:
# #         return mlux_points[0], mlux_points[0]

# #     if target_mlux >= mlux_points[-1]:
# #         return mlux_points[-1], mlux_points[-1]

# #     for index in range(len(mlux_points) - 1):
# #         low = mlux_points[index]
# #         high = mlux_points[index + 1]

# #         if low <= target_mlux <= high:
# #             return low, high

# #     raise ValueError(f"No calibration range found for {target_mlux} mlux.")


# # def get_low_light_commands(mlux: int, mode: str):
# #     mode_recipes = LOW_LIGHT_RECIPES.get(mode)

# #     if mode_recipes is None:
# #         raise ValueError(f"No low-light recipe table exists for mode: {mode}")

# #     if mlux not in mode_recipes:
# #         raise ValueError(
# #             f"No low-light recipe exists yet for {mlux} mlux in {mode} mode. "
# #             "Low-light range needs measured recipes."
# #         )

# #     return mode_recipes[mlux]


# # def get_normal_light_commands(mlux: int, mode: str):
# #     pcb_ids = get_pcb_ids_for_mode(mode)
# #     points = NORMAL_LIGHT_POINTS.get(mode)

# #     if points is None:
# #         raise ValueError(f"No normal-light calibration table exists for mode: {mode}")

# #     low_mlux, high_mlux = find_surrounding_points(mlux, points)

# #     low_point = points[low_mlux]
# #     high_point = points[high_mlux]

# #     if low_point["driver"] != high_point["driver"]:
# #         raise ValueError(
# #             f"Cannot interpolate between different drivers: "
# #             f"{low_mlux} mlux and {high_mlux} mlux."
# #         )

# #     driver = low_point["driver"]

# #     current_ma = round(
# #         interpolate_value(
# #             mlux,
# #             low_mlux,
# #             low_point["current_ma"],
# #             high_mlux,
# #             high_point["current_ma"],
# #         )
# #     )

# #     pwm = round(
# #         interpolate_value(
# #             mlux,
# #             low_mlux,
# #             low_point["pwm"],
# #             high_mlux,
# #             high_point["pwm"],
# #         )
# #     )

# #     current_ma = max(4, min(current_ma, 60))
# #     pwm = max(1, min(pwm, 100))

# #     commands = []

# #     for can_id in pcb_ids:
# #         commands.append(
# #             {
# #                 "can_id": can_id,
# #                 "type": COMMAND_CURRENT,
# #                 "driver": driver,
# #                 "value": current_ma,
# #             }
# #         )

# #         commands.append(
# #             {
# #                 "can_id": can_id,
# #                 "type": COMMAND_ALL_PWM,
# #                 "driver": driver,
# #                 "value": pwm,
# #             }
# #         )

# #     return commands


# # def get_visible_commands(target_mlux: int, mode: str):
# #     """
# #     Return the rounded mlux value and CAN command list for that light target.

# #     Below the all-LED minimum, use exact low-light recipes.
# #     At or above the all-LED minimum, interpolate between normal calibration points.
# #     """

# #     rounded_mlux = normalize_mlux(target_mlux)
# #     min_all_led_mlux = get_min_all_led_mlux_for_mode(mode)

# #     if rounded_mlux < min_all_led_mlux:
# #         commands = get_low_light_commands(rounded_mlux, mode)
# #     else:
# #         commands = get_normal_light_commands(rounded_mlux, mode)

# #     return rounded_mlux, commands

# # # """
# # # calibration/visible_light_sweep_algorithm.py
# # # """

# # # from config.app_config import (
# # #     DRIVER_HEADLIGHT,
# # #     DRIVER_SUNLIGHT,
# # # )


# # # MIN_CURRENT_MA = 4
# # # MAX_CURRENT_MA = 49

# # # MIN_PWM = 10
# # # MAX_PWM = 75


# # # # Based on your measured data.
# # # # This is only used to sort the sweep from dimmest to brightest.
# # # K = 0.100628
# # # CURRENT_EXPONENT = 0.90436
# # # PWM_EXPONENT = 1.02692


# # # def estimate_visible_lux(current_ma: int, pwm: int) -> float:
# # #     return K * (current_ma ** CURRENT_EXPONENT) * (pwm ** PWM_EXPONENT)


# # # def build_visible_sweep_table():
# # #     """
# # #     Builds all current/PWM combinations and sorts them from dimmest to brightest.
# # #     """

# # #     sweep_table = []

# # #     for current_ma in range(MIN_CURRENT_MA, MAX_CURRENT_MA + 1):
# # #         for pwm in range(MIN_PWM, MAX_PWM + 1):
# # #             estimated_lux = estimate_visible_lux(current_ma, pwm)

# # #             sweep_table.append({
# # #                 "current_ma": current_ma,
# # #                 "pwm": pwm,
# # #                 "estimated_lux": estimated_lux,
# # #             })

# # #     sweep_table.sort(key=lambda item: item["estimated_lux"])

# # #     return sweep_table


# # # VISIBLE_SWEEP_TABLE = build_visible_sweep_table()


# # # def get_visible_sweep_recipe(slider_value: int, driver: int):
# # #     if driver not in (DRIVER_HEADLIGHT, DRIVER_SUNLIGHT):
# # #         raise ValueError("Visible sweep only supports headlight or sunlight drivers.")

# # #     max_index = len(VISIBLE_SWEEP_TABLE) - 1

# # #     if slider_value < 0:
# # #         slider_value = 0

# # #     if slider_value > max_index:
# # #         slider_value = max_index

# # #     recipe = VISIBLE_SWEEP_TABLE[slider_value]

# # #     return {
# # #         "driver": driver,
# # #         "slider_value": slider_value,
# # #         "max_slider_value": max_index,
# # #         "current_ma": recipe["current_ma"],
# # #         "pwm": recipe["pwm"],
# # #         "estimated_lux": round(recipe["estimated_lux"], 2),
# # #     }


# """
# calibration/visible_light_algorithm.py

# Visible light target algorithm for the Lightbox GUI.

# The GUI gives this file:
#     - target mlux value
#     - mode: "glare" or "ambient"

# This file returns:
#     - the rounded mlux value
#     - a list of CAN commands to send

# Design notes:
#     - Low-light glare uses a fixed LED formation.
#     - For low-light glare, only PWM changes:
#           1 mlux -> 13% PWM
#           2 mlux -> 26% PWM
#           3 mlux -> 39% PWM
#           ...
#     - Current stays at 4 mA for low-light glare.
#     - Normal light uses all LEDs and interpolates between measured points.
# """

# from config.app_config import (
#     DRIVER_HEADLIGHT,
#     DRIVER_SUNLIGHT,
# )


# # -----------------------------------------------------------------------------
# # Command types
# # -----------------------------------------------------------------------------

# COMMAND_CURRENT = "current"
# COMMAND_ALL_PWM = "all_pwm"
# COMMAND_SINGLE_PWM = "single_pwm"


# # -----------------------------------------------------------------------------
# # Modes
# # -----------------------------------------------------------------------------

# MODE_GLARE = "glare"
# MODE_AMBIENT = "ambient"


# # -----------------------------------------------------------------------------
# # PCB groups
# # -----------------------------------------------------------------------------

# GLARE_PCB_IDS = [0x02, 0x03, 0x04, 0x05, 0x06, 0x07]
# AMBIENT_PCB_IDS = [0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D]


# # -----------------------------------------------------------------------------
# # General limits
# # -----------------------------------------------------------------------------

# MAX_VISIBLE_MLUX = 300_000

# # For glare, anything below this uses the low-light formation.
# # Right now, the low-light formation only supports 1-7 mlux because
# # 8 mlux would require 104% PWM with the current 13% per mlux pattern.
# MIN_GLARE_ALL_LED_MLUX = 120
# MIN_AMBIENT_ALL_LED_MLUX = 120  # TODO: update after ambient measurement


# # -----------------------------------------------------------------------------
# # Low-light glare formation
# # -----------------------------------------------------------------------------

# LOW_LIGHT_CURRENT_MA = 4
# LOW_LIGHT_PWM_PER_MLUX = 10
# LOW_LIGHT_MAX_MLUX = 10

# # This formation is used for low-light glare.
# # The formation stays the same. Only PWM changes.
# HEADLIGHT_FORMATION_LOWEST = {
#     0x02: [1, 23, 34],
#     0x03: [4, 20, 38],
#     0x04: [20, 23],
#     0x05: [20, 23],
#     0x06: [5, 23, 39],
#     0x07: [9, 20, 42],
# }

# HEADLIGHT_FORMATION_MIDLOWEST = {
#     0x02: [1, 2, 3, 4, 23, 34],
#     0x03: [1, 2, 3, 4, 20, 38],
#     0x04: [10, 15, 20, 23, 24, 29],
#     0x05: [14, 19, 20, 23, 28, 33],
#     0x06: [5, 23, 39, 40, 41, 42],
#     0x07: [9, 20, 39, 40, 41, 42],
# }

# HEADLIGHT_FORMATION_MID = {
#     0x02: [1, 2, 3, 4, 5, 10, 15, 20, 21, 22, 23, 34],
#     0x03: [1, 2, 3, 4, 9, 14, 19, 20, 21, 22, 23, 38],
#     0x04: [5, 10, 15, 20, 21, 22, 23, 24, 29, 34],
#     0x05: [9, 14, 19, 20, 21, 22, 23, 28, 33, 38],
#     0x06: [5, 20, 21, 22, 23, 24, 29, 34, 39, 40, 41, 42],
#     0x07: [9, 20, 21, 22, 23, 28, 33, 38, 39, 40, 41, 42],
# }

# HEADLIGHT_FORMATION_MIDHIGH = {
#     0x02: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 21, 22, 23, 24, 29, 34, 39, 40, 41, 42],
#     0x03: [1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 19, 20, 21, 22, 23, 28, 33, 38, 39, 40, 41, 42],
#     0x04: [5, 10, 15, 20, 21, 22, 23, 24, 29, 34],
#     0x05: [9, 14, 19, 20, 21, 22, 23, 28, 33, 38],
#     0x06: [1, 2, 3, 4, 5, 10, 15, 20, 21, 22, 23, 24, 29, 34, 35, 36, 37, 38, 39, 40, 41, 42],
#     0x07: [1, 2, 3, 4, 9, 14, 19, 20, 21, 22, 23, 28, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
# }

# HEADLIGHT_FORMATION_HIGH = {
#     0x02: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 34, 35, 39, 40, 41, 42],
#     0x03: [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 32, 33, 37, 38, 39, 40, 41, 42],
#     0x04: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25, 29, 30, 34, 35, 36, 37, 38, 39, 40, 41, 42],
#     0x05: [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 18, 19, 20, 21, 22, 23, 27, 28, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
#     0x06: [1, 2, 3, 4, 5, 6, 10, 11, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 29, 30, 34, 35, 36, 37, 38, 39, 40, 41, 42],
#     0x07: [1, 2, 3, 4, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 27, 28, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
# }

# HEADLIGHT_FORMATION_NEXTHIGH = {
#     0x02: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
#     0x03: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
#     0x04: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
#     0x05: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
#     0x06: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
#     0x07: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
# }

# HEADLIGHT_FORMATION_ALMOSTHIGH = {
#     0x02: [0],
#     0x03: [0],
#     0x04: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
#     0x05: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
#     0x06: [0],
#     0x07: [0],
# }

# HEADLIGHT_FORMATION_HIGHEST = {
#     0x02: [0],
#     0x03: [0],
#     0x04: [0],
#     0x05: [0],
#     0x06: [0],
#     0x07: [0],
# }

# CALIBRATION_FORMATIONS = {
#     "formation_1_low_light": {
#         "name": "formation_1_low_light",
#         "driver": DRIVER_HEADLIGHT,
#         "formation": HEADLIGHT_FORMATION_LOWEST,
#         "min_current_ma": 4,
#         "max_current_ma": 50,
#         "min_pwm": 10,
#         "max_pwm": 100,
#         "pwm_step": 5,
#         "settle_time_s": 2.0,
#         "output_csv": "formation_1_low_light_calibration.csv",
#     },

#     "formation_3_midlow_light": {
#         "name": "formation_3_midlow_light",
#         "driver": DRIVER_HEADLIGHT,
#         "formation": HEADLIGHT_FORMATION_MIDLOWEST,
#         "min_current_ma": 4,
#         "max_current_ma": 50,
#         "min_pwm": 10,
#         "max_pwm": 100,
#         "pwm_step": 5,
#         "settle_time_s": 2.0,
#         "output_csv": "formation_3_midlow_light_calibration.csv",
#     },

#     "formation_4_mid_light": {
#         "name": "formation_4_mid_light",
#         "driver": DRIVER_HEADLIGHT,
#         "formation": HEADLIGHT_FORMATION_MID,
#         "min_current_ma": 4,
#         "max_current_ma": 50,
#         "min_pwm": 10,
#         "max_pwm": 100,
#         "pwm_step": 5,
#         "settle_time_s": 2.0,
#         "output_csv": "formation_4_mid_light_calibration.csv",
#     },

#     "formation_5_midhigh_light": {
#         "name": "formation_5_midhigh_light",
#         "driver": DRIVER_HEADLIGHT,
#         "formation": HEADLIGHT_FORMATION_MIDHIGH,
#         "min_current_ma": 4,
#         "max_current_ma": 50,
#         "min_pwm": 10,
#         "max_pwm": 100,
#         "pwm_step": 5,
#         "settle_time_s": 2.0,
#         "output_csv": "formation_5_midhigh_light_calibration.csv",
#     },

#     "formation_6_high_light": {
#         "name": "formation_6_high_light",
#         "driver": DRIVER_HEADLIGHT,
#         "formation": HEADLIGHT_FORMATION_HIGH,
#         "min_current_ma": 4,
#         "max_current_ma": 50,
#         "min_pwm": 10,
#         "max_pwm": 100,
#         "pwm_step": 5,
#         "settle_time_s": 2.0,
#         "output_csv": "formation_6_high_light_calibration.csv",
#     },

#     "formation_7_higher_light": {
#         "name": "formation_7_higher_light",
#         "driver": DRIVER_HEADLIGHT,
#         "formation": HEADLIGHT_FORMATION_NEXTHIGH,
#         "min_current_ma": 4,
#         "max_current_ma": 50,
#         "min_pwm": 10,
#         "max_pwm": 100,
#         "pwm_step": 5,
#         "settle_time_s": 2.0,
#         "output_csv": "formation_7_higher_light_calibration.csv",
#     },

#     "formation_8_highest_light": {
#         "name": "formation_8_highest_light",
#         "driver": DRIVER_HEADLIGHT,
#         "formation": HEADLIGHT_FORMATION_ALMOSTHIGH,
#         "min_current_ma": 4,
#         "max_current_ma": 50,
#         "min_pwm": 10,
#         "max_pwm": 100,
#         "pwm_step": 5,
#         "settle_time_s": 2.0,
#         "output_csv": "formation_8_highest_light_calibration.csv",
#     },

#     "formation_2_bright_light": {
#         "name": "formation_2_bright_light",
#         "driver": DRIVER_HEADLIGHT,
#         "formation": HEADLIGHT_FORMATION_HIGHEST,
#         "min_current_ma": 4,
#         "max_current_ma": 50,
#         "min_pwm": 10,
#         "max_pwm": 100,
#         "pwm_step": 5,
#         "settle_time_s": 2.0,
#         "output_csv": "formation_2_bright_light_calibration.csv",
#     },
# }

# # -----------------------------------------------------------------------------
# # Normal all-LED calibration points
# # -----------------------------------------------------------------------------

# NORMAL_LIGHT_POINTS = {
#     MODE_GLARE: {
#         120: {
#             "driver": DRIVER_HEADLIGHT,
#             "current_ma": 4,
#             "pwm": 1,
#         },
#         500: {
#             "driver": DRIVER_HEADLIGHT,
#             "current_ma": 4,
#             "pwm": 2,
#         },
#         1_000: {
#             "driver": DRIVER_HEADLIGHT,
#             "current_ma": 7,
#             "pwm": 3,
#         },
#         10_000: {
#             "driver": DRIVER_HEADLIGHT,
#             "current_ma": 8,
#             "pwm": 13,
#         },
#         100_000: {
#             "driver": DRIVER_HEADLIGHT,
#             "current_ma": 49,
#             "pwm": 27,
#         },
#         300_000: {  # confirmed
#             "driver": DRIVER_HEADLIGHT,
#             "current_ma": 49,
#             "pwm": 75,
#         },
#     },

#     MODE_AMBIENT: {
#         120: {
#             "driver": DRIVER_HEADLIGHT,
#             "current_ma": 4,
#             "pwm": 1,
#         },
#         500: {
#             "driver": DRIVER_HEADLIGHT,
#             "current_ma": 4,
#             "pwm": 3,
#         },
#         1_000: {
#             "driver": DRIVER_HEADLIGHT,
#             "current_ma": 4,
#             "pwm": 6,
#         },
#         10_000: {
#             "driver": DRIVER_HEADLIGHT,
#             "current_ma": 8,
#             "pwm": 25,
#         },
#         100_000: {
#             "driver": DRIVER_HEADLIGHT,
#             "current_ma": 20,
#             "pwm": 60,
#         },
#         300_000: {
#             "driver": DRIVER_HEADLIGHT,
#             "current_ma": 30,
#             "pwm": 50,
#         },
#     },
# }


# # -----------------------------------------------------------------------------
# # Helpers
# # -----------------------------------------------------------------------------

# def normalize_mlux(mlux: int) -> int:
#     """
#     Clamp and round DOWN to the nearest valid increment.

#     1-1000 mlux         -> 1 mlux steps
#     1000-5000 mlux      -> 5 mlux steps
#     5000-25000 mlux     -> 10 mlux steps
#     25000-100000 mlux   -> 50 mlux steps
#     100000-300000 mlux  -> 1000 mlux steps
#     """

#     mlux = max(1, min(mlux, MAX_VISIBLE_MLUX))

#     if mlux <= 1_000:
#         step = 1
#     elif mlux <= 5_000:
#         step = 5
#     elif mlux <= 25_000:
#         step = 10
#     elif mlux <= 100_000:
#         step = 50
#     else:
#         step = 1_000

#     return (mlux // step) * step


# def get_pcb_ids_for_mode(mode: str):
#     if mode == MODE_GLARE:
#         return GLARE_PCB_IDS

#     if mode == MODE_AMBIENT:
#         return AMBIENT_PCB_IDS

#     raise ValueError(f"Invalid visible light mode: {mode}")


# def get_min_all_led_mlux_for_mode(mode: str):
#     if mode == MODE_GLARE:
#         return MIN_GLARE_ALL_LED_MLUX

#     if mode == MODE_AMBIENT:
#         return MIN_AMBIENT_ALL_LED_MLUX

#     raise ValueError(f"Invalid visible light mode: {mode}")


# def interpolate_value(x, x0, y0, x1, y1):
#     if x0 == x1:
#         return y0

#     ratio = (x - x0) / (x1 - x0)
#     return y0 + ratio * (y1 - y0)


# def find_surrounding_points(target_mlux: int, points: dict):
#     mlux_points = sorted(points.keys())

#     if target_mlux <= mlux_points[0]:
#         return mlux_points[0], mlux_points[0]

#     if target_mlux >= mlux_points[-1]:
#         return mlux_points[-1], mlux_points[-1]

#     for index in range(len(mlux_points) - 1):
#         low = mlux_points[index]
#         high = mlux_points[index + 1]

#         if low <= target_mlux <= high:
#             return low, high

#     raise ValueError(f"No calibration range found for {target_mlux} mlux.")


# # -----------------------------------------------------------------------------
# # Low-light command generation
# # -----------------------------------------------------------------------------

# def build_low_light_formation_commands(mlux: int, mode: str):
#     """
#     Build low-light commands from a fixed LED formation.

#     Current stays at 4 mA.
#     PWM is generated from the mlux value:
#         pwm = mlux * 13

#     This prevents copying the same LED formation over and over.
#     """

#     if mode != MODE_GLARE:
#         raise ValueError("Low-light formation is only defined for glare mode right now.")

#     if mlux < 1:
#         mlux = 1

#     if mlux > LOW_LIGHT_MAX_MLUX:
#         raise ValueError(
#             f"Low-light glare only supports 1-{LOW_LIGHT_MAX_MLUX} mlux right now. "
#             "The transition range still needs measured recipes."
#         )

#     pwm = mlux * LOW_LIGHT_PWM_PER_MLUX
#     pwm = max(1, min(pwm, 100))

#     commands = []

#     for can_id, led_list in HEADLIGHT_FORMATION_LOWEST.items():
#         commands.append(
#             {
#                 "can_id": can_id,
#                 "type": COMMAND_CURRENT,
#                 "driver": DRIVER_HEADLIGHT,
#                 "value": LOW_LIGHT_CURRENT_MA,
#             }
#         )

#         for led in led_list:
#             commands.append(
#                 {
#                     "can_id": can_id,
#                     "type": COMMAND_SINGLE_PWM,
#                     "driver": DRIVER_HEADLIGHT,
#                     "led": led,
#                     "value": pwm,
#                 }
#             )

#     return commands


# def get_low_light_commands(mlux: int, mode: str):
#     if mode == MODE_AMBIENT:
#         raise ValueError("Ambient low-light formation has not been measured yet.")

#     return build_low_light_formation_commands(mlux, mode)


# # -----------------------------------------------------------------------------
# # Normal all-LED command generation
# # -----------------------------------------------------------------------------

# def get_normal_light_commands(mlux: int, mode: str):
#     pcb_ids = get_pcb_ids_for_mode(mode)
#     points = NORMAL_LIGHT_POINTS.get(mode)

#     if points is None:
#         raise ValueError(f"No normal-light calibration table exists for mode: {mode}")

#     low_mlux, high_mlux = find_surrounding_points(mlux, points)

#     low_point = points[low_mlux]
#     high_point = points[high_mlux]

#     if low_point["driver"] != high_point["driver"]:
#         raise ValueError(
#             f"Cannot interpolate between different drivers: "
#             f"{low_mlux} mlux and {high_mlux} mlux."
#         )

#     driver = low_point["driver"]

#     current_ma = round(
#         interpolate_value(
#             mlux,
#             low_mlux,
#             low_point["current_ma"],
#             high_mlux,
#             high_point["current_ma"],
#         )
#     )

#     pwm = round(
#         interpolate_value(
#             mlux,
#             low_mlux,
#             low_point["pwm"],
#             high_mlux,
#             high_point["pwm"],
#         )
#     )

#     current_ma = max(4, min(current_ma, 60))
#     pwm = max(1, min(pwm, 100))

#     commands = []

#     for can_id in pcb_ids:
#         commands.append(
#             {
#                 "can_id": can_id,
#                 "type": COMMAND_CURRENT,
#                 "driver": driver,
#                 "value": current_ma,
#             }
#         )

#         commands.append(
#             {
#                 "can_id": can_id,
#                 "type": COMMAND_ALL_PWM,
#                 "driver": driver,
#                 "value": pwm,
#             }
#         )

#     return commands


# # -----------------------------------------------------------------------------
# # Main public function used by GUI
# # -----------------------------------------------------------------------------

# def get_visible_commands(target_mlux: int, mode: str):
#     """
#     Return the rounded mlux value and CAN command list for that light target.

#     Current supported glare ranges:
#         - 1-7 mlux:
#             fixed low-light LED formation
#         - 120-300000 mlux:
#             all-LED normal calibration

#     Current unsupported glare range:
#         - 8-119 mlux:
#             needs measured transition recipes

#     Current ambient support:
#         - 120-300000 mlux only
#         - low-light ambient still needs measurement
#     """

#     rounded_mlux = normalize_mlux(target_mlux)
#     min_all_led_mlux = get_min_all_led_mlux_for_mode(mode)

#     if mode == MODE_GLARE and rounded_mlux <= LOW_LIGHT_MAX_MLUX:
#         commands = get_low_light_commands(rounded_mlux, mode)

#     elif rounded_mlux < min_all_led_mlux:
#         if mode == MODE_AMBIENT:
#             raise ValueError(
#                 f"No ambient recipe exists yet for {rounded_mlux} mlux. "
#                 f"Current ambient support starts at {min_all_led_mlux} mlux."
#             )

#         raise ValueError(
#             f"No glare recipe exists yet for {rounded_mlux} mlux. "
#             f"Current glare support is 1-{LOW_LIGHT_MAX_MLUX} mlux "
#             f"and {min_all_led_mlux}-{MAX_VISIBLE_MLUX} mlux."
#         )

#     else:
#         commands = get_normal_light_commands(rounded_mlux, mode)

#     return rounded_mlux, commands

"""
calibration/visible_light_algorithm.py

Visible light target algorithm for the Lightbox GUI.

This version uses the auto-generated lookup table created from the CSV sweeps.
The lookup table chooses:
    - formation_name
    - current_ma
    - pwm_percent

This file converts that lookup row into the CAN command list the GUI already sends.
"""

from config.app_config import DRIVER_HEADLIGHT
from calibration.visible_light_lookup_table import VISIBLE_LIGHT_LOOKUP


# -----------------------------------------------------------------------------
# Command types
# -----------------------------------------------------------------------------

COMMAND_CURRENT = "current"
COMMAND_ALL_PWM = "all_pwm"
COMMAND_SINGLE_PWM = "single_pwm"


# -----------------------------------------------------------------------------
# Modes
# -----------------------------------------------------------------------------

MODE_GLARE = "glare"
MODE_AMBIENT = "ambient"


# -----------------------------------------------------------------------------
# PCB groups
# -----------------------------------------------------------------------------

GLARE_PCB_IDS = [0x02, 0x03, 0x04, 0x05, 0x06, 0x07]
AMBIENT_PCB_IDS = [0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D]


# -----------------------------------------------------------------------------
# General limits / target step sizes
# -----------------------------------------------------------------------------

MAX_VISIBLE_MLUX = 300_001

HEADLIGHT_FORMATION_LOWEST = {
    0x02: [1, 23, 34],
    0x03: [4, 20, 38],
    0x04: [20, 23],
    0x05: [20, 23],
    0x06: [5, 23, 39],
    0x07: [9, 20, 42],
}

HEADLIGHT_FORMATION_MIDLOWEST = {
    0x02: [1, 2, 3, 4, 23, 34],
    0x03: [1, 2, 3, 4, 20, 38],
    0x04: [10, 15, 20, 23, 24, 29],
    0x05: [14, 19, 20, 23, 28, 33],
    0x06: [5, 23, 39, 40, 41, 42],
    0x07: [9, 20, 39, 40, 41, 42],
}

HEADLIGHT_FORMATION_MID = {
    0x02: [1, 2, 3, 4, 5, 10, 15, 20, 21, 22, 23, 34],
    0x03: [1, 2, 3, 4, 9, 14, 19, 20, 21, 22, 23, 38],
    0x04: [5, 10, 15, 20, 21, 22, 23, 24, 29, 34],
    0x05: [9, 14, 19, 20, 21, 22, 23, 28, 33, 38],
    0x06: [5, 20, 21, 22, 23, 24, 29, 34, 39, 40, 41, 42],
    0x07: [9, 20, 21, 22, 23, 28, 33, 38, 39, 40, 41, 42],
}

HEADLIGHT_FORMATION_MIDHIGH = {
    0x02: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 21, 22, 23, 24, 29, 34, 39, 40, 41, 42],
    0x03: [1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 19, 20, 21, 22, 23, 28, 33, 38, 39, 40, 41, 42],
    0x04: [5, 10, 15, 20, 21, 22, 23, 24, 29, 34],
    0x05: [9, 14, 19, 20, 21, 22, 23, 28, 33, 38],
    0x06: [1, 2, 3, 4, 5, 10, 15, 20, 21, 22, 23, 24, 29, 34, 35, 36, 37, 38, 39, 40, 41, 42],
    0x07: [1, 2, 3, 4, 9, 14, 19, 20, 21, 22, 23, 28, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
}

HEADLIGHT_FORMATION_HIGH = {
    0x02: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 34, 35, 39, 40, 41, 42],
    0x03: [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 32, 33, 37, 38, 39, 40, 41, 42],
    0x04: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25, 29, 30, 34, 35, 36, 37, 38, 39, 40, 41, 42],
    0x05: [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 18, 19, 20, 21, 22, 23, 27, 28, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
    0x06: [1, 2, 3, 4, 5, 6, 10, 11, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 29, 30, 34, 35, 36, 37, 38, 39, 40, 41, 42],
    0x07: [1, 2, 3, 4, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 27, 28, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
}

HEADLIGHT_FORMATION_NEXTHIGH = {
    0x02: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
    0x03: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
    0x04: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
    0x05: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
    0x06: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
    0x07: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
}

HEADLIGHT_FORMATION_ALMOSTHIGH = {
    0x02: [0],
    0x03: [0],
    0x04: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
    0x05: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
    0x06: [0],
    0x07: [0],
}

HEADLIGHT_FORMATION_HIGHEST = {
    0x02: [0],
    0x03: [0],
    0x04: [0],
    0x05: [0],
    0x06: [0],
    0x07: [0],
}

CALIBRATION_FORMATIONS = {
    "headlight_formation_lowest": {
        "name": "headlight_formation_lowest",
        "driver": DRIVER_HEADLIGHT,
        "formation": HEADLIGHT_FORMATION_LOWEST,
        "min_current_ma": 4,
        "max_current_ma": 50,
        "min_pwm": 10,
        "max_pwm": 100,
        "pwm_step": 5,
        "settle_time_s": 2.0,
        "output_csv": "headlight_formation_lowest_calibration.csv",
    },

    "formation_3_midlow_light": {
        "name": "formation_3_midlow_light",
        "driver": DRIVER_HEADLIGHT,
        "formation": HEADLIGHT_FORMATION_MIDLOWEST,
        "min_current_ma": 4,
        "max_current_ma": 50,
        "min_pwm": 10,
        "max_pwm": 100,
        "pwm_step": 5,
        "settle_time_s": 2.0,
        "output_csv": "formation_3_midlow_light_calibration.csv",
    },

    "formation_4_mid_light": {
        "name": "formation_4_mid_light",
        "driver": DRIVER_HEADLIGHT,
        "formation": HEADLIGHT_FORMATION_MID,
        "min_current_ma": 4,
        "max_current_ma": 50,
        "min_pwm": 10,
        "max_pwm": 100,
        "pwm_step": 5,
        "settle_time_s": 2.0,
        "output_csv": "formation_4_mid_light_calibration.csv",
    },

    "formation_5_midhigh_light": {
        "name": "formation_5_midhigh_light",
        "driver": DRIVER_HEADLIGHT,
        "formation": HEADLIGHT_FORMATION_MIDHIGH,
        "min_current_ma": 4,
        "max_current_ma": 50,
        "min_pwm": 10,
        "max_pwm": 100,
        "pwm_step": 5,
        "settle_time_s": 2.0,
        "output_csv": "formation_5_midhigh_light_calibration.csv",
    },

    "formation_6_high_light": {
        "name": "formation_6_high_light",
        "driver": DRIVER_HEADLIGHT,
        "formation": HEADLIGHT_FORMATION_HIGH,
        "min_current_ma": 4,
        "max_current_ma": 50,
        "min_pwm": 10,
        "max_pwm": 100,
        "pwm_step": 5,
        "settle_time_s": 2.0,
        "output_csv": "formation_6_high_light_calibration.csv",
    },

    "formation_7_higher_light": {
        "name": "formation_7_higher_light",
        "driver": DRIVER_HEADLIGHT,
        "formation": HEADLIGHT_FORMATION_NEXTHIGH,
        "min_current_ma": 4,
        "max_current_ma": 50,
        "min_pwm": 10,
        "max_pwm": 100,
        "pwm_step": 5,
        "settle_time_s": 2.0,
        "output_csv": "formation_7_higher_light_calibration.csv",
    },

    "formation_8_highest_light": {
        "name": "formation_8_highest_light",
        "driver": DRIVER_HEADLIGHT,
        "formation": HEADLIGHT_FORMATION_ALMOSTHIGH,
        "min_current_ma": 4,
        "max_current_ma": 50,
        "min_pwm": 10,
        "max_pwm": 100,
        "pwm_step": 5,
        "settle_time_s": 2.0,
        "output_csv": "formation_8_highest_light_calibration.csv",
    },

    "headlight_all_leds": {
        "name": "headlight_all_leds",
        "driver": DRIVER_HEADLIGHT,
        "formation": HEADLIGHT_FORMATION_HIGHEST,
        "min_current_ma": 4,
        "max_current_ma": 50,
        "min_pwm": 10,
        "max_pwm": 100,
        "pwm_step": 5,
        "settle_time_s": 2.0,
        "output_csv": "headlight_all_leds_calibration.csv",
    },
}

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def normalize_mlux(mlux: int) -> int:
    """
    Clamp and round DOWN to the nearest required increment.

    Required steps:
        1-1000 mlux          -> 1 mlux steps
        1000-5000 mlux       -> 10 mlux steps
        5000-25000 mlux      -> 25 mlux steps
        25000-300000 mlux    -> 100 mlux steps
    """

    mlux = max(0, min(int(mlux), MAX_VISIBLE_MLUX))

    if mlux == 0:
        return 0

    if mlux <= 1_000:
        step = 1
    elif mlux <= 5_000:
        step = 10
    elif mlux <= 25_000:
        step = 25
    else:
        step = 100

    return (mlux // step) * step


def get_pcb_ids_for_mode(mode: str):
    if mode == MODE_GLARE:
        return GLARE_PCB_IDS

    if mode == MODE_AMBIENT:
        return AMBIENT_PCB_IDS

    raise ValueError(f"Invalid visible light mode: {mode}")


def get_lookup_row(rounded_mlux: int):
    """Return the measured/interpolated recipe from the generated table."""

    if rounded_mlux not in VISIBLE_LIGHT_LOOKUP:
        raise ValueError(
            f"No lookup recipe exists for {rounded_mlux} mlux. "
            "Regenerate visible_light_lookup_table.py and make sure it goes to 300 lux."
        )

    return VISIBLE_LIGHT_LOOKUP[rounded_mlux]


def build_all_off_commands(mode: str):
    """Build commands for 0 mlux."""

    commands = []

    for can_id in get_pcb_ids_for_mode(mode):
        commands.append(
            {
                "can_id": can_id,
                "type": COMMAND_ALL_PWM,
                "driver": DRIVER_HEADLIGHT,
                "value": 0,
            }
        )

    return commands


def build_commands_from_lookup_row(row: dict, mode: str):
    """
    Convert one VISIBLE_LIGHT_LOOKUP row into CAN commands.

    Lookup row format expected:
        {
            "formation_name": "formation_8_highest_light",
            "current_ma": 4,
            "pwm_percent": 10,
        }

    Formation rule:
        [0] means send COMMAND_ALL_PWM to that PCB.
        Otherwise, send COMMAND_SINGLE_PWM to each listed LED.
    """

    if mode != MODE_GLARE:
        raise ValueError(
            "This lookup table currently uses glare/headlight PCB formations only. "
            "Generate an ambient lookup table before using ambient mode."
        )

    formation_name = row.get("formation_name")
    current_ma = int(row.get("current_ma"))
    pwm_percent = int(row.get("pwm_percent"))

    if formation_name not in CALIBRATION_FORMATIONS:
        raise ValueError(
            f"Formation '{formation_name}' was found in the lookup table, "
            "but it does not exist in CALIBRATION_FORMATIONS."
        )

    formation_config = CALIBRATION_FORMATIONS[formation_name]
    formation = formation_config["formation"]
    driver = formation_config["driver"]

    commands = []

    for can_id, led_list in formation.items():
        commands.append(
            {
                "can_id": can_id,
                "type": COMMAND_CURRENT,
                "driver": driver,
                "value": current_ma,
            }
        )

        if led_list == [0]:
            commands.append(
                {
                    "can_id": can_id,
                    "type": COMMAND_ALL_PWM,
                    "driver": driver,
                    "value": pwm_percent,
                }
            )
        else:
            for led in led_list:
                commands.append(
                    {
                        "can_id": can_id,
                        "type": COMMAND_SINGLE_PWM,
                        "driver": driver,
                        "led": led,
                        "value": pwm_percent,
                    }
                )

    return commands


# -----------------------------------------------------------------------------
# Main public function used by GUI
# -----------------------------------------------------------------------------

def get_visible_commands(target_mlux: int, mode: str):
    """
    Return:
        rounded_mlux, commands

    Flow:
        target_mlux
        -> round down to required step size
        -> get row from VISIBLE_LIGHT_LOOKUP
        -> get formation from CALIBRATION_FORMATIONS
        -> build CAN commands
    """

    rounded_mlux = normalize_mlux(target_mlux)

    if rounded_mlux == 0:
        return rounded_mlux, build_all_off_commands(mode)

    lookup_row = get_lookup_row(rounded_mlux)
    commands = build_commands_from_lookup_row(lookup_row, mode)

    return rounded_mlux, commands
