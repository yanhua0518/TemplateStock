#《Summer Pockets REFLECTION BLUE手机版焊接补丁》

补丁说明：
 * 本补丁基于枫笛汉化版制作，感谢《枫笛汉化组》的努力付出以及复制粘贴苦力们的辛勤劳动。
 * 本补丁仅为快速复制粘贴，不保证内容完整性，未汉化界面和图片。
 * 本补丁翻译内容归《枫笛汉化组》所有，严禁用于任何商业用途。

使用方法：
___EXTEND_SummerPockets为原来的无印焊接补丁；

___EXTEND_SummerPockets_rb是RB焊接补丁。

安卓系统直接将文件复制到对应位置替换即可。

注意：
 * 需要先正常下载完游戏数据后再替换！
 * 安卓RB只替换Scene.pck一个文件，另外两个是给iOS用的，不要替换！

越狱iOS系统将安卓___EXTEND_SummerPockets_rb数据包和RB焊接补丁复制到：

app文件共享\Documents\___EXTEND_SummerPockets


未越狱iOS启动RB并汉化的方法：

在梯子（一般都是小火箭）的配置文件中添加“URL重写”：

^http://cdn.anigema.jp/anigema/gamedata/agp0154.kn.summerpockets.contents.ios/(.*) http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.rb/$1 302

启动游戏下载数据，游戏就变成SPRB的内容了。

注意：
 * 此操作无法恢复！而且会增加3GB以上的空间占用！
 * 目前iOS无法解锁RB新增四线内容！
 * 想要恢复必须删除app（卸载app不行）重装，会丢失存档！

数据下载完成后，删除上面的配置，添加以下配置：

http://cdn.anigema.jp/anigema/gamedata/agp0154.kn.summerpockets.contents.ios/___DL.json https://od.lk/d/NzZfNzY5ODk2NDhf/___DL.json 302

http://cdn.anigema.jp/anigema/gamedata/agp0154.kn.summerpockets.contents.ios/Scene.pck https://od.lk/d/NzZfNzY5ODk2NDlf/Scene.pck 302

http://cdn.anigema.jp/anigema/gamedata/agp0154.kn.summerpockets.contents.ios/Scene.pck.hash https://od.lk/d/NzZfNzY5ODk2NTBf/Scene.pck.hash 302

重新启动游戏下载数据。

如果以上方法无法成功下载数据，可以在电脑上安装Fiddler。

Tools-Options-Connections：

勾选Allow remote computers to connect

然后在主窗口右侧找到AutoResponder标签，

勾选Enable rules和Unmatched requests passthrough。

然后Add Rule，添加：

EXACT:http://cdn.anigema.jp/anigema/gamedata/agp0154.kn.summerpockets.contents.ios/___DL.json

EXACT:http://cdn.anigema.jp/anigema/gamedata/agp0154.kn.summerpockets.contents.ios/Scene.pck

EXACT:http://cdn.anigema.jp/anigema/gamedata/agp0154.kn.summerpockets.contents.ios/Scene.pck.hash

三个并分别指向你解压出来的对应的本地文件，然后save。

手机进入设置-无线局域网，点击你连接的wifi右侧的i

配置代理-手动

服务器：你电脑的IP地址

端口：8888

然后断开梯子，重启游戏下载数据。

注意：
 * 此方法要求每次启动游戏都要电脑开启Fiddler。此情况下手机可能无法正常上网。
 * 可以在使用此方法成功下载数据之后，把配置代理改回关闭。然后重新在梯子里配置前面一种方法：
 
http://cdn.anigema.jp/anigema/gamedata/agp0154.kn.summerpockets.contents.ios/___DL.json https://od.lk/d/NzZfNzY5ODk2NDhf/___DL.json 302

仅添加这一条配置。之后只要启动游戏的时候挂着梯子就行了。
