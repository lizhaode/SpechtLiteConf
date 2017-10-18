
if __name__ == '__main__':
    tmp = []
    # 生成CIDR广告过滤
    # with open('ipReject.txt') as f:
    #     for i in f.readlines():
    #         i = i.strip('\n')
    #         final = 'IP-CIDR,{ip},REJECT\n'.format(ip=i)
    #         tmp.append(final)
    # with open('reject.conf','w') as f:
    #     f.writelines(tmp)

    # 生成域名代理
    # with open('domainProxy.txt') as f:
    #     for i in f.readlines():
    #         i = i.strip('\n')
    #         if i.endswith('$'):
    #             i = i.rstrip('$')
    #             i = i.replace('\\','')
    #             final = 'DOMAIN-SUFFIX,{domain},PROXY\n'.format(domain=i)
    #             tmp.append(final)
    #         else:
    #             final = 'DOMAIN-KEYWORD,{domain},PROXY\n'.format(domain=i)
    #             tmp.append(final)
    # with open('domain.conf','w') as f:
    #     f.writelines(tmp)
    
    # 生成CIDR代理
    with open('ipProxy.txt') as f:
        for i in f.readlines():
            i = i.strip('\n')
            if i == '':
                continue
            final = 'IP-CIDR,{ip},PROXY\n'.format(ip=i)
            tmp.append(final)

    with open('ip.conf','w') as f:
        f.writelines(tmp)
