# 个人自定义的配置文件 for [SpechtLite](https://github.com/zhuhaow/SpechtLite)

这个项目是从  [geekpi/SpechtLiteConf](https://github.com/geekpi/SpechtLiteConf)  fork 来的，感谢原作者！

## List Explaination

- **gfwlist**: proxy list gnerate from [gfwlist](https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt)

- **whitelist**: white list generate from [dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list)

- **rejectlist**: reject list from [BurpSuite](https://raw.githubusercontent.com/BurpSuite/CloudGate-RuleList/master/Rule/REJECT)

## 使用方法

每次重新安装系统后，只需要将本项目 `git clone` 到 *Documents* 目录下，然后运行 `runFirst.sh`  脚本即可

## 更新脚本

- 在使用过程中，发现 GFWlist 过于庞杂，有太多的内容并不需要，所以改成在 [Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules) 项目中的 [手工规则](https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_adb.conf) 的基础上，加入手动维护一部分内容

- 提取其中 过滤广告IP 这部分的内容
- 走代理的域名，是在其基础上，手动加入了一些内容