# TODO 链接Waapi,不会2022以前版本进行兼容
# TODO 输入Perforce账号
# TODO 检测当前Wwise工程是否包含 MasteringSuite 原厂预设
# TODO 通过Waapi向工程中添加效果器 in_uFXIndex即效果器插槽下标，因Mastering Suite默认位于AudioDevice_Effect的最后一个插槽，即in_uFXIndex=3
# TODO 将MasteringSuite 原厂预设显式地加入到Init.bnk的Inclusion中
# TODO 自动生成Init.bnk,并且生成生成头文件，即Wwise_IDS.h,用于获取以下函数所需的参数
# TODO 关闭Wwise工程
# TODO 链接Perforce，迁出改动至changelist
# TODO 通过python获取当前UE工程的路径
# TODO 验证UE是否有Wwise集成
# TODO 获取当前运行地址，将source下的文件分别拷贝至UE工程下
# TODO cpp文件放置地址 %GameProjectName\Plugins\Wwise\Source\AkAudio\Private\
# TODO header文件放置地址 %GameProjectName\Plugins\Wwise\Source\AkAudio\Public\SwitchBusFX.h
# TODO 编辑文件AkAudio.Build.cs 位于%GameProjectName\Plugins\Wwise\Source\AkAudio\AkAudio.Build.cs
# TODO 执行UE的代码编译
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

