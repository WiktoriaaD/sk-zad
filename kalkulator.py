ip_value="12.34.56.78/28"
ip_value = ip_value.split("/")
print(ip_value) 

ip = ip_value[0].split(".")
print(ip)
print(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))

ip = (int(ip[0]) << 24) | (int(ip[1]) << 16) | (int(ip[2]) << 8 | int(ip[3]))
print(ip)

mask = int("1" * int(ip_value[1]) + "0" * (32 - int(ip_value[1])), 2)
print("Mask:" ,mask)

network = ip & mask
broadcast = network | ~mask & 0xFFFFFFFF

first_host = network + 1
last_host = broadcast - 1

hosts = 2 ** (32 - int(ip_value[1])) - 2

def convert(x):
    print(format(x, "032b"))
    print((x>>24)&255, (x>>16)&255, (x>>8)&255, x&255)
    print("\n")


print("\nIlosc hostow:", hosts)
print("Adres sieci:")
convert(network)
print("Adres rozgloszeniowy:")
convert(broadcast)
print("Pierwszy host:")
convert(first_host)
print("Ostatni host:")
convert(last_host)