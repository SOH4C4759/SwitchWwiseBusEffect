# TODO ����Waapi,����2022��ǰ�汾���м���
# TODO ����Perforce�˺�
# TODO ��⵱ǰWwise�����Ƿ���� MasteringSuite ԭ��Ԥ��
# TODO ͨ��Waapi�򹤳������Ч���� in_uFXIndex��Ч��������±꣬��Mastering SuiteĬ��λ��AudioDevice_Effect�����һ����ۣ���in_uFXIndex=3
# TODO ��MasteringSuite ԭ��Ԥ����ʽ�ؼ��뵽Init.bnk��Inclusion��
# TODO �Զ�����Init.bnk,������������ͷ�ļ�����Wwise_IDS.h,���ڻ�ȡ���º�������Ĳ���
# TODO �ر�Wwise����
# TODO ����Perforce��Ǩ���Ķ���changelist
# TODO ͨ��python��ȡ��ǰUE���̵�·��
# TODO ��֤UE�Ƿ���Wwise����
# TODO ��ȡ��ǰ���е�ַ����source�µ��ļ��ֱ𿽱���UE������
# TODO cpp�ļ����õ�ַ %GameProjectName\Plugins\Wwise\Source\AkAudio\Private\
# TODO header�ļ����õ�ַ %GameProjectName\Plugins\Wwise\Source\AkAudio\Public\SwitchBusFX.h
# TODO �༭�ļ�AkAudio.Build.cs λ��%GameProjectName\Plugins\Wwise\Source\AkAudio\AkAudio.Build.cs
# TODO ִ��UE�Ĵ������
# �༭�������£�
"""
AkAudio.Build.cs��167�к�����Ч����������  "MasteringSuiteFX"�����¡�

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

