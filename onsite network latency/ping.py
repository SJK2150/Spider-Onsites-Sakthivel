from ping3 import ping

def pingservermultipletimes(server, count=4):
    latencies = []
    for _ in range(count):
        latency = ping(server, timeout=2)
        if latency:
            latencies.append(latency)
    return latencies

def display_results(server):
    latencies = pingservermultipletimes(server)
    if latencies:
        average_latency = sum(latencies) / len(latencies)
        packet_loss = (1 - len(latencies) / 4) * 100
        print(f"Server: {server}")
        print(f"Average Latency: {average_latency:.2f} ms")
        print(f"Packet Loss: {packet_loss:.2f}%")
    else:
        print(f"Failed to ping {server}.")

def getserverinput():
    server = input("Enter the server IP or hostname: ")
    display_results(server)

if __name__ == "__main__":
    getserverinput()
