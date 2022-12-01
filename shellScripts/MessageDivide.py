import sys

f1 = open("partition1_1.txt", 'a')
f2 = open("partition1_2.txt", 'a')
f3 = open("partition1_3.txt", 'a')
f4 = open("temp.txt", 'w')
f5 = open("tempWhole.txt", 'a')

message = sys.argv[1]

f1.write(message.split(' ',2)[0])
f1.write('   ')
f2.write(message.split(' ',2)[1])
f2.write('   ')
f3.write(message.split(' ',2)[2])
f3.write('   ')
f4.write(message)
f5.write(message)

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
