# 《LUNARiA -Virtualized Moonchild- 手机版汉化补丁》

## 补丁说明：
 * 本补丁由【夏日纯臻汉化组】制作，所有剧情汉化，游戏界面未汉化。  
 * 本补丁仅安卓和越狱iOS可用，未越狱iOS请自行想办法解决。
 * 本补丁的翻译内容归汉化组所有，仅供试用，不提供任何破解内容，请支持正版游戏。  
 * 严禁将本补丁用于商业用途，若因此触犯法律，本组不承担任何责任。  

## 使用方法：
### root安卓
将Scene.pck、__g00_patch_001.pck复制到“Android\data\jp.co.product.kn.lunaria\files\”内替换。  

### 越狱iOS
将Scene.pck、__g00_patch_001.pck复制到“程序(用户)\LUNARiA\kn0020_kn_LUNARiA.app\”内替换。  

**注意：**
 * 安卓需要先正常下载完游戏数据后再替换！  
 * 只替换这两个文件，其他文件是给未root安卓用的，不要替换！  

## 未root安卓：
在梯子（一般都是小火箭）的配置文件中添加“URL重写”：  

http://cdn.anigema.jp/anigema/gamedata/agp0178.kn.lunaria/___DL.json https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/LuNA/___DL.json 302  
http://cdn.anigema.jp/anigema/gamedata/agp0178.kn.lunaria/dat/Scene.pck https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/LuNA/Scene.pck 302  
http://cdn.anigema.jp/anigema/gamedata/agp0178.kn.lunaria/dat/__g00_patch_001.pck https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/LuNA/__g00_patch_001.pck 302  

之后启动游戏下载数据。  
**注意：**
 * 使用此方法，每次启动游戏时需要连着梯子，否则会恢复为原版。  

## Shadowrocket（小火箭）添加URL重写的方法：
打开小火箭，点下面“配置”  
点击本地文件中打着√的配置文件（一般是default.conf），选编辑纯文本。  
拉到最下面，看到[URL Rewrite]部分，  
把要添加的配置整体复制下来，粘贴到后面。然后点保存。  
