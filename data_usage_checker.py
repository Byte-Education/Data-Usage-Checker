import os

def get_networks():
    os.system("top -l 1 -n 0 > top.txt")
    with open("top.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if "Networks" in line:
                return line.split()

def parse_networks():
    network_data = {"in": 0, "out": 0}
    with open("top.txt", "r") as f:
        for line in f:
            if "Networks" in line:
                network_data["in"] = line.split()[2].split("/")[1]
                network_data["out"] = line.split()[4].split("/")[1]
    return network_data

def get_total(network_data):
    return int(network_data["in"][0:-1]) + int(network_data["out"][0:-1])

def get_uptime():
    os.system("uptime > uptime.txt")
    with open("uptime.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if "up" in line:
                return line.split()[2]

def analyze(name, data):
    print(f"{name}: {data}")

if __name__ == "__main__":
  get_networks()
  total = get_total(parse_networks())
  uptime = get_uptime()
  analyze("Total", f"{total}GB")
  analyze("Uptime", f"{uptime} days")
  analyze("Average per day", f"{total / int(uptime)}GB")