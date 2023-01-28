# AppleOsXNetworkPayloadEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_interface** | **str** | Gets or sets network Interface to connect to network using Wi-Fi or Ethernet. | [optional] 
**service_set_identifier** | **str** | Gets or sets sSID of the Wi-Fi network to be used. | [optional] 
**hidden_network** | **bool** | Gets or sets a value indicating whether besides SSID, the device uses information such as broadcast type and encryption type to differentiate a network. | [optional] 
**auto_join** | **bool** | Gets or sets a value indicating whether if true, the network is auto-joined on iOS 5+. | [optional] 
**security_type** | **str** | Gets or sets the encryption type of the Wi-FI network. | [optional] 
**password** | **str** | Gets or sets sSID password (Pre-Shared Key). | [optional] 
**use_as_login_window_configuration** | **bool** | Gets or sets a value indicating whether it true, allows the user to authenticate to the network at login. | [optional] 
**use_directory_authentication** | **bool** | Gets or sets a value indicating whether if true, the target machine’s directory credentials is used as an authentication method. | [optional] 
**tls** | **bool** | Gets or sets a value indicating whether if true, TLS is used for the Extensible Authentication Protocol. | [optional] 
**ttls** | **bool** | Gets or sets a value indicating whether if true, TTLS is used for the Extensible Authentication Protocol. | [optional] 
**leap** | **bool** | Gets or sets a value indicating whether if true, LEAP is used for the Extensible Authentication Protocol. | [optional] 
**peap** | **bool** | Gets or sets a value indicating whether if true, PEAP is used for the Extensible Authentication Protocol. | [optional] 
**eapfast** | **bool** | Gets or sets a value indicating whether if true, EAP-FAST is used for the Extensible Authentication Protocol. | [optional] 
**eapsim** | **bool** | Gets or sets a value indicating whether if true, EAP-SIM is used for the Extensible Authentication Protocol. | [optional] 
**eapaka** | **bool** | Gets or sets a value indicating whether if true, EAP-AKA is used for the Extensible Authentication Protocol. | [optional] 
**tls_minimum_version** | **str** | Gets or sets the minimum TLS version to be used with EAP-TLS authentication. If no value is specified, the default minimum is 1.0. | [optional] 
**tls_maximum_version** | **str** | Gets or sets the maximum TLS version to be used with EAP-TLS authentication. If no value is specified, the default maximum is 1.2. | [optional] 
**disable_association_mac_randomization** | **bool** | Gets or sets a value indicating whether MAC randomization is disabled. | [optional] 
**user_name** | **str** | Gets or sets the username used for authentication. | [optional] 
**user_password** | **str** | Gets or sets the password used for authentication. | [optional] 
**identity_certificate** | **str** | Gets or sets the certificate payload to use for the identity credential. | [optional] 
**inner_identity** | **str** | Gets or sets specifies the inner authentication used by the TTLS module. | [optional] 
**outer_identity** | **str** | Gets or sets this key is only relevant to TTLS, PEAP, and EAP-FAST for allowing the user to hide his or her identity. | [optional] 
**use_pac** | **bool** | Gets or sets a value indicating whether if true, the device will use an existing PAC if it&#39;s present. | [optional] 
**allow_two_rands** | **bool** | Gets or sets a value indicating whether if true, two RANDs are used for EAPSIM. | [optional] 
**trusted_certificates** | **list[str]** | Gets or sets certificates to be trusted for this authentication. | [optional] 
**allow_trust_exceptions** | **bool** | Gets or sets a value indicating whether if true, allows a dynamic trust decision by the user. | [optional] 
**proxy_type** | **str** | Gets or sets proxy type. | [optional] 
**proxy_server** | **str** | Gets or sets the host name of the HTTP proxy. | [optional] 
**proxy_server_port** | **int** | Gets or sets the port number of the HTTP proxy. | [optional] 
**proxy_username** | **str** | Gets or sets the username used for authentication. | [optional] 
**proxy_password** | **str** | Gets or sets the password used for authentication. | [optional] 
**proxy_url** | **str** | Gets or sets uRL to the location of the proxy auto-configuration file. | [optional] 
**pac_fallback** | **bool** | Gets or sets a value indicating whether if false, prevents the device from connecting directly to the destination if the PAC file is unreachable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


