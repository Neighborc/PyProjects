# Chris Neighbor
# initial python hamming distance sequence not using reservoir computing

print('How many bits is your input bitstream?:')
size = input()
size = int(size)
while True:
    print(f'Enter a {size} bit stream A:')
    bitstream_A = input()
    print(f'Enter another {size} bit stream B:')
    bitstream_B = input()
    if len(bitstream_A) != size or len(bitstream_B) != size:
        print(f'Wrong number of bits! Please enter a {size}-bit number for both values')
    elif len(bitstream_A) == size and len(bitstream_B) == size:
        break
print(f'A = {bitstream_A} \nB =  {bitstream_B}')
distance = 0
for bit in range(0,len(bitstream_A)):
    if bitstream_A[bit] != bitstream_B[bit]:
        distance += 1
print(f'Hamming distance = {distance}')
