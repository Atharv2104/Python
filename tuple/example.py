
server_ip = ("192", "168", "1", "10")   
allowed_ips = ["192.168.1.5"]          

def update_allowed_ips(new_ip):
   
    if new_ip not in allowed_ips:
        allowed_ips.append(new_ip)
        print(f"IP {new_ip} added to allowed list.")
    else:
        print(f"IP {new_ip} is already in allowed list.")

def display_config():

    print("\n Web Server Configuration ")
    print(f"Server IP: {server_ip}")
    print(f"Allowed IPs: {allowed_ips}")
    

display_config()


update_allowed_ips("192.168.1.6")
update_allowed_ips("192.168.1.7")


try:
    server_ip = ("10", "0", "0", "1")  
    print("Server IP changed!")     
except TypeError:
    print("Cannot change server_ip!")

display_config()
