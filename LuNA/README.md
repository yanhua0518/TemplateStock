# 《LUNARiA -Virtualized Moonchild- 手机版汉化补丁》

## 补丁说明：
 * 本补丁由【夏日纯臻汉化组】制作，所有剧情汉化，游戏界面未汉化。  
 * 本补丁仅安卓和越狱iOS可用，未越狱iOS请自行想办法解决。
 * 本补丁的翻译内容归汉化组所有，仅供试用，不提供任何破解内容，请支持正版游戏。  
 * 严禁将本补丁用于商业用途，若因此触犯法律，本组不承担任何责任。  

## 使用方法：
### 安卓11以下
将Scene.pck、__g00_patch_001.pck复制到“Android\data\jp.co.product.kn.lunaria\files\”内替换。  
### 安卓11及以上
使用 MT文件管理器、ZArchiver 等支持[SAF](https://developer.android.com/guide/topics/providers/document-provider?hl=zh-cn) api的文件管理器将Scene.pck、__g00_patch_001.pck复制到“Android\data\jp.co.product.kn.lunaria\files\”替换。  

### 越狱iOS
将Scene.pck、__g00_patch_001.pck复制到“程序(用户)\LUNARiA\kn0020_kn_LUNARiA.app\”内替换。  

**注意：**
 * 安卓需要先正常下载完游戏数据后再替换！  
 * 只替换这两个文件，其他文件是给未root安卓用的，不要替换！  

## 未越狱IOS或无法访问Android\data的安卓
在支持URl重写的工具中添加“URL重写”：  
```
http://cdn.anigema.jp/anigema/gamedata/agp0178.kn.lunaria/___DL.json https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/LuNA/___DL.json 302  
http://cdn.anigema.jp/anigema/gamedata/agp0178.kn.lunaria/dat/Scene.pck https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/LuNA/Scene.pck 302  
http://cdn.anigema.jp/anigema/gamedata/agp0178.kn.lunaria/dat/__g00_patch_001.pck https://raw.githubusercontent.com/yanhua0518/TemplateStock/master/LuNA/__g00_patch_001.pck 302  
```

之后启动游戏下载数据。  
**注意：**
 * 使用此方法，每次启动游戏时都需要URL重写，否则会恢复为原版。  
