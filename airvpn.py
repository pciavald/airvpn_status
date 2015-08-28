import urllib2
import json
import sys

# check for API key
if (len(sys.argv) != 2):
    print "usage: python airvpn.py apikey"
    sys.exit(1)

# request API service
def request(service, apikey):
    protocol = "json"

    url = "https://airvpn.org/api/?format=" + protocol + "&key=" + apikey + "&service=" + service
    req = urllib2.urlopen(url).read()
    info = json.loads(req)
    return (info)


info = request("userinfo", sys.argv[1])

# display public ip if not connected
if info['user']['connected'] == False:
    ip = urllib2.urlopen('http://ip.42.pl/raw').read()
    print "Public (" + ip + ")"
    sys.exit(0)

# gather state of connection
servername = info['connection']['server_name']
country = info['connection']['server_country_code']
ip = info['connection']['exit_ip']
days = str(info['user']['expiration_days'])

# request specifics about server
info = request("status", sys.argv[1])
for server in info['servers']:
    if server['public_name'] == servername:
        break
bw = str(server['bw'])
bw_max = str(server['bw_max'])

# construct line
line = servername + "_" + country + " (" + ip + ") [" + bw + "/" + bw_max + "] [" + days + "]"
print line
