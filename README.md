# pyUpdateGoDaddyIP

## Features

 * Update GoDaddy's subdomain DNS "A" record according to the local machine's external IP (A cheap alternative of DDNS once you have a GoDaddy domain.).



## Prerequisite

##### [Python 2.7](https://www.python.org/download/releases/2.7/)

##### urllib
```bash
pip install urllib
```
##### requests
```bash
pip install requests
```
##### [GoDaddy API key and secret](https://developer.godaddy.com/)

##### Valid network connection.

## Usage
##### Change this two lines according to your API key and secret in pyUpdateGoDaddyIP.py file:
```python
api_key = "your_api_key"
api_secret = "your_api_secret"
```
##### Run in command by using
```bash
pyUpdateGoDaddyIP.py subdomain.domain.com
```
##### or

```bash
pyUpdateGoDaddyIP.py domain.com subdomain
```
##### or a specific IP
```bash
pyUpdateGoDaddyIP.py  domain.com subdomain 111.111.111.111
```
##### or running without any input parameters
changing these two lines to your domain and subdomain in pyUpdateGoDaddyIP.py file:
```python
subdomain = "your_subdomain"
domain = "your_domain.com"
```
then it will take no input parameters to run.

## Version
1.0.0

## Lisence

GPLv3
