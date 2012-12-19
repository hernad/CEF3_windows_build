# Copyright (c) 2011 The Chromium Embedded Framework Authors. All rights
# reserved. Use of this source code is governed by a BSD-style license that
# can be found in the LICENSE file.

{
  'includes': [
    # Bring in the autogenerated source file lists.
    'cef_paths.gypi',
   ],
  'variables': {
    'includes_common': [
      'include/cef_base.h',
      'include/cef_nplugin.h',
      'include/cef_runnable.h',
      'include/cef_version.h',
      'include/internal/cef_build.h',
      'include/internal/cef_export.h',
      'include/internal/cef_nplugin_types.h',
      'include/internal/cef_ptr.h',
      'include/internal/cef_string.h',
      'include/internal/cef_string_list.h',
      'include/internal/cef_string_map.h',
      'include/internal/cef_string_multimap.h',
      'include/internal/cef_string_types.h',
      'include/internal/cef_string_wrappers.h',
      'include/internal/cef_time.h',
      'include/internal/cef_tuple.h',
      'include/internal/cef_types.h',
      'include/internal/cef_types_wrappers.h',
      '<@(autogen_cpp_includes)',
    ],
    'includes_capi': [
      'include/capi/cef_base_capi.h',
      'include/capi/cef_nplugin_capi.h',
      '<@(autogen_capi_includes)',
    ],
    'includes_wrapper': [
      'include/wrapper/cef_byte_read_handler.h',
      'include/wrapper/cef_xml_object.h',
      'include/wrapper/cef_zip_archive.h',
    ],
    'includes_win': [
      'include/internal/cef_types_win.h',
      'include/internal/cef_win.h',
    ],
    'includes_mac': [
      'include/cef_application_mac.h',
      'include/internal/cef_mac.h',
      'include/internal/cef_types_mac.h',
    ],
    'includes_linux': [
      'include/internal/cef_linux.h',
      'include/internal/cef_types_linux.h',
    ],
    'libcef_sources_common': [
      'libcef_dll/cef_logging.h',
      'libcef_dll/cpptoc/cpptoc.h',
      'libcef_dll/ctocpp/ctocpp.h',
      'libcef_dll/libcef_dll.cc',
      'libcef_dll/libcef_dll2.cc',
      'libcef_dll/resource.h',
      'libcef_dll/transfer_util.cpp',
      'libcef_dll/transfer_util.h',
      '<@(autogen_library_side)',
    ],
    'libcef_dll_wrapper_sources_common': [
      'libcef_dll/cef_logging.h',
      'libcef_dll/cpptoc/base_cpptoc.h',
      'libcef_dll/cpptoc/cpptoc.h',
      'libcef_dll/ctocpp/base_ctocpp.h',
      'libcef_dll/ctocpp/ctocpp.h',
      'libcef_dll/transfer_util.cpp',
      'libcef_dll/transfer_util.h',
      'libcef_dll/wrapper/cef_byte_read_handler.cc',
      'libcef_dll/wrapper/cef_xml_object.cc',
      'libcef_dll/wrapper/cef_zip_archive.cc',
      'libcef_dll/wrapper/libcef_dll_wrapper.cc',
      'libcef_dll/wrapper/libcef_dll_wrapper2.cc',
      '<@(autogen_client_side)',
    ],
    'cefclient_sources_common': [
      'cefclient/binding_test.cpp',
      'cefclient/binding_test.h',
      'cefclient/cefclient.cpp',
      'cefclient/cefclient.h',
      'cefclient/cefclient_switches.cpp',
      'cefclient/cefclient_switches.h',
      'cefclient/client_handler.cpp',
      'cefclient/client_handler.h',
      'cefclient/client_popup_handler.cpp',
      'cefclient/client_popup_handler.h',
      'cefclient/download_handler.cpp',
      'cefclient/download_handler.h',
      'cefclient/extension_test.cpp',
      'cefclient/extension_test.h',
      'cefclient/res/domaccess.html',
      'cefclient/res/extensionperf.html',
      'cefclient/res/localstorage.html',
      'cefclient/res/logo.png',
      'cefclient/res/xmlhttprequest.html',
      'cefclient/resource_util.h',
      'cefclient/scheme_test.cpp',
      'cefclient/scheme_test.h',
      'cefclient/string_util.cpp',
      'cefclient/string_util.h',
      'cefclient/util.h',
    ],
    'cefclient_sources_win': [
      'cefclient/cefclient.rc',
      'cefclient/cefclient_win.cpp',
      'cefclient/client_handler_win.cpp',
      'cefclient/clientplugin.cpp',
      'cefclient/clientplugin.h',
      'cefclient/osrenderer.cpp',
      'cefclient/osrenderer.h',
      'cefclient/osrplugin.cpp',
      'cefclient/osrplugin.h',
      'cefclient/osrplugin_test.cpp',
      'cefclient/osrplugin_test.h',
      'cefclient/plugin_test.cpp',
      'cefclient/plugin_test.h',
      'cefclient/Resource.h',
      'cefclient/res/cefclient.ico',
      'cefclient/res/logoball.png',
      'cefclient/res/modaldialog.html',
      'cefclient/res/modalmain.html',
      'cefclient/res/osrplugin.html',
      'cefclient/res/small.ico',
      'cefclient/res/transparency.html',
      'cefclient/res/uiplugin.html',
      'cefclient/resource_util_win.cpp',
      'cefclient/uiplugin.cpp',
      'cefclient/uiplugin.h',
      'cefclient/uiplugin_test.cpp',
      'cefclient/uiplugin_test.h',
    ],
    'cefclient_sources_mac': [
      'cefclient/cefclient_mac.mm',
      'cefclient/client_handler_mac.mm',
      'cefclient/osrenderer.cpp',
      'cefclient/osrenderer.h',
      'cefclient/osrtest_mac.h',
      'cefclient/osrtest_mac.mm',
      'cefclient/resource_util_mac.mm',
    ],
    'cefclient_bundle_resources_mac': [
      'cefclient/mac/cefclient.icns',
      'cefclient/mac/English.lproj/InfoPlist.strings',
      'cefclient/mac/English.lproj/MainMenu.xib',
      'cefclient/mac/Info.plist',
      'cefclient/res/domaccess.html',
      'cefclient/res/extensionperf.html',
      'cefclient/res/localstorage.html',
      'cefclient/res/logo.png',
      'cefclient/res/logoball.png',
      'cefclient/res/osrtest.html',
      'cefclient/res/transparency.html',
      'cefclient/res/xmlhttprequest.html',
    ],
    'cefclient_sources_linux': [
      'cefclient/cefclient_gtk.cpp',
      'cefclient/client_handler_gtk.cpp',
      'cefclient/resource_util_linux.cpp',
    ],
    'cefclient_bundle_resources_linux': [
      'cefclient/res/domaccess.html',
      'cefclient/res/extensionperf.html',
      'cefclient/res/localstorage.html',
      'cefclient/res/logo.png',
      'cefclient/res/xmlhttprequest.html',
    ],
  },
}
