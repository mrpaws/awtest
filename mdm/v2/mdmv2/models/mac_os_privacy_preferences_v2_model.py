# coding: utf-8

"""
    MDM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mdmv2.configuration import Configuration


class MacOsPrivacyPreferencesV2Model(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'identifier': 'str',
        'identifier_type': 'str',
        'code_requirement': 'str',
        'static_code': 'bool',
        'comment': 'str',
        'address_book': 'str',
        'calendar': 'str',
        'reminders': 'str',
        'photos': 'str',
        'camera': 'str',
        'microphone': 'str',
        'accessibility': 'str',
        'post_event': 'str',
        'system_policy_all_files': 'str',
        'system_policy_sys_admin_files': 'str',
        'file_provider_presence': 'str',
        'listen_event': 'str',
        'media_library': 'str',
        'screen_capture': 'str',
        'speech_recognition': 'str',
        'system_policy_desktop_folder': 'str',
        'system_policy_documents_folder': 'str',
        'system_policy_downloads_folder': 'str',
        'system_policy_network_volumes': 'str',
        'system_policy_removable_volumes': 'str',
        'apple_events': 'str',
        'ae_receiver_identifier': 'str',
        'ae_receiver_identifier_type': 'str',
        'ae_receiver_code_requirement': 'str',
        'apple_events_list': 'list[AppleEvent]'
    }

    attribute_map = {
        'identifier': 'Identifier',
        'identifier_type': 'IdentifierType',
        'code_requirement': 'CodeRequirement',
        'static_code': 'StaticCode',
        'comment': 'Comment',
        'address_book': 'AddressBook',
        'calendar': 'Calendar',
        'reminders': 'Reminders',
        'photos': 'Photos',
        'camera': 'Camera',
        'microphone': 'Microphone',
        'accessibility': 'Accessibility',
        'post_event': 'PostEvent',
        'system_policy_all_files': 'SystemPolicyAllFiles',
        'system_policy_sys_admin_files': 'SystemPolicySysAdminFiles',
        'file_provider_presence': 'FileProviderPresence',
        'listen_event': 'ListenEvent',
        'media_library': 'MediaLibrary',
        'screen_capture': 'ScreenCapture',
        'speech_recognition': 'SpeechRecognition',
        'system_policy_desktop_folder': 'SystemPolicyDesktopFolder',
        'system_policy_documents_folder': 'SystemPolicyDocumentsFolder',
        'system_policy_downloads_folder': 'SystemPolicyDownloadsFolder',
        'system_policy_network_volumes': 'SystemPolicyNetworkVolumes',
        'system_policy_removable_volumes': 'SystemPolicyRemovableVolumes',
        'apple_events': 'AppleEvents',
        'ae_receiver_identifier': 'AEReceiverIdentifier',
        'ae_receiver_identifier_type': 'AEReceiverIdentifierType',
        'ae_receiver_code_requirement': 'AEReceiverCodeRequirement',
        'apple_events_list': 'AppleEventsList'
    }

    def __init__(self, identifier=None, identifier_type=None, code_requirement=None, static_code=None, comment=None, address_book=None, calendar=None, reminders=None, photos=None, camera=None, microphone=None, accessibility=None, post_event=None, system_policy_all_files=None, system_policy_sys_admin_files=None, file_provider_presence=None, listen_event=None, media_library=None, screen_capture=None, speech_recognition=None, system_policy_desktop_folder=None, system_policy_documents_folder=None, system_policy_downloads_folder=None, system_policy_network_volumes=None, system_policy_removable_volumes=None, apple_events=None, ae_receiver_identifier=None, ae_receiver_identifier_type=None, ae_receiver_code_requirement=None, apple_events_list=None, _configuration=None):  # noqa: E501
        """MacOsPrivacyPreferencesV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._identifier = None
        self._identifier_type = None
        self._code_requirement = None
        self._static_code = None
        self._comment = None
        self._address_book = None
        self._calendar = None
        self._reminders = None
        self._photos = None
        self._camera = None
        self._microphone = None
        self._accessibility = None
        self._post_event = None
        self._system_policy_all_files = None
        self._system_policy_sys_admin_files = None
        self._file_provider_presence = None
        self._listen_event = None
        self._media_library = None
        self._screen_capture = None
        self._speech_recognition = None
        self._system_policy_desktop_folder = None
        self._system_policy_documents_folder = None
        self._system_policy_downloads_folder = None
        self._system_policy_network_volumes = None
        self._system_policy_removable_volumes = None
        self._apple_events = None
        self._ae_receiver_identifier = None
        self._ae_receiver_identifier_type = None
        self._ae_receiver_code_requirement = None
        self._apple_events_list = None
        self.discriminator = None

        if identifier is not None:
            self.identifier = identifier
        if identifier_type is not None:
            self.identifier_type = identifier_type
        if code_requirement is not None:
            self.code_requirement = code_requirement
        if static_code is not None:
            self.static_code = static_code
        if comment is not None:
            self.comment = comment
        if address_book is not None:
            self.address_book = address_book
        if calendar is not None:
            self.calendar = calendar
        if reminders is not None:
            self.reminders = reminders
        if photos is not None:
            self.photos = photos
        if camera is not None:
            self.camera = camera
        if microphone is not None:
            self.microphone = microphone
        if accessibility is not None:
            self.accessibility = accessibility
        if post_event is not None:
            self.post_event = post_event
        if system_policy_all_files is not None:
            self.system_policy_all_files = system_policy_all_files
        if system_policy_sys_admin_files is not None:
            self.system_policy_sys_admin_files = system_policy_sys_admin_files
        if file_provider_presence is not None:
            self.file_provider_presence = file_provider_presence
        if listen_event is not None:
            self.listen_event = listen_event
        if media_library is not None:
            self.media_library = media_library
        if screen_capture is not None:
            self.screen_capture = screen_capture
        if speech_recognition is not None:
            self.speech_recognition = speech_recognition
        if system_policy_desktop_folder is not None:
            self.system_policy_desktop_folder = system_policy_desktop_folder
        if system_policy_documents_folder is not None:
            self.system_policy_documents_folder = system_policy_documents_folder
        if system_policy_downloads_folder is not None:
            self.system_policy_downloads_folder = system_policy_downloads_folder
        if system_policy_network_volumes is not None:
            self.system_policy_network_volumes = system_policy_network_volumes
        if system_policy_removable_volumes is not None:
            self.system_policy_removable_volumes = system_policy_removable_volumes
        if apple_events is not None:
            self.apple_events = apple_events
        if ae_receiver_identifier is not None:
            self.ae_receiver_identifier = ae_receiver_identifier
        if ae_receiver_identifier_type is not None:
            self.ae_receiver_identifier_type = ae_receiver_identifier_type
        if ae_receiver_code_requirement is not None:
            self.ae_receiver_code_requirement = ae_receiver_code_requirement
        if apple_events_list is not None:
            self.apple_events_list = apple_events_list

    @property
    def identifier(self):
        """Gets the identifier of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets the bundle ID or installation path of the binary.  # noqa: E501

        :return: The identifier of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this MacOsPrivacyPreferencesV2Model.

        Gets or sets the bundle ID or installation path of the binary.  # noqa: E501

        :param identifier: The identifier of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def identifier_type(self):
        """Gets the identifier_type of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets the type of Identifier value. Must be either bundleID or path.  # noqa: E501

        :return: The identifier_type of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._identifier_type

    @identifier_type.setter
    def identifier_type(self, identifier_type):
        """Sets the identifier_type of this MacOsPrivacyPreferencesV2Model.

        Gets or sets the type of Identifier value. Must be either bundleID or path.  # noqa: E501

        :param identifier_type: The identifier_type of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._identifier_type = identifier_type

    @property
    def code_requirement(self):
        """Gets the code_requirement of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets obtained via the command \"codesign --display -r - path\".  # noqa: E501

        :return: The code_requirement of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._code_requirement

    @code_requirement.setter
    def code_requirement(self, code_requirement):
        """Sets the code_requirement of this MacOsPrivacyPreferencesV2Model.

        Gets or sets obtained via the command \"codesign --display -r - path\".  # noqa: E501

        :param code_requirement: The code_requirement of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._code_requirement = code_requirement

    @property
    def static_code(self):
        """Gets the static_code of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets a value indicating whether if set to true, statically validate the code requirement.  # noqa: E501

        :return: The static_code of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: bool
        """
        return self._static_code

    @static_code.setter
    def static_code(self, static_code):
        """Sets the static_code of this MacOsPrivacyPreferencesV2Model.

        Gets or sets a value indicating whether if set to true, statically validate the code requirement.  # noqa: E501

        :param static_code: The static_code of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: bool
        """

        self._static_code = static_code

    @property
    def comment(self):
        """Gets the comment of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets the comment.  # noqa: E501

        :return: The comment of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this MacOsPrivacyPreferencesV2Model.

        Gets or sets the comment.  # noqa: E501

        :param comment: The comment of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def address_book(self):
        """Gets the address_book of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets allows the application access to contact information managed by Contacts app. Must be either Allow or Disallow.  # noqa: E501

        :return: The address_book of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._address_book

    @address_book.setter
    def address_book(self, address_book):
        """Sets the address_book of this MacOsPrivacyPreferencesV2Model.

        Gets or sets allows the application access to contact information managed by Contacts app. Must be either Allow or Disallow.  # noqa: E501

        :param address_book: The address_book of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._address_book = address_book

    @property
    def calendar(self):
        """Gets the calendar of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets allows the application access to calendar information managed by Calendar.app. Must be either Allow or Disallow.  # noqa: E501

        :return: The calendar of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._calendar

    @calendar.setter
    def calendar(self, calendar):
        """Sets the calendar of this MacOsPrivacyPreferencesV2Model.

        Gets or sets allows the application access to calendar information managed by Calendar.app. Must be either Allow or Disallow.  # noqa: E501

        :param calendar: The calendar of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._calendar = calendar

    @property
    def reminders(self):
        """Gets the reminders of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets allows the application access to reminders information managed by Reminders.app. Must be either Allow or Disallow.  # noqa: E501

        :return: The reminders of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._reminders

    @reminders.setter
    def reminders(self, reminders):
        """Sets the reminders of this MacOsPrivacyPreferencesV2Model.

        Gets or sets allows the application access to reminders information managed by Reminders.app. Must be either Allow or Disallow.  # noqa: E501

        :param reminders: The reminders of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._reminders = reminders

    @property
    def photos(self):
        """Gets the photos of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets allows the application access to pictures managed by Photos.app in ~/Pictures/.photoslibrary. Must be either Allow or Disallow.  # noqa: E501

        :return: The photos of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._photos

    @photos.setter
    def photos(self, photos):
        """Sets the photos of this MacOsPrivacyPreferencesV2Model.

        Gets or sets allows the application access to pictures managed by Photos.app in ~/Pictures/.photoslibrary. Must be either Allow or Disallow.  # noqa: E501

        :param photos: The photos of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._photos = photos

    @property
    def camera(self):
        """Gets the camera of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets a system camera. Access to the camera cannot be given in a profile; it can only be Disallow.  # noqa: E501

        :return: The camera of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._camera

    @camera.setter
    def camera(self, camera):
        """Sets the camera of this MacOsPrivacyPreferencesV2Model.

        Gets or sets a system camera. Access to the camera cannot be given in a profile; it can only be Disallow.  # noqa: E501

        :param camera: The camera of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._camera = camera

    @property
    def microphone(self):
        """Gets the microphone of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets a system microphone. Access to the microphone cannot be given in a profile; it can only be Disallow.  # noqa: E501

        :return: The microphone of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._microphone

    @microphone.setter
    def microphone(self, microphone):
        """Sets the microphone of this MacOsPrivacyPreferencesV2Model.

        Gets or sets a system microphone. Access to the microphone cannot be given in a profile; it can only be Disallow.  # noqa: E501

        :param microphone: The microphone of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._microphone = microphone

    @property
    def accessibility(self):
        """Gets the accessibility of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets control the application via the Accessibility subsystem. Must be either Allow or Disallow.  # noqa: E501

        :return: The accessibility of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._accessibility

    @accessibility.setter
    def accessibility(self, accessibility):
        """Sets the accessibility of this MacOsPrivacyPreferencesV2Model.

        Gets or sets control the application via the Accessibility subsystem. Must be either Allow or Disallow.  # noqa: E501

        :param accessibility: The accessibility of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._accessibility = accessibility

    @property
    def post_event(self):
        """Gets the post_event of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets allows the application to use CoreGraphics APIs to send CGEvents to the system event stream. Must be either Allow or Disallow.  # noqa: E501

        :return: The post_event of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._post_event

    @post_event.setter
    def post_event(self, post_event):
        """Sets the post_event of this MacOsPrivacyPreferencesV2Model.

        Gets or sets allows the application to use CoreGraphics APIs to send CGEvents to the system event stream. Must be either Allow or Disallow.  # noqa: E501

        :param post_event: The post_event of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._post_event = post_event

    @property
    def system_policy_all_files(self):
        """Gets the system_policy_all_files of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets allows the application access to all protected files. Must be either Allow or Disallow.  # noqa: E501

        :return: The system_policy_all_files of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._system_policy_all_files

    @system_policy_all_files.setter
    def system_policy_all_files(self, system_policy_all_files):
        """Sets the system_policy_all_files of this MacOsPrivacyPreferencesV2Model.

        Gets or sets allows the application access to all protected files. Must be either Allow or Disallow.  # noqa: E501

        :param system_policy_all_files: The system_policy_all_files of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._system_policy_all_files = system_policy_all_files

    @property
    def system_policy_sys_admin_files(self):
        """Gets the system_policy_sys_admin_files of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets allows the application access to some files used in system administration. Must be either Allow or Disallow.  # noqa: E501

        :return: The system_policy_sys_admin_files of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._system_policy_sys_admin_files

    @system_policy_sys_admin_files.setter
    def system_policy_sys_admin_files(self, system_policy_sys_admin_files):
        """Sets the system_policy_sys_admin_files of this MacOsPrivacyPreferencesV2Model.

        Gets or sets allows the application access to some files used in system administration. Must be either Allow or Disallow.  # noqa: E501

        :param system_policy_sys_admin_files: The system_policy_sys_admin_files of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._system_policy_sys_admin_files = system_policy_sys_admin_files

    @property
    def file_provider_presence(self):
        """Gets the file_provider_presence of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets allows the application to access documents and directories stored and managed by another app???s File Provider extension.??.  # noqa: E501

        :return: The file_provider_presence of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._file_provider_presence

    @file_provider_presence.setter
    def file_provider_presence(self, file_provider_presence):
        """Sets the file_provider_presence of this MacOsPrivacyPreferencesV2Model.

        Gets or sets allows the application to access documents and directories stored and managed by another app???s File Provider extension.??.  # noqa: E501

        :param file_provider_presence: The file_provider_presence of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._file_provider_presence = file_provider_presence

    @property
    def listen_event(self):
        """Gets the listen_event of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets disallows the application to monitor events from input devices (mouse, keyboard, and trackpad). It can only be denied.  # noqa: E501

        :return: The listen_event of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._listen_event

    @listen_event.setter
    def listen_event(self, listen_event):
        """Sets the listen_event of this MacOsPrivacyPreferencesV2Model.

        Gets or sets disallows the application to monitor events from input devices (mouse, keyboard, and trackpad). It can only be denied.  # noqa: E501

        :param listen_event: The listen_event of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._listen_event = listen_event

    @property
    def media_library(self):
        """Gets the media_library of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets user???s collections of images, audio, and video from various media sources, such as iTunes or Aperture.  # noqa: E501

        :return: The media_library of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._media_library

    @media_library.setter
    def media_library(self, media_library):
        """Sets the media_library of this MacOsPrivacyPreferencesV2Model.

        Gets or sets user???s collections of images, audio, and video from various media sources, such as iTunes or Aperture.  # noqa: E501

        :param media_library: The media_library of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._media_library = media_library

    @property
    def screen_capture(self):
        """Gets the screen_capture of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets disallows the application to access controls for screen capture and recording. It can only be denied.  # noqa: E501

        :return: The screen_capture of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._screen_capture

    @screen_capture.setter
    def screen_capture(self, screen_capture):
        """Sets the screen_capture of this MacOsPrivacyPreferencesV2Model.

        Gets or sets disallows the application to access controls for screen capture and recording. It can only be denied.  # noqa: E501

        :param screen_capture: The screen_capture of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._screen_capture = screen_capture

    @property
    def speech_recognition(self):
        """Gets the speech_recognition of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets allows the application to use speech recognition capabilities.  # noqa: E501

        :return: The speech_recognition of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._speech_recognition

    @speech_recognition.setter
    def speech_recognition(self, speech_recognition):
        """Sets the speech_recognition of this MacOsPrivacyPreferencesV2Model.

        Gets or sets allows the application to use speech recognition capabilities.  # noqa: E501

        :param speech_recognition: The speech_recognition of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._speech_recognition = speech_recognition

    @property
    def system_policy_desktop_folder(self):
        """Gets the system_policy_desktop_folder of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets allows the application access to files on the Desktop.  # noqa: E501

        :return: The system_policy_desktop_folder of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._system_policy_desktop_folder

    @system_policy_desktop_folder.setter
    def system_policy_desktop_folder(self, system_policy_desktop_folder):
        """Sets the system_policy_desktop_folder of this MacOsPrivacyPreferencesV2Model.

        Gets or sets allows the application access to files on the Desktop.  # noqa: E501

        :param system_policy_desktop_folder: The system_policy_desktop_folder of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._system_policy_desktop_folder = system_policy_desktop_folder

    @property
    def system_policy_documents_folder(self):
        """Gets the system_policy_documents_folder of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets allows the application access to files in Documents.  # noqa: E501

        :return: The system_policy_documents_folder of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._system_policy_documents_folder

    @system_policy_documents_folder.setter
    def system_policy_documents_folder(self, system_policy_documents_folder):
        """Sets the system_policy_documents_folder of this MacOsPrivacyPreferencesV2Model.

        Gets or sets allows the application access to files in Documents.  # noqa: E501

        :param system_policy_documents_folder: The system_policy_documents_folder of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._system_policy_documents_folder = system_policy_documents_folder

    @property
    def system_policy_downloads_folder(self):
        """Gets the system_policy_downloads_folder of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets allows the application access to files in Downloads.  # noqa: E501

        :return: The system_policy_downloads_folder of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._system_policy_downloads_folder

    @system_policy_downloads_folder.setter
    def system_policy_downloads_folder(self, system_policy_downloads_folder):
        """Sets the system_policy_downloads_folder of this MacOsPrivacyPreferencesV2Model.

        Gets or sets allows the application access to files in Downloads.  # noqa: E501

        :param system_policy_downloads_folder: The system_policy_downloads_folder of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._system_policy_downloads_folder = system_policy_downloads_folder

    @property
    def system_policy_network_volumes(self):
        """Gets the system_policy_network_volumes of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets allows the application access to files on Network Volumes.  # noqa: E501

        :return: The system_policy_network_volumes of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._system_policy_network_volumes

    @system_policy_network_volumes.setter
    def system_policy_network_volumes(self, system_policy_network_volumes):
        """Sets the system_policy_network_volumes of this MacOsPrivacyPreferencesV2Model.

        Gets or sets allows the application access to files on Network Volumes.  # noqa: E501

        :param system_policy_network_volumes: The system_policy_network_volumes of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._system_policy_network_volumes = system_policy_network_volumes

    @property
    def system_policy_removable_volumes(self):
        """Gets the system_policy_removable_volumes of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets allows the application access to files on Removable Volumes.  # noqa: E501

        :return: The system_policy_removable_volumes of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._system_policy_removable_volumes

    @system_policy_removable_volumes.setter
    def system_policy_removable_volumes(self, system_policy_removable_volumes):
        """Sets the system_policy_removable_volumes of this MacOsPrivacyPreferencesV2Model.

        Gets or sets allows the application access to files on Removable Volumes.  # noqa: E501

        :param system_policy_removable_volumes: The system_policy_removable_volumes of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._system_policy_removable_volumes = system_policy_removable_volumes

    @property
    def apple_events(self):
        """Gets the apple_events of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets allows the application to send a restricted AppleEvent to another process. Must be either Allow or Disallow.  # noqa: E501

        :return: The apple_events of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._apple_events

    @apple_events.setter
    def apple_events(self, apple_events):
        """Sets the apple_events of this MacOsPrivacyPreferencesV2Model.

        Gets or sets allows the application to send a restricted AppleEvent to another process. Must be either Allow or Disallow.  # noqa: E501

        :param apple_events: The apple_events of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._apple_events = apple_events

    @property
    def ae_receiver_identifier(self):
        """Gets the ae_receiver_identifier of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets the identifier of the process receiving an AppleEvent sent by the Identifier process.  # noqa: E501

        :return: The ae_receiver_identifier of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._ae_receiver_identifier

    @ae_receiver_identifier.setter
    def ae_receiver_identifier(self, ae_receiver_identifier):
        """Sets the ae_receiver_identifier of this MacOsPrivacyPreferencesV2Model.

        Gets or sets the identifier of the process receiving an AppleEvent sent by the Identifier process.  # noqa: E501

        :param ae_receiver_identifier: The ae_receiver_identifier of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._ae_receiver_identifier = ae_receiver_identifier

    @property
    def ae_receiver_identifier_type(self):
        """Gets the ae_receiver_identifier_type of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets the type of AEReceiverIdentifier value. Must be either bundleID or path.  # noqa: E501

        :return: The ae_receiver_identifier_type of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._ae_receiver_identifier_type

    @ae_receiver_identifier_type.setter
    def ae_receiver_identifier_type(self, ae_receiver_identifier_type):
        """Sets the ae_receiver_identifier_type of this MacOsPrivacyPreferencesV2Model.

        Gets or sets the type of AEReceiverIdentifier value. Must be either bundleID or path.  # noqa: E501

        :param ae_receiver_identifier_type: The ae_receiver_identifier_type of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._ae_receiver_identifier_type = ae_receiver_identifier_type

    @property
    def ae_receiver_code_requirement(self):
        """Gets the ae_receiver_code_requirement of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets code requirement for the receiving binary.  # noqa: E501

        :return: The ae_receiver_code_requirement of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._ae_receiver_code_requirement

    @ae_receiver_code_requirement.setter
    def ae_receiver_code_requirement(self, ae_receiver_code_requirement):
        """Sets the ae_receiver_code_requirement of this MacOsPrivacyPreferencesV2Model.

        Gets or sets code requirement for the receiving binary.  # noqa: E501

        :param ae_receiver_code_requirement: The ae_receiver_code_requirement of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: str
        """

        self._ae_receiver_code_requirement = ae_receiver_code_requirement

    @property
    def apple_events_list(self):
        """Gets the apple_events_list of this MacOsPrivacyPreferencesV2Model.  # noqa: E501

        Gets or sets apple Events list.  # noqa: E501

        :return: The apple_events_list of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :rtype: list[AppleEvent]
        """
        return self._apple_events_list

    @apple_events_list.setter
    def apple_events_list(self, apple_events_list):
        """Sets the apple_events_list of this MacOsPrivacyPreferencesV2Model.

        Gets or sets apple Events list.  # noqa: E501

        :param apple_events_list: The apple_events_list of this MacOsPrivacyPreferencesV2Model.  # noqa: E501
        :type: list[AppleEvent]
        """

        self._apple_events_list = apple_events_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MacOsPrivacyPreferencesV2Model, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MacOsPrivacyPreferencesV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MacOsPrivacyPreferencesV2Model):
            return True

        return self.to_dict() != other.to_dict()
