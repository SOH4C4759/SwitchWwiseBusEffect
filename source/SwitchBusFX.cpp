#include "SwitchBusFX.h"
#include <AK/Plugin/MasteringSuiteFXFactory.h>
#include <AK\SoundEngine\Common\AkMemoryMgr.h>
#include <AK\SoundEngine\Common\AkModule.h>

// Define an enum to represent the available presets
enum class EPreset :int
{
    Off = 0,
    TV,
    HomeCinema,
    Headphones,
    SoundBar,
    NightMode,
    Count // Keep track of the number of presets
};

// Define a struct to hold the information for each preset
struct FPresetInfo
{
    int64 FxShareSetID;
    FString Name;
};

// Define an array of preset information
const TArray<FPresetInfo> PresetInfoArray = 
{
    {930712164,TEXT("Off")},
    {1568083719, TEXT("TV")},
    {4131355637, TEXT("HomeCinema")},
    {880395932, TEXT("Headphones")},
    {1396549701, TEXT("SoundBar")},
    {2444352864, TEXT("NightMode")}
}

// Declare and initialize the current preset index
int CurrentPresetIndex = 0;

void UWwiseExtensions::ChangeAudioDevicePreset()
{
    const int64 AudioDeviceID = 3859886410; // Default audio device ID
    const int UserFxIndex = 3; // Default user Fx index

    // Check if the game engine is running and log a message
    if (GEngine)
    {
        GEngine->AddOnScreenDebugMessage(-1, 5, FColor::Green, TEXT("FunctionCalled::ChangeAudioDevicePreset!"));
        UE_LOG(LogTemp, Display, TEXT("CalledFunction:ChangeAudioDevicePreset!"));
    }

    // Increments the current preset index and wrap around if necessary
    CurrentPresetIndex = (CurrentPresetIndex + 1) % static_cast<int>(EPreset::Count);

    // Set the FxShareSetId based on the current preset index
    const int64 FxShareSetID = PresetInfoArray[CurrentPresetIndex].FxShareSetID;
    const FString& PresetName = PresetInfoArray[CurrentPresetIndex].Name;

    // Log a message to indicate which preset has been selected
    const FString Message = FString::Printf(Text("Preset=%s"), *PresetName);
    GEngine->AddOnScreenDebugMessage(-1, 5, FColor::Red, Message);

    // Set the output device effect using the Wwise API
    AK::SoundEngine::SetOutputDeviceEffect(AudioDeviceID, UserFxIndex, FxShareSetID);
};
