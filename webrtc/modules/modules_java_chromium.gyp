# Copyright (c) 2013 The WebRTC project authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.  All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.

{
  'targets': [
    {
      'target_name': 'audio_device_module_java',
      'type': 'none',
      'variables': {
        'java_in_dir': 'audio_device/android/java',
      },
      'includes': [ '../../../build/java.gypi' ],
    }, # audio_device_module_java
  ],
}
