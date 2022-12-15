# 用途
用于实施切换Wwise音频总线的效果

# 适用范围
适用于所有使用Mastering Suite的Wwise音频方案

# 准备
[] Wwise已集成至Unreal引擎

[] Wwise工程需要具有Mastering Suite权限

[] Wwise工程File_ImportFactoryAsset..._MasteringSuite

[] 将Mastering Suite预设的Work Unit显式地导入至SoundBank

[] 点击User Setting，勾选生成头文件，即Wwise_IDS.h,用于获取以下函数所需的参数

  - AudioDevice “System" = 3859886410U(如命名不同则需要另行生成上述头文件获取AudioDeviceID，或使用）
  - Mastering Suite ShareSetID
    - Off = 930712164U (设为Default Preset）
    - TV = 1568083719U
    - HomeCinema = 1568083719U
    - HeadPhones = 880395932U
    - SoundBar = 1396549701U
    - NightMode = 2444352864U
  - in_uFXIndex即效果器插槽下标，因Mastering Suite默认位于AudioDevice_Effect的最后一个插槽，即in_uFXIndex=3
目前所有 AK::SoundEngine 调用均通过 AudioDevice实现，且必须在 AkAudio模块内实现，必须在AkAudio模块内扩展功能，以便暴露所需的Wwise功能。

[] UE C++工程

[] AkAudio.Build.cs，167行后加入该效果器的名称  "MasteringSuiteFX"【如下】

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

# 使用方法
    AkAudio.Build.cs 位于%GameProjectName\Plugins\Wwise\Source\AkAudio\AkAudio.Build.cs

    cpp文件放置地址 %GameProjectName\Plugins\Wwise\Source\AkAudio\Private\SwitchBusFX.cpp

    header文件放置地址 %GameProjectName\Plugins\Wwise\Source\AkAudio\Public\AudioLab.h

    以C++工程运行Unreal编辑器，编译代码后，即可在蓝图Wwise|AudioDevice中使用该Wwise功能扩展