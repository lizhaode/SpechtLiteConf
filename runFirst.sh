# 重装系统后，首次执行的脚本

mkdir -p ~/.SpechtLite

cp ./com.lizhao.ss.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.lizhao.ss.plist

echo "拷贝配置文件"
cp -R ./conf/* ~/.SpechtLite/

echo "请重新加载配置文件"