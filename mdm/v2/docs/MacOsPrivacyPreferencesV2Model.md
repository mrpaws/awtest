# MacOsPrivacyPreferencesV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Gets or sets the bundle ID or installation path of the binary. | [optional] 
**identifier_type** | **str** | Gets or sets the type of Identifier value. Must be either bundleID or path. | [optional] 
**code_requirement** | **str** | Gets or sets obtained via the command \&quot;codesign --display -r - path\&quot;. | [optional] 
**static_code** | **bool** | Gets or sets a value indicating whether if set to true, statically validate the code requirement. | [optional] 
**comment** | **str** | Gets or sets the comment. | [optional] 
**address_book** | **str** | Gets or sets allows the application access to contact information managed by Contacts app. Must be either Allow or Disallow. | [optional] 
**calendar** | **str** | Gets or sets allows the application access to calendar information managed by Calendar.app. Must be either Allow or Disallow. | [optional] 
**reminders** | **str** | Gets or sets allows the application access to reminders information managed by Reminders.app. Must be either Allow or Disallow. | [optional] 
**photos** | **str** | Gets or sets allows the application access to pictures managed by Photos.app in ~/Pictures/.photoslibrary. Must be either Allow or Disallow. | [optional] 
**camera** | **str** | Gets or sets a system camera. Access to the camera cannot be given in a profile; it can only be Disallow. | [optional] 
**microphone** | **str** | Gets or sets a system microphone. Access to the microphone cannot be given in a profile; it can only be Disallow. | [optional] 
**accessibility** | **str** | Gets or sets control the application via the Accessibility subsystem. Must be either Allow or Disallow. | [optional] 
**post_event** | **str** | Gets or sets allows the application to use CoreGraphics APIs to send CGEvents to the system event stream. Must be either Allow or Disallow. | [optional] 
**system_policy_all_files** | **str** | Gets or sets allows the application access to all protected files. Must be either Allow or Disallow. | [optional] 
**system_policy_sys_admin_files** | **str** | Gets or sets allows the application access to some files used in system administration. Must be either Allow or Disallow. | [optional] 
**file_provider_presence** | **str** | Gets or sets allows the application to access documents and directories stored and managed by another app’s File Provider extension. . | [optional] 
**listen_event** | **str** | Gets or sets disallows the application to monitor events from input devices (mouse, keyboard, and trackpad). It can only be denied. | [optional] 
**media_library** | **str** | Gets or sets user’s collections of images, audio, and video from various media sources, such as iTunes or Aperture. | [optional] 
**screen_capture** | **str** | Gets or sets disallows the application to access controls for screen capture and recording. It can only be denied. | [optional] 
**speech_recognition** | **str** | Gets or sets allows the application to use speech recognition capabilities. | [optional] 
**system_policy_desktop_folder** | **str** | Gets or sets allows the application access to files on the Desktop. | [optional] 
**system_policy_documents_folder** | **str** | Gets or sets allows the application access to files in Documents. | [optional] 
**system_policy_downloads_folder** | **str** | Gets or sets allows the application access to files in Downloads. | [optional] 
**system_policy_network_volumes** | **str** | Gets or sets allows the application access to files on Network Volumes. | [optional] 
**system_policy_removable_volumes** | **str** | Gets or sets allows the application access to files on Removable Volumes. | [optional] 
**apple_events** | **str** | Gets or sets allows the application to send a restricted AppleEvent to another process. Must be either Allow or Disallow. | [optional] 
**ae_receiver_identifier** | **str** | Gets or sets the identifier of the process receiving an AppleEvent sent by the Identifier process. | [optional] 
**ae_receiver_identifier_type** | **str** | Gets or sets the type of AEReceiverIdentifier value. Must be either bundleID or path. | [optional] 
**ae_receiver_code_requirement** | **str** | Gets or sets code requirement for the receiving binary. | [optional] 
**apple_events_list** | [**list[AppleEvent]**](AppleEvent.md) | Gets or sets apple Events list. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


