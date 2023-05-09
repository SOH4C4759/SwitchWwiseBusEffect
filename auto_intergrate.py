# -*- coding: utf-8 -*-

# region Import
from waapi import connect, CannotConnectToWaapiException
from P4 import P4, P4Exception
import sys

# endregion

# region WwiseConnection
url = None
try:
    client = connect(url)
except CannotConnectToWaapiException as e:
    print(e)
    exit()
# endregion

# region P4 Instances
p4 = P4()
# endregion

# region Initialize
_info_ = client.call("ak.wwise.core.getInfo")
_projInfo_ = client.call("ak.wwise.core.getProjectInfo")

__console__ = _info_['directories']['bin'] + 'WwiseConsole.exe'
__wwise_version__ = _info_['version']['year']
__masteringSuit_factory__ = ['Headphones', 'HomeCinema', 'NightMode', 'Off', 'SoundBar', 'TV']


# endregion

# Define Functions
def check_presets_exist() -> bool:
    """检测当前Wwise工程是否包含 MasteringSuite 原厂预设"""
    for i in __masteringSuit_factory__:
        args = {
            "waql": f"from type Effect where name = \"{i}\""
        }
        res = client.call("ak.wwise.core.object.get", **args)['return']

        print(f"MasteringSuite Preset：{res[0]['name']}")

        if res != []:  # 不可简化
            pass
        else:
            print("Mastering Suite 官方预设不完整，请重新导入")
            return False
    return True


def import_p4_args() -> bool:
    """输入Perforce账号"""
    p4.port = input("请输入p4的Port：")
    p4.user = input("请输入p4的User：")
    p4.client = input("请输入p4的Client：")
    p4.password = input("请输入p4的PassWord：")
    try:
        p4.connect()
        info = p4.run("info")
        p4.run_sync()  # 拉新
        print("Perforce 连接成功")
        return True
    except P4Exception as e:
        print(e)
        return False


def insert_effect_to_object():
    """通过Waapi向工程中添加效果器 in_uFXIndex即效果器插槽下标，因Mastering Suite默认位于AudioDevice_Effect的最后一个插槽，in_uFXIndex=3"""
    args = {
        "objects": [
            {
                "object": "\\Audio Devices\\Default Work Unit\\System",
                "@Effect3": {
                    "type": "Effect",
                    "name": "Off",
                    "classId": 12189699
                }
            }
        ]
    }
    res = client.call("ak.wwise.core.object.set", **args)
    if res:
        print(f"效果器MasteringSuite添加成功 \n {res}")
        return True
    else:
        return False

# endregion
# TODO 将MasteringSuite 原厂预设显式地加入到Init.bnk的Inclusion中 # FIXME MasteringSuite No License
# TODO 自动生成Init.bnk,并且生成生成头文件，即Wwise_IDS.h,用于获取以下函数所需的参数
# TODO 关闭Wwise工程
# TODO 链接Perforce，迁出改动至changelist
# TODO 通过python获取当前UE工程的路径

"""```python
import unreal

# 获取当前活动的编辑器窗口
editor_util = unreal.EditorUtilityLibrary()
editor_window = editor_util.get_active_editor_window()

# 获取当前工程的路径
if editor_window:
    current_world = editor_window.get_current_world()
    if current_world:
        project_file_path = current_world.get_map_file_path()
        project_dir = unreal.Paths.get_path(project_file_path)
        print("当前工程路径：", project_dir)
```

这段代码使用了`unreal`模块中的`EditorUtilityLibrary`和`Paths`类来获取当前工程的路径。`get_active_editor_window()`可以获取当前活动的编辑器窗口，`get_current_world()`可以获取当前编辑器窗口中的世界，`get_map_file_path()`可以获取当前世界对应的地图文件路径。最后，使用`get_path()`方法从地图文件路径中提取出工程路径。"""

# TODO 验证UE是否有Wwise集成
# TODO 获取当前运行地址，将source下的文件分别拷贝至UE工程下
# TODO cpp文件放置地址 %GameProjectName\Plugins\Wwise\Source\AkAudio\Private\
# TODO header文件放置地址 %GameProjectName\Plugins\Wwise\Source\AkAudio\Public\SwitchBusFX.h
# TODO 编辑文件AkAudio.Build.cs 位于%GameProjectName\Plugins\Wwise\Source\AkAudio\AkAudio.Build.cs
# TODO 执行UE的代码编译
# TODO 提交UE改动至版本管理
# 编辑内容如下：
"""
AkAudio.Build.cs，167行后加入该效果器的名称  "MasteringSuiteFX"【如下】

    public class AkAudio : ModuleRules
    {
            private static AkUEPlatform AkUEPlatformInstance;
            private List<string> AkLibs = new List<string> 
            {
                    "AkSoundEngine",
                    "AkMemoryMgr",
                    "AkStreamMgr",
                    "AkMusicEngine",
                    "AkSpatialAudio",
                    "AkAudioInputSource",
                    "AkVorbisDecoder",
                    "AkMeterFX", // AkMeter does not have a dedicated DLL
                    "MasteringSuiteFX",
            };
"""
