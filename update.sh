# 更新配置文件
echo "更新规则"
add=$(which python3)
${add} getRules.py

sleep 10

echo "拷贝文件"
cp ./conf/domainProxy.txt ~/.SpechtLite/
cp ./conf/domainReject.txt ~/.SpechtLite/
cp ./conf/ipProxy.txt ~/.SpechtLite/
cp ./conf/ipReject.txt ~/.SpechtLite/

echo "完成"