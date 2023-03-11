import subprocess

# Ask for user input
ip_address = input("Enter IP address: ")
domain_name = input("Enter domain name: ")

# Define the dig commands to run
commands = [
    f"dig {domain_name} A +short",
    f"dig {domain_name} TXT +short",
    f"dig {domain_name} ANY +short",
    f"dig {domain_name} NS +short",
    f"dig -x {ip_address} +short",
    f"dig {domain_name} MX +short",
    f"dnsenum --dnsserver {ip_address} --enum -p 0 -s 0 -o subdomains.txt -f /usr/share/wordlists/seclists/Discovery/DNS/fierce-hostlist.txt {domain_name} --threads 90"
]

# Run the dig commands and dnsenum and print the output
for command in commands:
    output = subprocess.run(command.split(), stdout=subprocess.PIPE)
    print(output.stdout.decode())

# Read in the subdomains discovered by dnsenum
with open('subdomains.txt') as f:
    subdomains = f.read().splitlines()

# If any subdomains were found, run dnsenum on each of them
if subdomains:
    print(f"Discovered {len(subdomains)} subdomains:")
    for subdomain in subdomains:
        subdomain = subdomain.strip()
        print(f"Running dnsenum on {subdomain}")
        command = f"dnsenum --dnsserver {ip_address} --enum -p 0 -s 0 -o subdomains_{subdomain}.txt -f /usr/share/wordlists/seclists/Discovery/DNS/fierce-hostlist.txt {subdomain} --threads 90"
        output = subprocess.run(command.split(), stdout=subprocess.PIPE)
        print(output.stdout.decode())
else:
    print("No subdomains discovered.")

# Construct the zone transfer command
zone_transfer_command = f"dig axfr {domain_name} @{ip_address}"

# Run the zone transfer command
print(f"Running zone transfer on {domain_name}")
output = subprocess.run(zone_transfer_command.split(), stdout=subprocess.PIPE)
print(output.stdout.decode())

# If any subdomains were found, run zone transfer on each of them
if subdomains:
    for subdomain in subdomains:
        subdomain = subdomain.strip()
        subdomain_name = f"{subdomain}.{domain_name}"
        subdomain_zone_transfer_command = f"dig axfr {subdomain_name} @{ip_address}"
        print(f"Running zone transfer on {subdomain_name}")
        output = subprocess.run(subdomain_zone_transfer_command.split(), stdout=subprocess.PIPE)
        print(output.stdout.decode())
