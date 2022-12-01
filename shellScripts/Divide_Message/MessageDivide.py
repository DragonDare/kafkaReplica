import sys

f1 = open("partition1_1.txt", 'a')
f2 = open("partition1_2.txt", 'a')
f3 = open("partition1_3.txt", 'a')

message = sys.argv[1: ]

f1.write(message[0])
f2.write(message[1])
f3.write(message[2])

f1.close()
f2.close()
f3.close()
