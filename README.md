# 个人自定义的配置文件 for [SpechtLite](https://github.com/zhuhaow/SpechtLite)

这个项目是学习了 [geekpi/SpechtLiteConf](https://github.com/geekpi/SpechtLiteConf)  方法，感谢原作者！

本人自己使用 ShadowSocks-libev ，通过SpechtLite转发来实现自动分流和屏蔽广告的效果

`使用中发现规则文件太多，会稍微影响网络性能，所以去掉了屏蔽广告，也大幅度减少了代理规则`

`并且也从 ShadowSocks-libev 切换到 V2ray 所以以下内容大部分作废了`

***

## 首次使用

- 从Github上下载运行SpechtLite
- 通过Homebrew安装ShadowSocks-libev和simple-obfs
- 根据实际情况修改local.json(ss运行的配置文件)和plist
- 执行runFirst.sh脚本

这样每次开机都会自动运行ss-libev，并且通过SpechtLite实现分流和屏蔽广告的效果

## 说明
目前暂时只通过更新conf文件夹中的配置文件来更新配置。等待找到更好的广告屏蔽源，抽时间修改自动化的脚本，实现定时更新
