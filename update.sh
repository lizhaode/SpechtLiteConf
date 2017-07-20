#! /bin/sh
#  执行更新gfwlist 脚本，然后拷贝更新的文件到 SpechtLite
echo "执行更新 gfwlist py脚本"

# 脚本执行环境设置
source ~/.bash_profile
cd ~/Documents/SpechtLiteConf

python newRules.py
echo "拷贝文件"
cp ./conf/domainProxy.txt /Users/lizhao/.SpechtLite
cp ./conf/ipProxy.txt /Users/lizhao/.SpechtLite
cp ./conf/ipReject.txt /Users/lizhao/.SpechtLite

echo "完成"