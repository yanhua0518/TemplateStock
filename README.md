# 《Summer Pockets REFLECTION BLUE手机版焊接补丁》

## 补丁说明：
 * 本补丁基于枫笛汉化版制作，感谢《枫笛汉化组》的努力付出以及复制粘贴苦力们的辛勤劳动。  
 * 本补丁仅为快速复制粘贴，不保证内容完整性，未汉化界面和图片。  
 * 本补丁翻译内容归《枫笛汉化组》所有，严禁用于任何商业用途。  

## 使用方法：
### 安卓
直接将Scene.pck复制到___EXTEND_SummerPockets_rb替换即可。  

### 越狱iOS
将Scene.pck复制到：  
app文件共享\Documents\___EXTEND_SummerPockets_rb  

**注意：**
 * 需要先正常下载完游戏数据后再替换！  
 * 只替换Scene.pck一个文件，其他文件是给未越狱iOS用的，不要替换！  

## iOS反和谐：
### 越狱系统
直接把安卓数据包内的__g00_patch_002.pck替换到iOS数据包里即可  

### 未越狱系统
#### 方法1
下载数据前，在梯子（一般都是小火箭）的配置文件中添加“URL重写”：  
^http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.ios.rb/(.*) http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.rb/$1 302  
之后启动游戏下载数据。已经下载过数据也可以，启动游戏会提示重新下载500MB+的数据。  

**注意：**
 * 使用此方法后，每次启动游戏时需要断网或连着梯子，否则会让你重新下载和谐数据。  

#### 方法2
下载数据前，在梯子的配置文件中添加“URL重写”：
http://cdn.anigema.jp/anigema/gamedata/agp0154.kn.summerpockets.contents.ios/___DL.json https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/___DLorg.json 302  
http://cdn.anigema.jp/anigema/gamedata/agp0154.kn.summerpockets.contents.ios/Scene.pck https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/SceneOrg.pck 302  
http://cdn.anigema.jp/anigema/gamedata/agp0154.kn.summerpockets.contents.ios/Scene.pck.hash https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/SceneOrg.pck.hash 302  
之后启动游戏下载数据。  

**注意：**
 * 使用此方法后，不需要每次启动游戏断网或连梯子，但这意味着此操作不可逆！  
 * 若想恢复只能删除app（卸载app无效）重新下载。  
 
## 未越狱iOS汉化：
#### 方法1
在URL重写中添加以下配置：  
http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.ios.rb/___DL.json https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/___DL.json 302  
http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.ios.rb/Scene.pck https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/Scene.pck 302  
http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.ios.rb/Scene.pck.hash https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/Scene.pck.hash 302  
重新启动游戏下载数据。

**注意：**
 * 使用了反和谐方法2的情况下需要使用方法2进行补丁。  
 * 使用此方法，每次启动游戏时需要断网或连着梯子，否则会恢复为日文版。  

#### 方法2
在URL重写中添加以下配置：
http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.rb/___DLorg.json https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/___DL.json 302  
http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.rb/Scene.pck https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/Scene.pck 302  
http://cdn.anigema.jp/anigema/gamedata/agp0169.kn.summerpocketsrb.contents.ios.rb/Scene.pck.hash https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/Scene.pck.hash 302  
重新启动游戏下载数据。

**注意：**
 * 使用了反和谐方法2的情况需要使用此方法。此操作不可逆！  
 * 使用此方法后，不需要每次启动游戏断网或连梯子。  

