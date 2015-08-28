import urllib2
import json

# request API service
def request(service, apikey):
    protocol = "json"
    url = "https://airvpn.org/api/?format=" + protocol + "&key=" + apikey + "&service=" + service
    req = urllib2.urlopen(url).read()
    info = json.loads(req)
    return (info)

def airvpn():

    apikey = str(open("airvpn_api.key", "r").read()).strip()
    info = request("userinfo", apikey)

    # display public ip if not connected
    if info['user']['connected'] == False:
        ip = urllib2.urlopen('http://ip.42.pl/raw').read()
        return "Public (" + ip + ")"

    # gather state of connection
    servername = info['connection']['server_name']
    country = info['connection']['server_country_code']
    ip = info['connection']['exit_ip']
    days = str(info['user']['expiration_days'])

    # request specifics about server
    info = request("status", apikey)
    for server in info['servers']:
        if server['public_name'] == servername:
            break
    bw = str(server['bw'])
    bw_max = str(server['bw_max'])

    # construct line
    line = servername + "_" + country + " (" + ip + ") [" + bw + "/" + bw_max + "] [" + days + "]"
    return (line)
