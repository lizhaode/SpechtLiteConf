# 重装系统后，首次执行的脚本

mkdir -p ~/.SpechtLite

echo "开始设置更新 gfwlist 定时任务"

cp ./com.lizhao.update.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.lizhao.update.plist

echo "开始更新 gfwlist"
launchctl start com.lizhao.update
cp -R ./conf/* ~/.SpechtLite/

echo "请重新加载配置文件"