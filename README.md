# 《Summer Pockets REFLECTION BLUE手机版汉化补丁》

## 补丁说明：
 * 本补丁由【夏日纯臻汉化组】制作，翻译内容归汉化组所有。  
 * 本补丁仅供试用，不提供任何破解内容，请支持正版游戏。  
 * 严禁将本补丁用于商业用途，若因此触犯法律，本组不承担任何责任。  

## 使用方法：
### 安卓
直接将Scene.pck复制到___EXTEND_SummerPockets_rb替换即可。  
### 越狱iOS
将Scene.pck复制到：  
app文件共享\Documents\___EXTEND_SummerPockets_rb  
**注意：**
 * 需要先正常下载完游戏数据后再替换！  
 * 只替换Scene.pck一个文件，其他文件是给未越狱iOS用的，不要替换！  
#### 反和谐
直接把安卓数据包内的__g00_patch_002.pck替换到iOS数据包里即可  

## 未越狱iOS双语+反和谐：
### 方法1
下载数据前，在梯子（一般都是小火箭）的配置文件中添加“URL重写”：  
http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.ios.rb/___DL.json https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/___DL.json 302  
http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.ios.rb/Scene.pck https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/Scene.pck 302  
http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.ios.rb/Scene.pck.hash https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/Scene.pck.hash 302  
^http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.ios.rb/(.*) http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.rb/$1 302  
之后启动游戏下载数据。  
**注意：**
 * 使用此方法，每次启动游戏时需要断网或连着梯子，否则会恢复为原版。   
### 方法2
下载数据前，在梯子的配置文件中添加“URL重写”：
http://cdn.anigema.jp/anigema/gamedata/agp0154.kn.summerpockets.contents.ios/___DL.json https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/___DLorg.json 302  
http://cdn.anigema.jp/anigema/gamedata/agp0154.kn.summerpockets.contents.ios/Scene.pck https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/SceneOrg.pck 302  
http://cdn.anigema.jp/anigema/gamedata/agp0154.kn.summerpockets.contents.ios/Scene.pck.hash https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/SceneOrg.pck.hash 302  
http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.rb/___DLorg.json https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/___DL.json 302  
http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.rb/Scene.pck https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/Scene.pck 302  
http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.rb/Scene.pck.hash https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/Scene.pck.hash 302  
http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.rb/Scene.pck https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/__dat_patch_000.pck 302  
http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.rb/Scene.pck.hash https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/__dat_patch_000.pck.hash 302  
之后启动游戏下载数据。  
**注意：**
 * 使用此方法后，不需要每次启动游戏断网或连梯子。但此操作不可逆！  
 * 若想恢复只能删除app（卸载app无效）重新下载。  

## Shadowrocket（小火箭）添加URL重写的方法：
打开小火箭，点下面“配置”  
点击本地文件中打着√的配置文件（一般是default.conf），选编辑纯文本。  
拉到最下面，看到[URL Rewrite]部分，  
把要添加的配置整体复制下来，粘贴到后面。然后点保存。  
