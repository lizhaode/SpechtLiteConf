# 个人自定义的配置文件 for [SpechtLite](https://github.com/zhuhaow/SpechtLite)

这个项目是学习了 [geekpi/SpechtLiteConf](https://github.com/geekpi/SpechtLiteConf)  方法，感谢原作者！

***
~~本人自己使用 ShadowSocks-libev ，通过SpechtLite转发来实现自动分流和屏蔽广告的效果~~

`使用中发现规则文件太多，会稍微影响网络性能，所以去掉了屏蔽广告，也大幅度减少了代理规则`

目前从 ShadowSocks-libev 切换到 V2ray，所以使用方法上有一些区别
***

## 首次使用

- 从 Github 上下载运行 SpechtLite
- 通过Homebrew安装 V2ray
- 根据实际情况修改 v2ray.json和plist
- 执行runFirst.sh脚本

这样每次开机都会自动运行 V2ray，并且通过SpechtLite实现分流代理的效果

## 说明

在没有特殊情况下，这个项目不会更新了  
因为 SpechtLite 作者目前不再更新软件，并且目前的代理规则已经足矣满足大部分的需要了，如果有特殊情况可以自行更新规则或者直接使用 `全局代理` 模式