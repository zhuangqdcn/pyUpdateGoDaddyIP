from requests import Session

class GoDaddyAPIs:
    __author__ = "Yuan Zhuang"
    __version__ = "1.0.0"
    __email__ = "zhuangqdcn@hotmail.com"
    
    def __init__(self, api_key, api_secret, user_id=""):
        self.api_key = api_key
        self.api_secret = api_secret
        self.authorization_string = "sso-key " + self.api_key + ":" + self.api_secret
        self.url_base = "https://api.godaddy.com"
        self.user_id = user_id
        self.session = Session()
        self.session.head(self.url_base)

    def get_info(self, url_get):
        response = self.session.get(
            url = url_get, 
            data = {
                },
            headers = {
                "Authorization": self.authorization_string,
                "Accept": "application/json"
                }
            )
        return response.json()
        
    def get_domains(self):
        # @return an array of domains under the api key
        url_get = self.url_base + "/v1/domains"
        return self.get_info(url_get)

    def get_domain_info(self, domain):
        # @return a json of the info of the domain
        url_get = "/".join([self.url_base, "v1/domains", domain])
        return self.get_info(url_get)

    def get_domain_record(self, domain, record = "A", subdomain=""):
        # @return a json of the info of the record
        url_get = "/".join([self.url_base, "v1/domains", domain, "records", record])
        if len(subdomain)>0:
            url_get = "/".join([url_get, subdomain])
        return self.get_info(url_get)

    def set_subdomain_ip(self, ip, domain, subdomain="www", record = "A",  ttl = 3600):
        # @return if sucess, should return a empty json
        url_put = "/".join([self.url_base, "v1/domains", domain, "records", record, subdomain])
        response = self.session.put(
            url = url_put,
            data = {
                "data": ip
                },
            headers = {
                "Authorization": self.authorization_string,
                "Accept": "application/json"
                }
            )
        return response.json()
                       
