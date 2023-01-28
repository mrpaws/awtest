# mdmv1.PickListsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pick_lists_get_allowed_geo_fencing_area_ids_by_lg**](PickListsApi.md#pick_lists_get_allowed_geo_fencing_area_ids_by_lg) | **GET** /picklists/organizationgroups/{ogid}/geofencingareas | Gets Geo Fencing Areas by Og Id.
[**pick_lists_get_allowed_time_fencing_schedule_ids_by_lg**](PickListsApi.md#pick_lists_get_allowed_time_fencing_schedule_ids_by_lg) | **GET** /picklists/organizationgroups/{ogid}/timefencingschedules | Gets Allowed Time Fencing Schedules by Og Id.
[**pick_lists_get_certificate_authority_list**](PickListsApi.md#pick_lists_get_certificate_authority_list) | **GET** /picklists/organizationgroups/{ogid}/certificateauthorities | Gets the list of Certificate Authorities (CA) for an organization group.
[**pick_lists_get_certificate_store_for_windows_mobile**](PickListsApi.md#pick_lists_get_certificate_store_for_windows_mobile) | **GET** /picklists/windowsmobilecertificatestore | Gets Certificate Store for WindowsMobile.
[**pick_lists_get_certificate_templates_for_certificate_authority**](PickListsApi.md#pick_lists_get_certificate_templates_for_certificate_authority) | **GET** /picklists/organizationgroups/{ogId}/certificateauthorities/{certificateAuthorityId}/getcertificatetemplates | Gets Certificate Templates List for Certificate Authority.
[**pick_lists_get_certificate_templates_list_for_certificate_authority**](PickListsApi.md#pick_lists_get_certificate_templates_list_for_certificate_authority) | **GET** /picklists/organizationgroups/{ogid}/certificateauthorities/{certificateAuthorityId}/certificatetemplates | Gets the list of Certificate Templates for a Certificate Authority (CA).
[**pick_lists_get_credential_certificate_store_for_windows_pc**](PickListsApi.md#pick_lists_get_credential_certificate_store_for_windows_pc) | **GET** /picklists/windowspccredentialcertificatestore | Returns Crdential Certificate Store for Windows PC platform.
[**pick_lists_get_credential_smime_for_apple**](PickListsApi.md#pick_lists_get_credential_smime_for_apple) | **GET** /picklists/applecredentialsmime | Gets the values that can be configured for the Credential Smime(Smime) for Apple Credentials profile.
[**pick_lists_get_credential_source_for_android**](PickListsApi.md#pick_lists_get_credential_source_for_android) | **GET** /picklists/androidcredentialsource | Gets Credential Source for Android.
[**pick_lists_get_credential_source_for_apple**](PickListsApi.md#pick_lists_get_credential_source_for_apple) | **GET** /picklists/applecredentialsource | Gets the values that can be configured for Credential Source(CertificateSource) for Apple Credentials profile.
[**pick_lists_get_credential_source_for_apple_os_x**](PickListsApi.md#pick_lists_get_credential_source_for_apple_os_x) | **GET** /picklists/appleosxcredentialsource | Gets valid CredentialSources(CertificateSource) for Apple macOS platform.
[**pick_lists_get_credential_source_for_windows_mobile**](PickListsApi.md#pick_lists_get_credential_source_for_windows_mobile) | **GET** /picklists/windowsmobilecredentialsource | Gets Credential Source for WindowsMobile.
[**pick_lists_get_credential_source_for_windows_pc**](PickListsApi.md#pick_lists_get_credential_source_for_windows_pc) | **GET** /picklists/windowspccredentialsource | Returns Crdential Source for Windows PC platform.
[**pick_lists_get_credential_store_location_for_windows_pc**](PickListsApi.md#pick_lists_get_credential_store_location_for_windows_pc) | **GET** /picklists/windowspccredentialstorelocation | Returns Crdential Store Location for Windows PC platform.
[**pick_lists_get_device_category_list**](PickListsApi.md#pick_lists_get_device_category_list) | **GET** /picklists/devicecategories | Gets device category list.
[**pick_lists_get_device_model_list**](PickListsApi.md#pick_lists_get_device_model_list) | **GET** /picklists/platforms/{platform}/devicemodels | Gets device model list.
[**pick_lists_get_device_type_list**](PickListsApi.md#pick_lists_get_device_type_list) | **GET** /picklists/devicetypes | Gets device type list.
[**pick_lists_get_eas_authentication_type_for_android**](PickListsApi.md#pick_lists_get_eas_authentication_type_for_android) | **GET** /picklists/androideasauthenticationtype | Gets Eas Authentication Type for Android.
[**pick_lists_get_eas_auto_lock_for_android**](PickListsApi.md#pick_lists_get_eas_auto_lock_for_android) | **GET** /picklists/androideasautolock | Gets Eas Auto Lock for Android.
[**pick_lists_get_eas_aw_email_client_complexity_for_apple**](PickListsApi.md#pick_lists_get_eas_aw_email_client_complexity_for_apple) | **GET** /picklists/appleeasawemailclientcomplexity | Gets EAS AW Email Client Passcode Complexity for Apple.
[**pick_lists_get_eas_aw_email_client_email_notifications_for_apple**](PickListsApi.md#pick_lists_get_eas_aw_email_client_email_notifications_for_apple) | **GET** /picklists/appleeasawemailclientemailnotifications | Gets EAS AW Email Client Email Notifications(Notifications) for Apple AirWatch EAS profile.
[**pick_lists_get_eas_aw_email_client_history_for_apple**](PickListsApi.md#pick_lists_get_eas_aw_email_client_history_for_apple) | **GET** /picklists/appleeasawemailclienthistory | Gets EAS AW Email Client Passcode History for Apple.
[**pick_lists_get_eas_aw_email_client_max_number_of_failed_attempts_for_apple**](PickListsApi.md#pick_lists_get_eas_aw_email_client_max_number_of_failed_attempts_for_apple) | **GET** /picklists/appleeasawemailclientmaximumfailedattempts | Gets EAS AW Email Client Maximum Failed Attempts for Apple.
[**pick_lists_get_eas_aw_email_client_passcode_type_for_apple**](PickListsApi.md#pick_lists_get_eas_aw_email_client_passcode_type_for_apple) | **GET** /picklists/appleeasawemailclientpasscodetype | Gets EAS AW Email Client Passcode Type for Apple.
[**pick_lists_get_eas_aw_email_client_past_days_of_calendar_to_sync_for_apple**](PickListsApi.md#pick_lists_get_eas_aw_email_client_past_days_of_calendar_to_sync_for_apple) | **GET** /picklists/appleeasawemailclientpastdaysofcalendartosync | Gets the number of days&#39; calendar to sync.
[**pick_lists_get_eas_aw_email_client_past_days_of_mail_to_sync_for_apple**](PickListsApi.md#pick_lists_get_eas_aw_email_client_past_days_of_mail_to_sync_for_apple) | **GET** /picklists/appleeasawemailclientpastdaysofmailtosync | Gets the number of days&#39; mail to sync.
[**pick_lists_get_eas_aw_email_client_sync_interval_for_apple**](PickListsApi.md#pick_lists_get_eas_aw_email_client_sync_interval_for_apple) | **GET** /picklists/appleeasawemailclientsyncinterval | SyncInterval determines the sync interval for the email.
[**pick_lists_get_eas_calendar_application_for_android**](PickListsApi.md#pick_lists_get_eas_calendar_application_for_android) | **GET** /picklists/androideascalendarapplication | Gets Eas Calendar Application for Android.
[**pick_lists_get_eas_contacts_application_for_android**](PickListsApi.md#pick_lists_get_eas_contacts_application_for_android) | **GET** /picklists/androideascontactsapplication | Gets Eas Contacts Application for Android.
[**pick_lists_get_eas_mail_client_for_android**](PickListsApi.md#pick_lists_get_eas_mail_client_for_android) | **GET** /picklists/androideasmailclient | Gets Eas Mail Client for Android.
[**pick_lists_get_eas_maximum_passcode_age_for_android**](PickListsApi.md#pick_lists_get_eas_maximum_passcode_age_for_android) | **GET** /picklists/androideasmaximumpasscodeage | Gets Eas Maximum Passcode Age for Android.
[**pick_lists_get_eas_minimum_passcode_length_for_android**](PickListsApi.md#pick_lists_get_eas_minimum_passcode_length_for_android) | **GET** /picklists/androideasminimumpasscodelength | Gets Eas Minimum Passcode length for Android.
[**pick_lists_get_eas_passcode_complexity_for_android**](PickListsApi.md#pick_lists_get_eas_passcode_complexity_for_android) | **GET** /picklists/androideaspasscodecomplexity | Gets Eas Passcode Complexity for Android.
[**pick_lists_get_eas_past_days_of_calendar_to_sync_for_android**](PickListsApi.md#pick_lists_get_eas_past_days_of_calendar_to_sync_for_android) | **GET** /picklists/androideaspastdaysofcalendartosync | Gets Eas past days of calendar to sync for Android.
[**pick_lists_get_eas_past_days_of_mail_to_sync_for_android**](PickListsApi.md#pick_lists_get_eas_past_days_of_mail_to_sync_for_android) | **GET** /picklists/androideaspastdaysofmailtosync | Gets Eas past days of mail to sync for Android.
[**pick_lists_get_eas_past_days_of_mail_to_sync_for_apple**](PickListsApi.md#pick_lists_get_eas_past_days_of_mail_to_sync_for_apple) | **GET** /picklists/appleeaspastdaysofmailtosync | Gets the the number of days&#39; mail to be synced.
[**pick_lists_get_eas_peak_time_for_android**](PickListsApi.md#pick_lists_get_eas_peak_time_for_android) | **GET** /picklists/androideaspeaktime | Gets Eas Peak Time for Android.
[**pick_lists_get_eas_restriction_type_for_android**](PickListsApi.md#pick_lists_get_eas_restriction_type_for_android) | **GET** /picklists/androideasrestrictiontype | Gets Eas Restriction Type for Android.
[**pick_lists_get_eas_sync_interval_for_android**](PickListsApi.md#pick_lists_get_eas_sync_interval_for_android) | **GET** /picklists/androideassyncinterval | Gets Eas Sync Interval for Android.
[**pick_lists_get_eas_sync_schedule_for_android**](PickListsApi.md#pick_lists_get_eas_sync_schedule_for_android) | **GET** /picklists/androideassyncschedule | Gets Eas Sync Schedule for Android.
[**pick_lists_get_email_account_type_for_apple**](PickListsApi.md#pick_lists_get_email_account_type_for_apple) | **GET** /picklists/appleemailaccounttype | Gets the values that can be configured for Email Account Type(EmailAccountType).
[**pick_lists_get_email_account_type_for_apple_os_x**](PickListsApi.md#pick_lists_get_email_account_type_for_apple_os_x) | **GET** /picklists/appleosxemailaccounttype | Gets valid Email Account types for Apple macOS Platform.
[**pick_lists_get_email_authentication_type_for_apple_os_x**](PickListsApi.md#pick_lists_get_email_authentication_type_for_apple_os_x) | **GET** /picklists/appleosxemailauthenticationtype | Gets valid Email Authentication Types for Apple macOS Platform.
[**pick_lists_get_email_sync_interval_for_android**](PickListsApi.md#pick_lists_get_email_sync_interval_for_android) | **GET** /picklists/androidemailsyncintervals | Gets E-Mail Sync Intervals for android.
[**pick_lists_get_encrypted_volume_for_windows_pc**](PickListsApi.md#pick_lists_get_encrypted_volume_for_windows_pc) | **GET** /picklists/windowspcencryptedvolume | Returns Encrypted volume for Windows PC platform.
[**pick_lists_get_font_size_for_android**](PickListsApi.md#pick_lists_get_font_size_for_android) | **GET** /picklists/androidfontsize | Gets Font Size for Android.
[**pick_lists_get_grace_period_for_passcode_change_for_android**](PickListsApi.md#pick_lists_get_grace_period_for_passcode_change_for_android) | **GET** /picklists/androidgraceperiodforpasscodechange | Gets Android Grace Period for Passcode change.
[**pick_lists_get_important_updates_for_windows_pc**](PickListsApi.md#pick_lists_get_important_updates_for_windows_pc) | **GET** /picklists/windowspcimportantupdates | Returns Important Updates for Windows PC platform.
[**pick_lists_get_incoming_mail_server_authentication_for_apple**](PickListsApi.md#pick_lists_get_incoming_mail_server_authentication_for_apple) | **GET** /picklists/appleincomingmailserverauthentication | Gets the values that can be configured for Incoming mail server authentication(IncomingMailServerAuthentication).
[**pick_lists_get_incoming_mail_server_protocol_for_android**](PickListsApi.md#pick_lists_get_incoming_mail_server_protocol_for_android) | **GET** /picklists/androidincomingmailserverprotocol | Gets Incomming Mail Server Protocol for android.
[**pick_lists_get_inner_identity_for_apple**](PickListsApi.md#pick_lists_get_inner_identity_for_apple) | **GET** /picklists/applewifiinneridentity | Gets the values that can be configured for inner authentication(TTLSInnerAuthentication) in Apple WIFI profile.
[**pick_lists_get_machine_authentication_for_apple**](PickListsApi.md#pick_lists_get_machine_authentication_for_apple) | **GET** /picklists/applemachineauthentication | Gets values that can be configured for Machine Authentication (IPSecAuthenticationMode) for Apple VPN profile.
[**pick_lists_get_max_mails_to_show_for_android**](PickListsApi.md#pick_lists_get_max_mails_to_show_for_android) | **GET** /picklists/androidmaxmailstoshow | Gets Maximum E-mails to show for Android.
[**pick_lists_get_min_wifi_security_for_android**](PickListsApi.md#pick_lists_get_min_wifi_security_for_android) | **GET** /picklists/androidminwifisecurity | Gets Minimum Wifi Security for Android.
[**pick_lists_get_network_inner_identity_for_apple_os_x**](PickListsApi.md#pick_lists_get_network_inner_identity_for_apple_os_x) | **GET** /picklists/appleosxnetworkinneridentity | Gets Network Inner Identity of TTLS protocol in Apple macOS Wi-Fi payload.
[**pick_lists_get_network_interface_for_apple_os_x**](PickListsApi.md#pick_lists_get_network_interface_for_apple_os_x) | **GET** /picklists/appleosxnetworkinterface | Gets Network Interfaces for Apple macOS Platform.
[**pick_lists_get_network_proxy_types_for_apple_os_x**](PickListsApi.md#pick_lists_get_network_proxy_types_for_apple_os_x) | **GET** /picklists/appleosxnetworkproxytype | Gets Valid ProxyTypes for Apple macOS Wi-Fi Payload.
[**pick_lists_get_network_security_type_for_apple_os_x**](PickListsApi.md#pick_lists_get_network_security_type_for_apple_os_x) | **GET** /picklists/appleosxnetworksecuritytype | Gets Network Security Protocols for Apple macOS Wi-Fi payload.
[**pick_lists_get_operating_system_list**](PickListsApi.md#pick_lists_get_operating_system_list) | **GET** /picklists/platforms/{platform}/operatingsystems | Gets operating systems list.
[**pick_lists_get_outgoing_mail_server_authentication_for_apple**](PickListsApi.md#pick_lists_get_outgoing_mail_server_authentication_for_apple) | **GET** /picklists/appleoutgoingmailserverauthentication | Gets the values that can be configured for Outgoing mail server authentication(IncomingMailServerAuthentication).
[**pick_lists_get_outgoing_mail_server_protocol_for_android**](PickListsApi.md#pick_lists_get_outgoing_mail_server_protocol_for_android) | **GET** /picklists/androidoutgoingmailserverprotocol | Gets Outgoing Mail Server Protocol for android.
[**pick_lists_get_ownership_type_list**](PickListsApi.md#pick_lists_get_ownership_type_list) | **GET** /picklists/ownershiptypes | Gets ownership type list.
[**pick_lists_get_passcode_auto_lock_for_apple**](PickListsApi.md#pick_lists_get_passcode_auto_lock_for_apple) | **GET** /picklists/applepasscodeautolock | Gets the values that can be configured for passcode autolock in minutes(maxInactivity) in Apple passcode profile.
[**pick_lists_get_passcode_auto_lock_for_apple_os_x**](PickListsApi.md#pick_lists_get_passcode_auto_lock_for_apple_os_x) | **GET** /picklists/appleosxpasscodeautolock | Gets the values that can be configured for passcode autolock in minutes(maxInactivity) in Apple macOS passcode profile.
[**pick_lists_get_passcode_content_for_android**](PickListsApi.md#pick_lists_get_passcode_content_for_android) | **GET** /picklists/androidpasscodecontent | Gets Passcode Content for Android.
[**pick_lists_get_passcode_grace_period_for_apple**](PickListsApi.md#pick_lists_get_passcode_grace_period_for_apple) | **GET** /picklists/applepasscodegraceperiod | Gets the values that can be configured for maximum grace period(maxGracePeriod) in Apple passcode profile.
[**pick_lists_get_proxy_type_for_apple**](PickListsApi.md#pick_lists_get_proxy_type_for_apple) | **GET** /picklists/appleproxytype | Gets the values that can be configured for Vpn proxy type(HTTPProxyType) in Apple VPN profile.
[**pick_lists_get_rating_apps_for_apple**](PickListsApi.md#pick_lists_get_rating_apps_for_apple) | **GET** /picklists/appleratingapps | Gets the values that can be configured for rating apps (ratingApps) in Apple Restrictions profile.
[**pick_lists_get_rating_movies_for_apple**](PickListsApi.md#pick_lists_get_rating_movies_for_apple) | **GET** /picklists/appleratingmovies | Gets the values that can be configured for rating movies (ratingMovies) in Apple Restrictions profile.
[**pick_lists_get_rating_region_for_apple**](PickListsApi.md#pick_lists_get_rating_region_for_apple) | **GET** /picklists/appleratingregion | Gets the values that can be configured for rating region (ratingRegion) in Apple Restrictions profile.
[**pick_lists_get_rating_tv_shows_for_apple**](PickListsApi.md#pick_lists_get_rating_tv_shows_for_apple) | **GET** /picklists/appleratingtvshows | Gets the values that can be configured for rating tv shows (ratingTVShows) in Apple Restrictions profile.
[**pick_lists_get_restriction_allowed_applications_for_apple_os_x**](PickListsApi.md#pick_lists_get_restriction_allowed_applications_for_apple_os_x) | **GET** /picklists/appleosxrestrictionallowedapplications | Gets eligible applications to apply restriction of Apple macOS platform.
[**pick_lists_get_restriction_allowed_widgets_for_apple_os_x**](PickListsApi.md#pick_lists_get_restriction_allowed_widgets_for_apple_os_x) | **GET** /picklists/appleosxrestrictionallowedwidgets | Gets eligible widgets to apply restriction of Apple macOS platform.
[**pick_lists_get_restriction_dataconnection_for_android**](PickListsApi.md#pick_lists_get_restriction_dataconnection_for_android) | **GET** /picklists/androidrestrictiondataconnection | Gets Restriction Data Connection for Android.
[**pick_lists_get_safari_accept_cookies_for_apple**](PickListsApi.md#pick_lists_get_safari_accept_cookies_for_apple) | **GET** /picklists/applesafariacceptcookies | Gets the values that can be configured for safari accept cookies(safariAcceptCookies) in Apple Restrictions profile.
[**pick_lists_get_scep_credential_source_for_apple**](PickListsApi.md#pick_lists_get_scep_credential_source_for_apple) | **GET** /picklists/applescepcredentialsource | Gets the values that can be configured for Credential Source(CertificateSource) for Apple SCEP profile.
[**pick_lists_get_scep_credential_source_for_apple_os_x**](PickListsApi.md#pick_lists_get_scep_credential_source_for_apple_os_x) | **GET** /picklists/appleosxscepcredentialsource | Gets valid Scep CredentialSorces(CertificateSource) for Apple macOS platform.
[**pick_lists_get_security_type_for_android_wifi**](PickListsApi.md#pick_lists_get_security_type_for_android_wifi) | **GET** /picklists/androidwifisecuritytype | Gets Security Type for Android Wifi.
[**pick_lists_get_security_type_for_windows_mobile_wifi**](PickListsApi.md#pick_lists_get_security_type_for_windows_mobile_wifi) | **GET** /picklists/windowsmobilewifisecuritytype | Gets Security Type for Windows Mobile Wifi.
[**pick_lists_get_sfa_type_for_android_wifi**](PickListsApi.md#pick_lists_get_sfa_type_for_android_wifi) | **GET** /picklists/androidwifisfatype | Gets sfa Type for Androie Wifi.
[**pick_lists_get_smime_certificate_type_for_android**](PickListsApi.md#pick_lists_get_smime_certificate_type_for_android) | **GET** /picklists/androidsmimecertificatetype | Gets SMIME certificate type for Android.
[**pick_lists_get_tfa_type_for_android_wifi**](PickListsApi.md#pick_lists_get_tfa_type_for_android_wifi) | **GET** /picklists/androidwifitfatype | Gets Tfa Type for Android Wifi.
[**pick_lists_get_user_authentication_type_for_apple**](PickListsApi.md#pick_lists_get_user_authentication_type_for_apple) | **GET** /picklists/appleuserauthenticationtype | Gets the values that can be configured for User Authentication Type for Apple VPN Profile.
[**pick_lists_get_vpn_authentication_method_for_apple**](PickListsApi.md#pick_lists_get_vpn_authentication_method_for_apple) | **GET** /picklists/applevpnauthenticationmethod | Gets the values that can be configured for Vpn authentication method(VpnAuthenticationMethod) in Apple VPN profile.
[**pick_lists_get_vpn_encryption_level_for_apple**](PickListsApi.md#pick_lists_get_vpn_encryption_level_for_apple) | **GET** /picklists/appleencryptionlevel | Gets values that can be configured for VPN encryption level(PP2PEncryptionLevel) for Apple VPN profile.
[**pick_lists_get_vpn_encryption_level_for_apple_os_x**](PickListsApi.md#pick_lists_get_vpn_encryption_level_for_apple_os_x) | **GET** /picklists/appleosxvpnencryptionlevel | Gets values that can be configured for VPN encryption level(PP2PEncryptionLevel) for Apple macOS VPN profile.
[**pick_lists_get_vpn_ike_id_type_for_android**](PickListsApi.md#pick_lists_get_vpn_ike_id_type_for_android) | **GET** /picklists/androidvpnikeidtype | Gets Vpn IKE ID Type for Android.
[**pick_lists_get_vpn_machine_authentication_for_apple_os_x**](PickListsApi.md#pick_lists_get_vpn_machine_authentication_for_apple_os_x) | **GET** /picklists/appleosxvpnmachineauthentication | Gets MachineAuthentication For Apple macOS VPN Profile.
[**pick_lists_get_vpn_on_demand_type_for_apple_os_x**](PickListsApi.md#pick_lists_get_vpn_on_demand_type_for_apple_os_x) | **GET** /picklists/appleosxvpnondemandtypes | Gets VPN OnDemandType values for Apple macOS platform.
[**pick_lists_get_vpn_proxy_for_apple_os_x_platform**](PickListsApi.md#pick_lists_get_vpn_proxy_for_apple_os_x_platform) | **GET** /picklists/appleosxvpnproxy | Gets VPN proxy types for Apple macOS platform.
[**pick_lists_get_vpn_type**](PickListsApi.md#pick_lists_get_vpn_type) | **GET** /picklists/platforms/{platform}/vpntypes | Gets Vpn Types by Platform.
[**pick_lists_get_vpn_user_authentication_for_apple_os_x**](PickListsApi.md#pick_lists_get_vpn_user_authentication_for_apple_os_x) | **GET** /picklists/appleosxvpnuserauthentication/{vpnType} | Gets Valid UserAuthentication for the specified VpnType.
[**pick_lists_get_wifi_connection_mode_for_windows_pc**](PickListsApi.md#pick_lists_get_wifi_connection_mode_for_windows_pc) | **GET** /picklists/windowspcwificonnectionmode | Returns Valid Wifi Connection Modes for Windows PC platform.
[**pick_lists_get_wifi_connection_type_for_windows_pc**](PickListsApi.md#pick_lists_get_wifi_connection_type_for_windows_pc) | **GET** /picklists/windowspcwificonnectiontype | Returns Valid Wifi Connection Types for Windows PC platform.
[**pick_lists_get_wifi_encryption_for_windows_pc**](PickListsApi.md#pick_lists_get_wifi_encryption_for_windows_pc) | **GET** /picklists/windowspcwifiencryptiontype | Returns Valid Wifi Encryption Types for Windows PC platform.
[**pick_lists_get_wifi_proxy_type_for_apple**](PickListsApi.md#pick_lists_get_wifi_proxy_type_for_apple) | **GET** /picklists/applewifiproxytype | Gets the values that can be configured for WIFI proxy type(ProxyType) in Apple WIFI profile.
[**pick_lists_get_wifi_security_type_for_apple**](PickListsApi.md#pick_lists_get_wifi_security_type_for_apple) | **GET** /picklists/applewifisecuritytype | Gets values that can be configured for encryption type(EncryptionType) for Apple WIFI profile.
[**pick_lists_get_wifi_security_type_for_windows_pc**](PickListsApi.md#pick_lists_get_wifi_security_type_for_windows_pc) | **GET** /picklists/windowspcwifisecuritytype | Returns Valid Wifi Security Types for Windows PC platform.
[**pick_lists_get_windows_update_source_for_windows_pc**](PickListsApi.md#pick_lists_get_windows_update_source_for_windows_pc) | **GET** /picklists/windowspcupdatesource | Returns Windows Update Source for Windows PC platform.


# **pick_lists_get_allowed_geo_fencing_area_ids_by_lg**
> list[PickListItem] pick_lists_get_allowed_geo_fencing_area_ids_by_lg(ogid)

Gets Geo Fencing Areas by Og Id.

Method to load area entities for a given location group.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))
ogid = 56 # int | Og Id (Required).

try:
    # Gets Geo Fencing Areas by Og Id.
    api_response = api_instance.pick_lists_get_allowed_geo_fencing_area_ids_by_lg(ogid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_allowed_geo_fencing_area_ids_by_lg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ogid** | **int**| Og Id (Required). | 

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_allowed_time_fencing_schedule_ids_by_lg**
> list[PickListItem] pick_lists_get_allowed_time_fencing_schedule_ids_by_lg(ogid)

Gets Allowed Time Fencing Schedules by Og Id.

Method to load Schedule entities for a given location group.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))
ogid = 56 # int | Og Id (Required).

try:
    # Gets Allowed Time Fencing Schedules by Og Id.
    api_response = api_instance.pick_lists_get_allowed_time_fencing_schedule_ids_by_lg(ogid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_allowed_time_fencing_schedule_ids_by_lg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ogid** | **int**| Og Id (Required). | 

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_certificate_authority_list**
> list[PickListItem] pick_lists_get_certificate_authority_list(ogid)

Gets the list of Certificate Authorities (CA) for an organization group.

Retrieves the list of Certificate Authority (CA) for an organization group.  In cryptography, a certificate authority is an entity that issues digital certificates. A digital certificate certifies the ownership of a public key by the named subject of the certificate.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))
ogid = 56 # int | Organization Group Id.

try:
    # Gets the list of Certificate Authorities (CA) for an organization group.
    api_response = api_instance.pick_lists_get_certificate_authority_list(ogid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_certificate_authority_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ogid** | **int**| Organization Group Id. | 

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_certificate_store_for_windows_mobile**
> pick_lists_get_certificate_store_for_windows_mobile()

Gets Certificate Store for WindowsMobile.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Certificate Store for WindowsMobile.
    api_instance.pick_lists_get_certificate_store_for_windows_mobile()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_certificate_store_for_windows_mobile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_certificate_templates_for_certificate_authority**
> pick_lists_get_certificate_templates_for_certificate_authority(og_id, certificate_authority_id)

Gets Certificate Templates List for Certificate Authority.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))
og_id = 56 # int | Og Id.
certificate_authority_id = 56 # int | Certificate Authority Id.

try:
    # Gets Certificate Templates List for Certificate Authority.
    api_instance.pick_lists_get_certificate_templates_for_certificate_authority(og_id, certificate_authority_id)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_certificate_templates_for_certificate_authority: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **og_id** | **int**| Og Id. | 
 **certificate_authority_id** | **int**| Certificate Authority Id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_certificate_templates_list_for_certificate_authority**
> list[PickListItem] pick_lists_get_certificate_templates_list_for_certificate_authority(ogid, certificate_authority_id)

Gets the list of Certificate Templates for a Certificate Authority (CA).

Retrieves the list of Certificate templates for an organization group.  A Certificate template is a preconfigured list of certificate settings that allows users and computers to enroll for certificates without having to create complex certificate requests.  Enterprise certification authorities (CAs) use certificate templates to define the format and content of certificates, to specify which users and computers can enroll for which types of certificates,  and to define the enrollment process, such as autoenrollment, enrollment only with authorized signatures, and manual enrollment.  Associated with each certificate template is a discretionary access control list (DACL) that defines which security principals have permissions to read and configure the template,  as well as to enroll or autoenroll for certificates based on the template. The certificate templates and their permissions are defined in Active Directory® Domain Services (AD DS) and are valid within the forest.  If more than one enterprise CA is running in the Active Directory forest, permission changes will affect all enterprise CAs.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))
ogid = 56 # int | Organization Group Id.
certificate_authority_id = 56 # int | Certificate Authority Id.

try:
    # Gets the list of Certificate Templates for a Certificate Authority (CA).
    api_response = api_instance.pick_lists_get_certificate_templates_list_for_certificate_authority(ogid, certificate_authority_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_certificate_templates_list_for_certificate_authority: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ogid** | **int**| Organization Group Id. | 
 **certificate_authority_id** | **int**| Certificate Authority Id. | 

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_credential_certificate_store_for_windows_pc**
> list[PickListItem] pick_lists_get_credential_certificate_store_for_windows_pc()

Returns Crdential Certificate Store for Windows PC platform.

Gets a list of supported credential certificate store for credentials profile.  Example : Personal, Trusted Root certificate authorities, Trusted publishers, untrusted publishers, Trusted people, Intermediate.  default is Personal.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Returns Crdential Certificate Store for Windows PC platform.
    api_response = api_instance.pick_lists_get_credential_certificate_store_for_windows_pc()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_credential_certificate_store_for_windows_pc: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_credential_smime_for_apple**
> list[PickListItem] pick_lists_get_credential_smime_for_apple()

Gets the values that can be configured for the Credential Smime(Smime) for Apple Credentials profile.

Smime detetrmines the encryption and signing requirements for email.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for the Credential Smime(Smime) for Apple Credentials profile.
    api_response = api_instance.pick_lists_get_credential_smime_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_credential_smime_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_credential_source_for_android**
> pick_lists_get_credential_source_for_android()

Gets Credential Source for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Credential Source for Android.
    api_instance.pick_lists_get_credential_source_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_credential_source_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_credential_source_for_apple**
> list[PickListItem] pick_lists_get_credential_source_for_apple()

Gets the values that can be configured for Credential Source(CertificateSource) for Apple Credentials profile.

CertificateSource determines the source of the certificate.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for Credential Source(CertificateSource) for Apple Credentials profile.
    api_response = api_instance.pick_lists_get_credential_source_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_credential_source_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_credential_source_for_apple_os_x**
> list[PickListItem] pick_lists_get_credential_source_for_apple_os_x()

Gets valid CredentialSources(CertificateSource) for Apple macOS platform.

CertificateSource determines the source of the certificate.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets valid CredentialSources(CertificateSource) for Apple macOS platform.
    api_response = api_instance.pick_lists_get_credential_source_for_apple_os_x()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_credential_source_for_apple_os_x: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_credential_source_for_windows_mobile**
> pick_lists_get_credential_source_for_windows_mobile()

Gets Credential Source for WindowsMobile.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Credential Source for WindowsMobile.
    api_instance.pick_lists_get_credential_source_for_windows_mobile()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_credential_source_for_windows_mobile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_credential_source_for_windows_pc**
> list[PickListItem] pick_lists_get_credential_source_for_windows_pc()

Returns Crdential Source for Windows PC platform.

Gets a list of supported credential source for credentials profile.  Example : DefinedCertificateAuthority.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Returns Crdential Source for Windows PC platform.
    api_response = api_instance.pick_lists_get_credential_source_for_windows_pc()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_credential_source_for_windows_pc: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_credential_store_location_for_windows_pc**
> list[PickListItem] pick_lists_get_credential_store_location_for_windows_pc()

Returns Crdential Store Location for Windows PC platform.

Gets a list of supported credential store locations for credentials profile.  Example : User Account, System Account.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Returns Crdential Store Location for Windows PC platform.
    api_response = api_instance.pick_lists_get_credential_store_location_for_windows_pc()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_credential_store_location_for_windows_pc: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_device_category_list**
> list[PickListItem] pick_lists_get_device_category_list()

Gets device category list.

Gets the list of all the available device categories from the picklist Eg.Apple.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets device category list.
    api_response = api_instance.pick_lists_get_device_category_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_device_category_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_device_model_list**
> list[PickListItem] pick_lists_get_device_model_list(platform)

Gets device model list.

Gets the list of all the available device models loaded from the picklist for the specified platform.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))
platform = 'platform_example' # str | device platform name Eg:APPLE (Required).

try:
    # Gets device model list.
    api_response = api_instance.pick_lists_get_device_model_list(platform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_device_model_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| device platform name Eg:APPLE (Required). | 

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_device_type_list**
> list[PickListItem] pick_lists_get_device_type_list()

Gets device type list.

Gets the list of all the available device types from the picklist Eg.Apple, Android.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets device type list.
    api_response = api_instance.pick_lists_get_device_type_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_device_type_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_authentication_type_for_android**
> pick_lists_get_eas_authentication_type_for_android()

Gets Eas Authentication Type for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Eas Authentication Type for Android.
    api_instance.pick_lists_get_eas_authentication_type_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_authentication_type_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_auto_lock_for_android**
> pick_lists_get_eas_auto_lock_for_android()

Gets Eas Auto Lock for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Eas Auto Lock for Android.
    api_instance.pick_lists_get_eas_auto_lock_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_auto_lock_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_aw_email_client_complexity_for_apple**
> list[PickListItem] pick_lists_get_eas_aw_email_client_complexity_for_apple()

Gets EAS AW Email Client Passcode Complexity for Apple.

Returns the expected passcode complexity for Email account of EAS profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets EAS AW Email Client Passcode Complexity for Apple.
    api_response = api_instance.pick_lists_get_eas_aw_email_client_complexity_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_aw_email_client_complexity_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_aw_email_client_email_notifications_for_apple**
> list[PickListItem] pick_lists_get_eas_aw_email_client_email_notifications_for_apple()

Gets EAS AW Email Client Email Notifications(Notifications) for Apple AirWatch EAS profile.

Notifications determines the emaiil client notifications for the email.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets EAS AW Email Client Email Notifications(Notifications) for Apple AirWatch EAS profile.
    api_response = api_instance.pick_lists_get_eas_aw_email_client_email_notifications_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_aw_email_client_email_notifications_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_aw_email_client_history_for_apple**
> list[PickListItem] pick_lists_get_eas_aw_email_client_history_for_apple()

Gets EAS AW Email Client Passcode History for Apple.

Returns passcode history for email account of EAS profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets EAS AW Email Client Passcode History for Apple.
    api_response = api_instance.pick_lists_get_eas_aw_email_client_history_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_aw_email_client_history_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_aw_email_client_max_number_of_failed_attempts_for_apple**
> list[PickListItem] pick_lists_get_eas_aw_email_client_max_number_of_failed_attempts_for_apple()

Gets EAS AW Email Client Maximum Failed Attempts for Apple.

Returns valid value for max failed attempts for email account of EAS profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets EAS AW Email Client Maximum Failed Attempts for Apple.
    api_response = api_instance.pick_lists_get_eas_aw_email_client_max_number_of_failed_attempts_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_aw_email_client_max_number_of_failed_attempts_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_aw_email_client_passcode_type_for_apple**
> list[PickListItem] pick_lists_get_eas_aw_email_client_passcode_type_for_apple()

Gets EAS AW Email Client Passcode Type for Apple.

Returns valid values for the Authentication type which can be used for EAS AW Email Client.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets EAS AW Email Client Passcode Type for Apple.
    api_response = api_instance.pick_lists_get_eas_aw_email_client_passcode_type_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_aw_email_client_passcode_type_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_aw_email_client_past_days_of_calendar_to_sync_for_apple**
> list[PickListItem] pick_lists_get_eas_aw_email_client_past_days_of_calendar_to_sync_for_apple()

Gets the number of days' calendar to sync.

returns values that can be configured for EAS AW Email Client Past Days of Calendar to Sync for Apple.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the number of days' calendar to sync.
    api_response = api_instance.pick_lists_get_eas_aw_email_client_past_days_of_calendar_to_sync_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_aw_email_client_past_days_of_calendar_to_sync_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_aw_email_client_past_days_of_mail_to_sync_for_apple**
> list[PickListItem] pick_lists_get_eas_aw_email_client_past_days_of_mail_to_sync_for_apple()

Gets the number of days' mail to sync.

Values that can be configured for the EAS AW Email Client Past Days of Mail to Sync(MaxEmailAge) for Apple.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the number of days' mail to sync.
    api_response = api_instance.pick_lists_get_eas_aw_email_client_past_days_of_mail_to_sync_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_aw_email_client_past_days_of_mail_to_sync_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_aw_email_client_sync_interval_for_apple**
> list[PickListItem] pick_lists_get_eas_aw_email_client_sync_interval_for_apple()

SyncInterval determines the sync interval for the email.

Gets the values that can be configured for EAS AW Email Client Sync Interval(SyncInterval) for Apple AirWatch EAS profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # SyncInterval determines the sync interval for the email.
    api_response = api_instance.pick_lists_get_eas_aw_email_client_sync_interval_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_aw_email_client_sync_interval_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_calendar_application_for_android**
> pick_lists_get_eas_calendar_application_for_android()

Gets Eas Calendar Application for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Eas Calendar Application for Android.
    api_instance.pick_lists_get_eas_calendar_application_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_calendar_application_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_contacts_application_for_android**
> pick_lists_get_eas_contacts_application_for_android()

Gets Eas Contacts Application for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Eas Contacts Application for Android.
    api_instance.pick_lists_get_eas_contacts_application_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_contacts_application_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_mail_client_for_android**
> pick_lists_get_eas_mail_client_for_android()

Gets Eas Mail Client for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Eas Mail Client for Android.
    api_instance.pick_lists_get_eas_mail_client_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_mail_client_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_maximum_passcode_age_for_android**
> pick_lists_get_eas_maximum_passcode_age_for_android()

Gets Eas Maximum Passcode Age for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Eas Maximum Passcode Age for Android.
    api_instance.pick_lists_get_eas_maximum_passcode_age_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_maximum_passcode_age_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_minimum_passcode_length_for_android**
> pick_lists_get_eas_minimum_passcode_length_for_android()

Gets Eas Minimum Passcode length for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Eas Minimum Passcode length for Android.
    api_instance.pick_lists_get_eas_minimum_passcode_length_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_minimum_passcode_length_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_passcode_complexity_for_android**
> pick_lists_get_eas_passcode_complexity_for_android()

Gets Eas Passcode Complexity for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Eas Passcode Complexity for Android.
    api_instance.pick_lists_get_eas_passcode_complexity_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_passcode_complexity_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_past_days_of_calendar_to_sync_for_android**
> pick_lists_get_eas_past_days_of_calendar_to_sync_for_android()

Gets Eas past days of calendar to sync for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Eas past days of calendar to sync for Android.
    api_instance.pick_lists_get_eas_past_days_of_calendar_to_sync_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_past_days_of_calendar_to_sync_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_past_days_of_mail_to_sync_for_android**
> pick_lists_get_eas_past_days_of_mail_to_sync_for_android()

Gets Eas past days of mail to sync for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Eas past days of mail to sync for Android.
    api_instance.pick_lists_get_eas_past_days_of_mail_to_sync_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_past_days_of_mail_to_sync_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_past_days_of_mail_to_sync_for_apple**
> list[PickListItem] pick_lists_get_eas_past_days_of_mail_to_sync_for_apple()

Gets the the number of days' mail to be synced.

MailNumberOfPastDaysToSync specifies values that can be configured for Eas Past Days of Mail to Sync(MailNumberOfPastDaysToSync) for Apple EAS profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the the number of days' mail to be synced.
    api_response = api_instance.pick_lists_get_eas_past_days_of_mail_to_sync_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_past_days_of_mail_to_sync_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_peak_time_for_android**
> pick_lists_get_eas_peak_time_for_android()

Gets Eas Peak Time for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Eas Peak Time for Android.
    api_instance.pick_lists_get_eas_peak_time_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_peak_time_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_restriction_type_for_android**
> pick_lists_get_eas_restriction_type_for_android()

Gets Eas Restriction Type for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Eas Restriction Type for Android.
    api_instance.pick_lists_get_eas_restriction_type_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_restriction_type_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_sync_interval_for_android**
> pick_lists_get_eas_sync_interval_for_android()

Gets Eas Sync Interval for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Eas Sync Interval for Android.
    api_instance.pick_lists_get_eas_sync_interval_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_sync_interval_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_eas_sync_schedule_for_android**
> pick_lists_get_eas_sync_schedule_for_android()

Gets Eas Sync Schedule for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Eas Sync Schedule for Android.
    api_instance.pick_lists_get_eas_sync_schedule_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_eas_sync_schedule_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_email_account_type_for_apple**
> list[PickListItem] pick_lists_get_email_account_type_for_apple()

Gets the values that can be configured for Email Account Type(EmailAccountType).

EmailAccountType determines the type of email (POP, IMAP) in Apple Email profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for Email Account Type(EmailAccountType).
    api_response = api_instance.pick_lists_get_email_account_type_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_email_account_type_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_email_account_type_for_apple_os_x**
> list[PickListItem] pick_lists_get_email_account_type_for_apple_os_x()

Gets valid Email Account types for Apple macOS Platform.

Supported Account types for Email Profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets valid Email Account types for Apple macOS Platform.
    api_response = api_instance.pick_lists_get_email_account_type_for_apple_os_x()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_email_account_type_for_apple_os_x: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_email_authentication_type_for_apple_os_x**
> list[PickListItem] pick_lists_get_email_authentication_type_for_apple_os_x()

Gets valid Email Authentication Types for Apple macOS Platform.

Server authentication types for Email Profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets valid Email Authentication Types for Apple macOS Platform.
    api_response = api_instance.pick_lists_get_email_authentication_type_for_apple_os_x()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_email_authentication_type_for_apple_os_x: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_email_sync_interval_for_android**
> pick_lists_get_email_sync_interval_for_android()

Gets E-Mail Sync Intervals for android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets E-Mail Sync Intervals for android.
    api_instance.pick_lists_get_email_sync_interval_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_email_sync_interval_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_encrypted_volume_for_windows_pc**
> list[PickListItem] pick_lists_get_encrypted_volume_for_windows_pc()

Returns Encrypted volume for Windows PC platform.

Gets a list of encrypted volumes for encryption profile.  Example : Complete Hard Disk, System Partition.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Returns Encrypted volume for Windows PC platform.
    api_response = api_instance.pick_lists_get_encrypted_volume_for_windows_pc()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_encrypted_volume_for_windows_pc: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_font_size_for_android**
> pick_lists_get_font_size_for_android()

Gets Font Size for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Font Size for Android.
    api_instance.pick_lists_get_font_size_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_font_size_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_grace_period_for_passcode_change_for_android**
> pick_lists_get_grace_period_for_passcode_change_for_android()

Gets Android Grace Period for Passcode change.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Android Grace Period for Passcode change.
    api_instance.pick_lists_get_grace_period_for_passcode_change_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_grace_period_for_passcode_change_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_important_updates_for_windows_pc**
> list[PickListItem] pick_lists_get_important_updates_for_windows_pc()

Returns Important Updates for Windows PC platform.

Gets a list of supported actions for important updates  Example : Install Updates Automatically, Download updates but let the user decide when to install them.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Returns Important Updates for Windows PC platform.
    api_response = api_instance.pick_lists_get_important_updates_for_windows_pc()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_important_updates_for_windows_pc: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_incoming_mail_server_authentication_for_apple**
> list[PickListItem] pick_lists_get_incoming_mail_server_authentication_for_apple()

Gets the values that can be configured for Incoming mail server authentication(IncomingMailServerAuthentication).

IncomingMailServerAuthentication determines the authentication scheme for incoming mail in Apple Email profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for Incoming mail server authentication(IncomingMailServerAuthentication).
    api_response = api_instance.pick_lists_get_incoming_mail_server_authentication_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_incoming_mail_server_authentication_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_incoming_mail_server_protocol_for_android**
> pick_lists_get_incoming_mail_server_protocol_for_android()

Gets Incomming Mail Server Protocol for android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Incomming Mail Server Protocol for android.
    api_instance.pick_lists_get_incoming_mail_server_protocol_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_incoming_mail_server_protocol_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_inner_identity_for_apple**
> list[PickListItem] pick_lists_get_inner_identity_for_apple()

Gets the values that can be configured for inner authentication(TTLSInnerAuthentication) in Apple WIFI profile.

TTLSInnerAuthentication determines inner authentication used by the TTLS module.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for inner authentication(TTLSInnerAuthentication) in Apple WIFI profile.
    api_response = api_instance.pick_lists_get_inner_identity_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_inner_identity_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_machine_authentication_for_apple**
> list[PickListItem] pick_lists_get_machine_authentication_for_apple()

Gets values that can be configured for Machine Authentication (IPSecAuthenticationMode) for Apple VPN profile.

Machine Authentication methods available for VPN profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets values that can be configured for Machine Authentication (IPSecAuthenticationMode) for Apple VPN profile.
    api_response = api_instance.pick_lists_get_machine_authentication_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_machine_authentication_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_max_mails_to_show_for_android**
> pick_lists_get_max_mails_to_show_for_android()

Gets Maximum E-mails to show for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Maximum E-mails to show for Android.
    api_instance.pick_lists_get_max_mails_to_show_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_max_mails_to_show_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_min_wifi_security_for_android**
> pick_lists_get_min_wifi_security_for_android()

Gets Minimum Wifi Security for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Minimum Wifi Security for Android.
    api_instance.pick_lists_get_min_wifi_security_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_min_wifi_security_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_network_inner_identity_for_apple_os_x**
> list[PickListItem] pick_lists_get_network_inner_identity_for_apple_os_x()

Gets Network Inner Identity of TTLS protocol in Apple macOS Wi-Fi payload.

Inner Authentication required for TTLS protocol.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Network Inner Identity of TTLS protocol in Apple macOS Wi-Fi payload.
    api_response = api_instance.pick_lists_get_network_inner_identity_for_apple_os_x()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_network_inner_identity_for_apple_os_x: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_network_interface_for_apple_os_x**
> list[PickListItem] pick_lists_get_network_interface_for_apple_os_x()

Gets Network Interfaces for Apple macOS Platform.

Supported interfaces(Wi-Fi, Ethernet) for Network profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Network Interfaces for Apple macOS Platform.
    api_response = api_instance.pick_lists_get_network_interface_for_apple_os_x()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_network_interface_for_apple_os_x: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_network_proxy_types_for_apple_os_x**
> list[PickListItem] pick_lists_get_network_proxy_types_for_apple_os_x()

Gets Valid ProxyTypes for Apple macOS Wi-Fi Payload.

Proxy types supported for Network profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Valid ProxyTypes for Apple macOS Wi-Fi Payload.
    api_response = api_instance.pick_lists_get_network_proxy_types_for_apple_os_x()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_network_proxy_types_for_apple_os_x: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_network_security_type_for_apple_os_x**
> list[PickListItem] pick_lists_get_network_security_type_for_apple_os_x()

Gets Network Security Protocols for Apple macOS Wi-Fi payload.

Supported Security protocols(WEP, WPA / WPA2) for Network profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Network Security Protocols for Apple macOS Wi-Fi payload.
    api_response = api_instance.pick_lists_get_network_security_type_for_apple_os_x()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_network_security_type_for_apple_os_x: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_operating_system_list**
> list[PickListItem] pick_lists_get_operating_system_list(platform)

Gets operating systems list.

Gets the list of all the available operating systems from the picklist for the specified platform Eg.iOS 4.0.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))
platform = 'platform_example' # str | device platform name Eg:APPLE (Required).

try:
    # Gets operating systems list.
    api_response = api_instance.pick_lists_get_operating_system_list(platform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_operating_system_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| device platform name Eg:APPLE (Required). | 

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_outgoing_mail_server_authentication_for_apple**
> list[PickListItem] pick_lists_get_outgoing_mail_server_authentication_for_apple()

Gets the values that can be configured for Outgoing mail server authentication(IncomingMailServerAuthentication).

IncomingMailServerAuthentication determines the authentication scheme for outgoing mail in Apple Email profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for Outgoing mail server authentication(IncomingMailServerAuthentication).
    api_response = api_instance.pick_lists_get_outgoing_mail_server_authentication_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_outgoing_mail_server_authentication_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_outgoing_mail_server_protocol_for_android**
> pick_lists_get_outgoing_mail_server_protocol_for_android()

Gets Outgoing Mail Server Protocol for android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Outgoing Mail Server Protocol for android.
    api_instance.pick_lists_get_outgoing_mail_server_protocol_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_outgoing_mail_server_protocol_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_ownership_type_list**
> list[PickListItem] pick_lists_get_ownership_type_list()

Gets ownership type list.

Gets the list of all the available ownership types from the picklist Eg.EmployeeOwned.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets ownership type list.
    api_response = api_instance.pick_lists_get_ownership_type_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_ownership_type_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_passcode_auto_lock_for_apple**
> list[PickListItem] pick_lists_get_passcode_auto_lock_for_apple()

Gets the values that can be configured for passcode autolock in minutes(maxInactivity) in Apple passcode profile.

Device automatically locks when time period elapses.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for passcode autolock in minutes(maxInactivity) in Apple passcode profile.
    api_response = api_instance.pick_lists_get_passcode_auto_lock_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_passcode_auto_lock_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_passcode_auto_lock_for_apple_os_x**
> list[PickListItem] pick_lists_get_passcode_auto_lock_for_apple_os_x()

Gets the values that can be configured for passcode autolock in minutes(maxInactivity) in Apple macOS passcode profile.

Device automatically locks when time period elapses.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for passcode autolock in minutes(maxInactivity) in Apple macOS passcode profile.
    api_response = api_instance.pick_lists_get_passcode_auto_lock_for_apple_os_x()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_passcode_auto_lock_for_apple_os_x: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_passcode_content_for_android**
> pick_lists_get_passcode_content_for_android()

Gets Passcode Content for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Passcode Content for Android.
    api_instance.pick_lists_get_passcode_content_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_passcode_content_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_passcode_grace_period_for_apple**
> list[PickListItem] pick_lists_get_passcode_grace_period_for_apple()

Gets the values that can be configured for maximum grace period(maxGracePeriod) in Apple passcode profile.

Amount of time device can be locked without prompting for passcode on unlock.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for maximum grace period(maxGracePeriod) in Apple passcode profile.
    api_response = api_instance.pick_lists_get_passcode_grace_period_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_passcode_grace_period_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_proxy_type_for_apple**
> list[PickListItem] pick_lists_get_proxy_type_for_apple()

Gets the values that can be configured for Vpn proxy type(HTTPProxyType) in Apple VPN profile.

HTTPProxyType determines proxy is manual or automatic.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for Vpn proxy type(HTTPProxyType) in Apple VPN profile.
    api_response = api_instance.pick_lists_get_proxy_type_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_proxy_type_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_rating_apps_for_apple**
> list[PickListItem] pick_lists_get_rating_apps_for_apple()

Gets the values that can be configured for rating apps (ratingApps) in Apple Restrictions profile.

RatingApps determines the ratings of the apps that are allowed.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for rating apps (ratingApps) in Apple Restrictions profile.
    api_response = api_instance.pick_lists_get_rating_apps_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_rating_apps_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_rating_movies_for_apple**
> list[PickListItem] pick_lists_get_rating_movies_for_apple(filter_key=filter_key)

Gets the values that can be configured for rating movies (ratingMovies) in Apple Restrictions profile.

RatingMovies determines the ratings of movies that are allowed.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))
filter_key = 'filter_key_example' # str | The key for filter countries. (optional)

try:
    # Gets the values that can be configured for rating movies (ratingMovies) in Apple Restrictions profile.
    api_response = api_instance.pick_lists_get_rating_movies_for_apple(filter_key=filter_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_rating_movies_for_apple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_key** | **str**| The key for filter countries. | [optional] 

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_rating_region_for_apple**
> list[PickListItem] pick_lists_get_rating_region_for_apple()

Gets the values that can be configured for rating region (ratingRegion) in Apple Restrictions profile.

RatingRegion determine the regions.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for rating region (ratingRegion) in Apple Restrictions profile.
    api_response = api_instance.pick_lists_get_rating_region_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_rating_region_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_rating_tv_shows_for_apple**
> list[PickListItem] pick_lists_get_rating_tv_shows_for_apple(filter_key=filter_key)

Gets the values that can be configured for rating tv shows (ratingTVShows) in Apple Restrictions profile.

RatingTVShows determines the ratings of tv shows that are allowed.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))
filter_key = 'filter_key_example' # str | The key for filter countries. (optional)

try:
    # Gets the values that can be configured for rating tv shows (ratingTVShows) in Apple Restrictions profile.
    api_response = api_instance.pick_lists_get_rating_tv_shows_for_apple(filter_key=filter_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_rating_tv_shows_for_apple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_key** | **str**| The key for filter countries. | [optional] 

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_restriction_allowed_applications_for_apple_os_x**
> list[PickListItem] pick_lists_get_restriction_allowed_applications_for_apple_os_x()

Gets eligible applications to apply restriction of Apple macOS platform.

Applicationsn list which are allowed to apply restrictions on.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets eligible applications to apply restriction of Apple macOS platform.
    api_response = api_instance.pick_lists_get_restriction_allowed_applications_for_apple_os_x()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_restriction_allowed_applications_for_apple_os_x: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_restriction_allowed_widgets_for_apple_os_x**
> list[PickListItem] pick_lists_get_restriction_allowed_widgets_for_apple_os_x()

Gets eligible widgets to apply restriction of Apple macOS platform.

Widgets list which are allowed to apply restrictions on.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets eligible widgets to apply restriction of Apple macOS platform.
    api_response = api_instance.pick_lists_get_restriction_allowed_widgets_for_apple_os_x()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_restriction_allowed_widgets_for_apple_os_x: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_restriction_dataconnection_for_android**
> pick_lists_get_restriction_dataconnection_for_android()

Gets Restriction Data Connection for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Restriction Data Connection for Android.
    api_instance.pick_lists_get_restriction_dataconnection_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_restriction_dataconnection_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_safari_accept_cookies_for_apple**
> list[PickListItem] pick_lists_get_safari_accept_cookies_for_apple()

Gets the values that can be configured for safari accept cookies(safariAcceptCookies) in Apple Restrictions profile.

SafariAcceptCookies determines conditions under which the device will accept cookies.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for safari accept cookies(safariAcceptCookies) in Apple Restrictions profile.
    api_response = api_instance.pick_lists_get_safari_accept_cookies_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_safari_accept_cookies_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_scep_credential_source_for_apple**
> list[PickListItem] pick_lists_get_scep_credential_source_for_apple()

Gets the values that can be configured for Credential Source(CertificateSource) for Apple SCEP profile.

CertificateSource determines the source of the certificate.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for Credential Source(CertificateSource) for Apple SCEP profile.
    api_response = api_instance.pick_lists_get_scep_credential_source_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_scep_credential_source_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_scep_credential_source_for_apple_os_x**
> list[PickListItem] pick_lists_get_scep_credential_source_for_apple_os_x(include_supported_only=include_supported_only, include_airwatch_caif_enabled_in_og=include_airwatch_caif_enabled_in_og, organization_group_uuid=organization_group_uuid)

Gets valid Scep CredentialSorces(CertificateSource) for Apple macOS platform.

CertificateSource determines the source of the certificate.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))
include_supported_only =  # bool | (Optional) Flag to indicate if only supported \"CredentialSource\" list is to be included or not.Default is False. (optional) (default to )
include_airwatch_caif_enabled_in_og =  # bool | (Optional) Flag to indicate to include Airwatch Certificate Authority only if its Enabled in the OG or not.Default is False. (optional) (default to )
organization_group_uuid =  # object | (Required if includeAirwatchCAIfEnabledInOg is true)OrganizationGroup's Uuid in which EnableAirwatchCA system code is to be checked for. (optional) (default to )

try:
    # Gets valid Scep CredentialSorces(CertificateSource) for Apple macOS platform.
    api_response = api_instance.pick_lists_get_scep_credential_source_for_apple_os_x(include_supported_only=include_supported_only, include_airwatch_caif_enabled_in_og=include_airwatch_caif_enabled_in_og, organization_group_uuid=organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_scep_credential_source_for_apple_os_x: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_supported_only** | **bool**| (Optional) Flag to indicate if only supported \&quot;CredentialSource\&quot; list is to be included or not.Default is False. | [optional] [default to ]
 **include_airwatch_caif_enabled_in_og** | **bool**| (Optional) Flag to indicate to include Airwatch Certificate Authority only if its Enabled in the OG or not.Default is False. | [optional] [default to ]
 **organization_group_uuid** | [**object**](.md)| (Required if includeAirwatchCAIfEnabledInOg is true)OrganizationGroup&#39;s Uuid in which EnableAirwatchCA system code is to be checked for. | [optional] [default to ]

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_security_type_for_android_wifi**
> pick_lists_get_security_type_for_android_wifi()

Gets Security Type for Android Wifi.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Security Type for Android Wifi.
    api_instance.pick_lists_get_security_type_for_android_wifi()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_security_type_for_android_wifi: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_security_type_for_windows_mobile_wifi**
> pick_lists_get_security_type_for_windows_mobile_wifi()

Gets Security Type for Windows Mobile Wifi.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Security Type for Windows Mobile Wifi.
    api_instance.pick_lists_get_security_type_for_windows_mobile_wifi()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_security_type_for_windows_mobile_wifi: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_sfa_type_for_android_wifi**
> pick_lists_get_sfa_type_for_android_wifi()

Gets sfa Type for Androie Wifi.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets sfa Type for Androie Wifi.
    api_instance.pick_lists_get_sfa_type_for_android_wifi()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_sfa_type_for_android_wifi: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_smime_certificate_type_for_android**
> pick_lists_get_smime_certificate_type_for_android()

Gets SMIME certificate type for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets SMIME certificate type for Android.
    api_instance.pick_lists_get_smime_certificate_type_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_smime_certificate_type_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_tfa_type_for_android_wifi**
> pick_lists_get_tfa_type_for_android_wifi()

Gets Tfa Type for Android Wifi.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Tfa Type for Android Wifi.
    api_instance.pick_lists_get_tfa_type_for_android_wifi()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_tfa_type_for_android_wifi: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_user_authentication_type_for_apple**
> list[PickListItem] pick_lists_get_user_authentication_type_for_apple()

Gets the values that can be configured for User Authentication Type for Apple VPN Profile.

UserAuthenticationType determines the authentication type for the user.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for User Authentication Type for Apple VPN Profile.
    api_response = api_instance.pick_lists_get_user_authentication_type_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_user_authentication_type_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_vpn_authentication_method_for_apple**
> list[PickListItem] pick_lists_get_vpn_authentication_method_for_apple()

Gets the values that can be configured for Vpn authentication method(VpnAuthenticationMethod) in Apple VPN profile.

VpnAuthenticationMethod determines the authentication method used for VPN.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for Vpn authentication method(VpnAuthenticationMethod) in Apple VPN profile.
    api_response = api_instance.pick_lists_get_vpn_authentication_method_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_vpn_authentication_method_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_vpn_encryption_level_for_apple**
> list[PickListItem] pick_lists_get_vpn_encryption_level_for_apple()

Gets values that can be configured for VPN encryption level(PP2PEncryptionLevel) for Apple VPN profile.

PP2PEncryptionLevel determines the vpn encryption level.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets values that can be configured for VPN encryption level(PP2PEncryptionLevel) for Apple VPN profile.
    api_response = api_instance.pick_lists_get_vpn_encryption_level_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_vpn_encryption_level_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_vpn_encryption_level_for_apple_os_x**
> list[PickListItem] pick_lists_get_vpn_encryption_level_for_apple_os_x()

Gets values that can be configured for VPN encryption level(PP2PEncryptionLevel) for Apple macOS VPN profile.

PP2PEncryptionLevel determines the vpn encryption level.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets values that can be configured for VPN encryption level(PP2PEncryptionLevel) for Apple macOS VPN profile.
    api_response = api_instance.pick_lists_get_vpn_encryption_level_for_apple_os_x()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_vpn_encryption_level_for_apple_os_x: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_vpn_ike_id_type_for_android**
> pick_lists_get_vpn_ike_id_type_for_android()

Gets Vpn IKE ID Type for Android.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets Vpn IKE ID Type for Android.
    api_instance.pick_lists_get_vpn_ike_id_type_for_android()
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_vpn_ike_id_type_for_android: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_vpn_machine_authentication_for_apple_os_x**
> list[PickListItem] pick_lists_get_vpn_machine_authentication_for_apple_os_x()

Gets MachineAuthentication For Apple macOS VPN Profile.

Authentication mode supported by VPN type for Machine Authentication.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets MachineAuthentication For Apple macOS VPN Profile.
    api_response = api_instance.pick_lists_get_vpn_machine_authentication_for_apple_os_x()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_vpn_machine_authentication_for_apple_os_x: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_vpn_on_demand_type_for_apple_os_x**
> list[PickListItem] pick_lists_get_vpn_on_demand_type_for_apple_os_x()

Gets VPN OnDemandType values for Apple macOS platform.

Supported for OnDemand Action values of VPN profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets VPN OnDemandType values for Apple macOS platform.
    api_response = api_instance.pick_lists_get_vpn_on_demand_type_for_apple_os_x()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_vpn_on_demand_type_for_apple_os_x: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_vpn_proxy_for_apple_os_x_platform**
> list[PickListItem] pick_lists_get_vpn_proxy_for_apple_os_x_platform()

Gets VPN proxy types for Apple macOS platform.

Proxy types valid for VPN profile.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets VPN proxy types for Apple macOS platform.
    api_response = api_instance.pick_lists_get_vpn_proxy_for_apple_os_x_platform()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_vpn_proxy_for_apple_os_x_platform: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_vpn_type**
> list[PickListItem] pick_lists_get_vpn_type(platform)

Gets Vpn Types by Platform.

Gets Vpn Payload picklist items for the specified platform(Ex. android, apple, appleosx, windowspc).

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))
platform = 'platform_example' # str | Platform name (Required).

try:
    # Gets Vpn Types by Platform.
    api_response = api_instance.pick_lists_get_vpn_type(platform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_vpn_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Platform name (Required). | 

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_vpn_user_authentication_for_apple_os_x**
> list[PickListItem] pick_lists_get_vpn_user_authentication_for_apple_os_x(vpn_type)

Gets Valid UserAuthentication for the specified VpnType.

Authentication method supported by VpnType.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))
vpn_type = 'vpn_type_example' # str | Vpn Type.

try:
    # Gets Valid UserAuthentication for the specified VpnType.
    api_response = api_instance.pick_lists_get_vpn_user_authentication_for_apple_os_x(vpn_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_vpn_user_authentication_for_apple_os_x: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_type** | **str**| Vpn Type. | 

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_wifi_connection_mode_for_windows_pc**
> list[PickListItem] pick_lists_get_wifi_connection_mode_for_windows_pc()

Returns Valid Wifi Connection Modes for Windows PC platform.

Gets a list of supported connection modes for wifi profile.  Example : Auto, Manual.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Returns Valid Wifi Connection Modes for Windows PC platform.
    api_response = api_instance.pick_lists_get_wifi_connection_mode_for_windows_pc()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_wifi_connection_mode_for_windows_pc: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_wifi_connection_type_for_windows_pc**
> list[PickListItem] pick_lists_get_wifi_connection_type_for_windows_pc()

Returns Valid Wifi Connection Types for Windows PC platform.

Gets a list of supported connection types for wifi profile.  Example : Infrastructure, ad-hoc.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Returns Valid Wifi Connection Types for Windows PC platform.
    api_response = api_instance.pick_lists_get_wifi_connection_type_for_windows_pc()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_wifi_connection_type_for_windows_pc: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_wifi_encryption_for_windows_pc**
> list[PickListItem] pick_lists_get_wifi_encryption_for_windows_pc()

Returns Valid Wifi Encryption Types for Windows PC platform.

Gets a list of supported encryption algorithms Wifi profile.  Example : TKIP, AES.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Returns Valid Wifi Encryption Types for Windows PC platform.
    api_response = api_instance.pick_lists_get_wifi_encryption_for_windows_pc()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_wifi_encryption_for_windows_pc: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_wifi_proxy_type_for_apple**
> list[PickListItem] pick_lists_get_wifi_proxy_type_for_apple()

Gets the values that can be configured for WIFI proxy type(ProxyType) in Apple WIFI profile.

ProxyType determines if the proxy is automatic or manual.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets the values that can be configured for WIFI proxy type(ProxyType) in Apple WIFI profile.
    api_response = api_instance.pick_lists_get_wifi_proxy_type_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_wifi_proxy_type_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_wifi_security_type_for_apple**
> list[PickListItem] pick_lists_get_wifi_security_type_for_apple()

Gets values that can be configured for encryption type(EncryptionType) for Apple WIFI profile.

EncryptionType determines the encryption type of the wifi configuration.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Gets values that can be configured for encryption type(EncryptionType) for Apple WIFI profile.
    api_response = api_instance.pick_lists_get_wifi_security_type_for_apple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_wifi_security_type_for_apple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_wifi_security_type_for_windows_pc**
> list[PickListItem] pick_lists_get_wifi_security_type_for_windows_pc()

Returns Valid Wifi Security Types for Windows PC platform.

Gets a list of supported security types for wifi profile.  Example : WPA2 Personal, WPA Enterprise.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Returns Valid Wifi Security Types for Windows PC platform.
    api_response = api_instance.pick_lists_get_wifi_security_type_for_windows_pc()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_wifi_security_type_for_windows_pc: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_lists_get_windows_update_source_for_windows_pc**
> list[PickListItem] pick_lists_get_windows_update_source_for_windows_pc()

Returns Windows Update Source for Windows PC platform.

Gets a list of supported update sources for windows update  Example : Microsoft, Corporate Wsus  Microsoft is default.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.PickListsApi(mdmv1.ApiClient(configuration))

try:
    # Returns Windows Update Source for Windows PC platform.
    api_response = api_instance.pick_lists_get_windows_update_source_for_windows_pc()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsApi->pick_lists_get_windows_update_source_for_windows_pc: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PickListItem]**](PickListItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

