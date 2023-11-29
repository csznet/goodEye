# goodEye

监控指定程序打开后修改笔记本亮度，关闭后恢复亮度

使用场景：笔记本打游戏时需要高亮度，不打游戏时不需要高亮度

笔记本连接多块屏幕时也只修改指定屏幕（默认代码指定的为笔记本屏幕）

如果需要修改目标屏幕，则使用
```
print(sbc.list_monitors())
```
获取屏幕名称，然后修改源代码中的```monitors```值为屏幕名称
