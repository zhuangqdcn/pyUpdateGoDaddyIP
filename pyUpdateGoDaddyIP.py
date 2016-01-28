#!/usr/bin/env python
import urllib
import GoDaddyAPIs
import sys
import logging

__author__ = "Yuan Zhuang"
__version__ = "1.0.0"
__email__ = "zhuangqdcn@hotmail.com"

logger = logging.getLogger("Auto update GoDaddy IP")
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

try:
    domain = sys.argv[1]
    try:
        subdomain = sys.argv[2]
    except:
        subdomain = sys.argv[1].split('.', 1)[0]
        domain = sys.argv[1].split('.', 1)[1]
except:
    subdomain = "your_subdomain"
    domain = "your_domain.com"
    logger.error("no input domains, use default one")
logger.info("domain is:"+domain)
logger.info("subdomain is:"+subdomain)

try:
    myip = sys.argv[3]
    logger.info("Have input ip, will not detected ip automatically.")
except:
    myip = urllib.urlopen("http://myip.dnsdynamic.org/").read()
    logger.info("External IP is " + myip)

api_key = "your_api_key"
api_secret = "your_api_secret"

godaddy = GoDaddyAPIs.GoDaddyAPIs(api_key, api_secret)
# check if is the same
old_ip = godaddy.get_domain_record(domain, 'A', subdomain)[0]['data']
print old_ip
if  old_ip != myip:
    response = godaddy.set_subdomain_ip(myip, domain, subdomain)
    if len(response)==0:
        logger.info(" ".join(["Successful updated", subdomain+"."+domain+"'s", "as", myip]))
    else:
        logger.warning(" ".join(["Fail updated", subdomain+"."+domain+"'s", "as", myip]))
        logger.info(response)
else:
    logger.info("No changes in IP, do not need change.")
