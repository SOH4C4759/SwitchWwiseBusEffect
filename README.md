# ��;
����ʵʩ�л�Wwise��Ƶ���ߵ�Ч��

# ���÷�Χ
����������ʹ��Mastering Suite��Wwise��Ƶ����

# ׼��
[] Wwise�Ѽ�����Unreal����

[] Wwise������Ҫ����Mastering SuiteȨ��

[] Wwise����File_ImportFactoryAsset..._MasteringSuite

[] ��Mastering SuiteԤ���Work Unit��ʽ�ص�����SoundBank

[] ���User Setting����ѡ����ͷ�ļ�����Wwise_IDS.h,���ڻ�ȡ���º�������Ĳ���

  - AudioDevice ��System" = 3859886410U(��������ͬ����Ҫ������������ͷ�ļ���ȡAudioDeviceID����ʹ�ã�
  - Mastering Suite ShareSetID
    - Off = 930712164U (��ΪDefault Preset��
    - TV = 1568083719U
    - HomeCinema = 1568083719U
    - HeadPhones = 880395932U
    - SoundBar = 1396549701U
    - NightMode = 2444352864U
  - in_uFXIndex��Ч��������±꣬��Mastering SuiteĬ��λ��AudioDevice_Effect�����һ����ۣ���in_uFXIndex=3
Ŀǰ���� AK::SoundEngine ���þ�ͨ�� AudioDeviceʵ�֣��ұ����� AkAudioģ����ʵ�֣�������AkAudioģ������չ���ܣ��Ա㱩¶�����Wwise���ܡ�

[] UE C++����

[] AkAudio.Build.cs��167�к�����Ч����������  "MasteringSuiteFX"�����¡�

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

# ʹ�÷���
    AkAudio.Build.cs λ��%GameProjectName\Plugins\Wwise\Source\AkAudio\AkAudio.Build.cs

    cpp�ļ����õ�ַ %GameProjectName\Plugins\Wwise\Source\AkAudio\Private\SwitchBusFX.cpp

    header�ļ����õ�ַ %GameProjectName\Plugins\Wwise\Source\AkAudio\Public\AudioLab.h

    ��C++��������Unreal�༭�����������󣬼�������ͼWwise|AudioDevice��ʹ�ø�Wwise������չ