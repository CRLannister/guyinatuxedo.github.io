hero = [0x0, 0x64, 0xd6, 0x10a, 0x171, 0x1a1, 0x20f, 0x26e, 0x2dd, 0x34f, 0x3ae, 0x41e, 0x452, 0x4c6, 0x538, 0x5a1, 0x604, 0x635, 0x696, 0x704, 0x763, 0x7cc, 0x840, 0x875, 0x8d4, 0x920, 0x96c, 0x9c2, 0xa0f]

flag = ""

for i in range(1, len(hero)):
	flag += chr(hero[i] - hero[i - 1])

print "We fought off the dragon: " + flag