# import struct
# import subprocess
# import time
# import resource

# prefix = b"::::::::::::::"
# program = "./lastchallenge"

# def launch(program, arg, output_file):
#     try:
#         with open(output_file, 'wb') as output:
#             p = subprocess.Popen([program], stdin=subprocess.PIPE, stdout=output, stderr=subprocess.STDOUT, text=True)
#             p.communicate(arg)
#     except Exception as e:
#         print(e)

# def loop(range, pack, output_file):
#     for i in range:
#         arg = prefix + struct.pack(pack, i)
#         launch(program, arg, output_file)

# def main():
#     output_file = "output.txt"  # Specify the output file name

#     loop(range(0x3000, 0x5000), "I", output_file)
#     time.sleep(5)

# if __name__ == "__main__":
#     main()

import struct
import subprocess
import time
import resource


prefix = b"::::::::::::::"
program = "./lastchallenge"


def launch(program, arg, output_file):
    try:
        with open(output_file, 'w') as file:
            p = subprocess.Popen([program], stdin=subprocess.PIPE)
            p.communicate(arg)
    except Exception as e:
        print(e)


def loop(range, pack, output_file):
    for i in range:
        arg = prefix + struct.pack(pack, i)
        #print(arg)
        launch(program, arg, output_file)


def main():
    output_file = "output.txt"
    # loop(range(0x00, 0x800), "I")
    # time.sleep(5)
    # loop(range(0x800, 0x1000), "I")
    # time.sleep(5)
    # loop(range(0x1000, 0x2000), "I")
    # time.sleep(5)
    # loop(range(0x3000, 0x5000), "I", output_file)
    # time.sleep(5)
    # need to go to 0xA1A79EE7
    loop(range(0xA19EFEAF, 0xA19F21D7), "I", output_file)
    time.sleep(5)
    # loop(range(0x7000, 0x10000), "I")
    # time.sleep(5)
    # loop(range(0x8000, 0x10000), "I")
    # time.sleep(5)
    # loop(range(0x10000, 0x18000), "I")
    # time.sleep(5)
    # loop(range(0x18000, 0x20000), "I")
    # time.sleep(5)
    # loop(range(0x20000, 0x28000), "I")
    # time.sleep(5)
    # loop(range(0x28000, 0x30000), "I")


if __name__ == "__main__":
    main()