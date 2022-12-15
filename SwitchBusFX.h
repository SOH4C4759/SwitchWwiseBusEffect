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
    * ͨ��Wwise�Ĳ��MasteringSuite ʵʱ�л�����Ч��
    */
    UFUNCTION(BlueprintCallable, Category = "Wwise|AudioDevice")
        static void ChangeAudioDevicePreset();
