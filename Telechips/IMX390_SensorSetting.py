
# Exposure Template
exposure = 950
# 1000 Dark
# 900 brightness ==> good
# 850 soso , 800 밝음






# SHS1 => 0x000C
command_template1 = "./i2cset -y -f 7 0x1a 0x00 0x0D {} i"
command_template2 = "./i2cset -y -f 7 0x1a 0x00 0x0C {} i"

# SHS2 => 0x0010
command_template3 = "./i2cset -y -f 7 0x1a 0x00 0x11 {} i"
command_template4 = "./i2cset -y -f 7 0x1a 0x00 0x10 {} i"

expH = exposure >> 8
expL = exposure & 0xFF

modified_command1 = command_template1.format(hex(expH))
modified_command2 = command_template2.format(hex(expL))
modified_command3 = command_template3.format(hex(expH))
modified_command4 = command_template4.format(hex(expL))
# print(modified_command1)
# print(modified_command2)
# print(modified_command3)
# print(modified_command4)


# Analog Gain Telplate
gain = 100

# AGAIN_SP1H => 0x0018
command_template1 = "./i2cset -y -f 7 0x1a 0x00 0x19 {} i"
command_template2 = "./i2cset -y -f 7 0x1a 0x00 0x18 {} i"

# AGAIN_SP1L => 0x001A
command_template3 = "./i2cset -y -f 7 0x1a 0x00 0x1B {} i"
command_template4 = "./i2cset -y -f 7 0x1a 0x00 0x1A {} i"

gainH = gain >> 8
gainL = gain & 0xFF

modified_command5 = command_template1.format(hex(gainH))
modified_command6 = command_template2.format(hex(gainL))
modified_command7 = command_template3.format(hex(gainH))
modified_command8 = command_template4.format(hex(gainL))

# Digital Gain Telplate
Dgain = 3

# PGA_GAIN_SP1H => 0x0024
command_template1 = "./i2cset -y -f 7 0x1a 0x00 0x25 {} i"
command_template2 = "./i2cset -y -f 7 0x1a 0x00 0x24 {} i"


gainH = Dgain >> 8
gainL = Dgain & 0xFF

modified_command9 = command_template1.format(hex(gainH))
modified_command10 = command_template2.format(hex(gainL))






# 결과를 result.txt 파일에 저장
with open("result.txt", "w") as f:
    f.write(modified_command1 + "\n")
    f.write(modified_command2 + "\n")
    f.write(modified_command3 + "\n")
    f.write(modified_command4 + "\n\n")
    f.write(modified_command5 + "\n")
    f.write(modified_command6 + "\n")
    f.write(modified_command7 + "\n")
    f.write(modified_command8 + "\n\n")
    f.write(modified_command9 + "\n")
    f.write(modified_command10 + "\n")
    f.write("\n")

print("Commands written to result.txt")
