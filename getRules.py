import requests
import io


class newRules(object):
    def getRulesIo(self,originalUrl):
        # originalUrl = 'https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_top500_whitelist_ad.conf'
        # originalUrl = 'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/banAD.acl'
        originalText = requests.get(originalUrl).text
        return originalText

    def getdomainRejectRules(self,originalRules):
        originalRules = io.StringIO(originalRules)
        rejectList = []
        for i in originalRules.readlines():
            if i.startswith('DOMAIN-SUFFIX') and i.endswith('Reject\n'):
                rejectList.append('(^|.)' + i.split(',')[1] + '$\n')

        return rejectList

    def getdomainSuffixRejectRules(self, originalRules):
        originalRules = io.StringIO(originalRules)
        rejectList = []
        for i in originalRules.readlines():
            if i.startswith('DOMAIN') and i.endswith('Reject\n'):
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
            if i.startswith('DOMAIN-SUFFIX') and i.endswith('PROXY\n'):
                proxyList.append(i.split(',')[1] + '$\n')

        tmp = io.StringIO(originalRules)
        for i in tmp.readlines():
            if i.startswith('DOMAIN-KEYWORD') and i.endswith('PROXY\n'):
                proxyList.append(i.split(',')[1] + '\n')

        return proxyList

    def addRegex(self,originalList):
        regexList = []
        for i in originalList:
            splitList = i.split('.')
            tmp = '\.'.join(splitList)
            regexList.append(tmp)

        return regexList

    def getUseText(self, oriText):
        startIndex = oriText.index('# 广告关键词')
        endIndex = oriText.index('# 直连列表')
        return oriText[startIndex:endIndex]

    def getDomainFromRegex(self, oriText):
        tmp = io.StringIO(oriText)
        domainList = []
        for i in tmp:
            if i.startswith('('):
                domainList.append(i.replace('\r\n','\n'))

        return domainList

    def getIPFromRegex(self, oriText):
        tmp = io.StringIO(oriText)
        ipList = []
        for i in tmp:
            if '/' in i:
                ipList.append(i.replace('\r\n','\n'))

        return ipList

if __name__ == '__main__':
    
    oriRules = newRules().getRulesIo('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/banAD.acl')
    useText = newRules().getUseText(oriRules)
    # 获取 domainReject 的内容
    domainReject = newRules().getDomainFromRegex(useText)
    with open('domainReject.txt','w') as f:
        f.writelines(domainReject)
    # 获取 ipReject 的内容
    ipReject = newRules().getIPFromRegex(useText)
    with open('ipReject.txt','w') as f:
        f.writelines(ipReject)

    # completeIpRejectRules = newRules().getIpRejectRules(oriRules)
    # with open('conf/ipReject.txt','w') as f:
    #     f.writelines(completeIpRejectRules)

    # oriRules = newRules().getRulesIo('http://67.218.153.234:8080/file/myconf.conf')

    # proxy = newRules().getProxyRules(oriRules)
    # completeProxyRules = newRules().addRegex(proxy)
    # with open('conf/domainProxy.txt','w') as f:
    #     f.writelines(completeProxyRules)
