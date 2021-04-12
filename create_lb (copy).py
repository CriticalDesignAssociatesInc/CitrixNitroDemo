import json
import requests, sys, base64, collections
import urllib3
import getpass


#Disable SSL Warnings if cert is untrusted
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#variables
NITRO_SERVER= sys.args[0]
#NITRO_SERVER="192.168.99.19"
#User input username
NITRO_USER= sys.args[1]
#NITRO_USER="nsroot"
#User input password
try:
    NITRO_PWD = sys.args[2]
except Exception as error:
    print('ERROR', error)
#NITRO_PWD="nsroot"
app_name = sys.args[3]
app_port = sys.args[4]
lb_serviceType = sys.args[5]
lb_IPadd = sys.args[6]

lb_name = "VS-LB-PRI-" + app_name + "-" + app_port
svg_name = "SVG-PRI-" + app_name + "-" + app_port
print(lb_name)
print(svg_name)

headers = {
"X-NITRO-USER":NITRO_USER,
"X-NITRO-PASS":NITRO_PWD,
"Content-Type": "application/json"
}


def create_lb():


    type(int(app_port))


    payload = {
    "lbvserver": 
    {
    "name":lb_name,
    "servicetype":lb_serviceType,
    "ipv46":lb_IPadd,
    "port":app_port
    } 
    }

    lbvs_response = requests.post(url="https://%s/nitro/v1/config/lbvserver"%(NITRO_SERVER),headers=headers,data=json.dumps(payload),verify=False)
    print(lbvs_response)
    print(lbvs_response.content)

def create_svg():



    payload= {
    "servicegroup": 
    {
    "servicegroupname":svg_name,
    "servicetype":svg_type
    } 
    }
    svg_resp=requests.post(url="https://%s/nitro/v1/config/servicegroup"%(NITRO_SERVER),headers=headers,data=json.dumps(payload),verify=False)
    print(svg_resp)
    print(svg_resp.content)
    
    print(lb_name)
    if lb_name:
        bind_svg= {
        "lbvserver_servicegroup_binding":
        {
        "name":lb_name,
        "servicegroupname":svg_name
        }
        }
        svg_bind_resp=requests.post(url="https://%s/nitro/v1/config/lbvserver_servicegroup_binding"%(NITRO_SERVER),headers=headers,data=json.dumps(bind_svg),verify=False)
        print(svg_bind_resp)
        print(svg_bind_resp.content)
        return(svg_name)

def create_servers():


    payload = {
    "server": 
    {
    "name":server_name,
    "ipaddress":server_ip
    } 
    }
    server_resp=requests.post(url="https://%s/nitro/v1/config/server"%(NITRO_SERVER),headers=headers,data=json.dumps(payload),verify=False)
    print(server_resp)
    print(server_resp.content)
    
    print(svg_name)
    if svg_name:
        bind_server={
        "servicegroup_servicegroupmember_binding":
        {
        "servicegroupname":svg_name,
        "port":server_port,
        "servername":server_name
        }
        }
        
        server_bind_resp=requests.post(url="https://%s/nitro/v1/config/servicegroup_servicegroupmember_binding"%(NITRO_SERVER),headers=headers,data=json.dumps(bind_server),verify=False)
        print(server_bind_resp)
        print(server_bind_resp.content)



if __name__=="__main__":

    create_lb()
    svg_type = sys.args[7]
    create_svg()
    
#    while True:
#        a = input("Add Backend Server? (y/n) ").lower()
#        if a == "y":
    server_name = sys.args[8]
    server_ip = sys.args[9]
    server_port = sys.args[10]
    create_servers()
#        elif a == "n":
#            break
#        else:
#            print("Enter y/n")