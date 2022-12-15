#pragma once

#include "CoreMinimal.h"
#include "AkAudioModule.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "SwitchBusFX.generated.h"

/**
 *
 */
UCLASS()
class AKAUDIO_API UWwiseExtensions : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

public:

    /**
    * 通过Wwise的插件MasteringSuite 实时切换总线效果
    */
    UFUNCTION(BlueprintCallable, Category = "Wwise|AudioDevice")
        static void ChangeAudioDevicePreset();
