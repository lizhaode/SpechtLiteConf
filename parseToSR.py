if __name__ == '__main__':
    tmp = []
    with open('ipReject.txt') as f:
        for i in f.readlines():
            i = i.strip('\n')
            final = 'IP-CIDR,{ip},REJECT\n'.format(ip=i)
            tmp.append(final)
    with open('reject.conf','w') as f:
        f.writelines(tmp)
