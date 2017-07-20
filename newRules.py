import requests
import io


class newRules(object):
    def getRulesIo(self,originalUrl):
        # 获取白名单，用 io 库读取成文件类型数据，便于处理
        # originalUrl = 'https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_top500_whitelist_ad.conf'
        # originalUrl = 'http://67.218.153.234:8080/file/myconf.conf'
        originalText = requests.get(originalUrl).text
        return originalText

    def getRejectRules(self,originalRules):
        originalRules = io.StringIO(originalRules)
        rejectList = []
        for i in originalRules.readlines():
            if i.startswith('DOMAIN-SUFFIX') and i.endswith('Reject\n'):
                rejectList.append('^' + i.split(',')[1] + '$\n')

        return rejectList

    def getIpRejectRules(self,originalRules):
        originalRules = io.StringIO(originalRules)
        ipRejectList = []
        for i in originalRules.readlines():
            if i.startswith('IP-CIDR') and i.endswith('Reject\n'):
                ipRejectList.append(i.split(',')[1] + '\n')

        return ipRejectList

    def getProxyRules(self,originalRules):
        tmp = io.StringIO(originalRules)
        proxyList = []
        for i in tmp.readlines():
            if i.startswith('DOMAIN-SUFFIX') and i.endswith('Proxy\n'):
                proxyList.append(i.split(',')[1] + '$\n')

        tmp = io.StringIO(originalRules)
        for i in tmp.readlines():
            if i.startswith('DOMAIN-KEYWORD') and i.endswith('Proxy\n'):
                proxyList.append(i.split(',')[1] + '\n')

        return proxyList

    def addRegex(self,originalList):
        regexList = []
        for i in originalList:
            splitList = i.split('.')
            tmp = '\.'.join(splitList)
            regexList.append(tmp)

        return regexList


if __name__ == '__main__':
    oriRules = newRules().getRulesIo('https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_top500_whitelist_ad.conf')

    # reject = newRules().getRejectRules(oriRules)
    # completeRejectRules = newRules().addRegex(reject)
    # with open('conf/domainReject.txt','w') as f:
    #     f.writelines(completeRejectRules)

    completeIpRejectRules = newRules().getIpRejectRules(oriRules)
    with open('conf/ipReject.txt','w') as f:
        f.writelines(completeIpRejectRules)

    oriRules = newRules().getRulesIo('http://67.218.153.234:8080/file/myconf.conf')

    proxy = newRules().getProxyRules(oriRules)
    completeProxyRules = newRules().addRegex(proxy)
    with open('conf/domainProxy.txt','w') as f:
        f.writelines(completeProxyRules)
