url = input("url: ")

if 'www' in url:
    del_www = url.split('www.')
    b = ''.join(del_www)
    url_sp1 = b.split("/")
    print(url_sp1[2])
else:
    url_sp1 = url.split("/")
    print(url_sp1[2])


ur = url.split('//')[1]
ur = ur.replise('www.' '')
ur = ur.split('/')[0]
print(ur)
