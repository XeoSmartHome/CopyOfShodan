from ipwhois import IPWhois

obj = IPWhois('16.58.214.142')

res1 = obj.lookup_whois()

print(res1)

res2 = obj.lookup_rdap()

print(res2)
