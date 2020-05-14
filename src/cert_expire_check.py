#!/app/miniconda3/bin/python
##better run this in linxu, windows may not able to load dll
import datetime
import ssl
from OpenSSL import crypto as c

ssl_hosts={
    'www.bing.com':443
}

ssl_date_fmt = '%Y%m%d%H%M%SZ'

print('CertHost,Port,Expire Date,Expire in # Days')
for host,port in ssl_hosts.items():
    try:
        cert = ssl.get_server_certificate((host, port))
        x509 = c.load_certificate(c.FILETYPE_PEM,cert)
        x509.get_issuer()
        expirationDate = datetime.datetime.strptime(x509.get_notAfter().decode('ascii'),ssl_date_fmt)
        now = datetime.datetime.now()
        delta = expirationDate - now
        print(host+','+str(port)+','+datetime.datetime.strftime(expirationDate,'%Y%m%d %H:%M:%S GMT')+','+str(delta.days))
    except Exception as e:
        print(host+','+str(port)+',ERROR!'+str(e)+',0')
