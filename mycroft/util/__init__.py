# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Mycroft util library.

A collections of utils and tools for making skill development easier.
"""
from __future__ import absolute_import

import os

import mycroft.audio
from mycroft.util.format import nice_number

from .audio_utils import (find_input_device, play_audio_file, play_mp3,
                          play_ogg, play_wav, record)
from .file_utils import (create_file, curate_cache, ensure_directory_exists,
                         get_cache_directory, get_temp_path, read_dict,
                         read_stripped_lines, resolve_resource_file)
from .log import LOG
from .network_utils import connected
from .parse import extract_datetime, extract_number, normalize
from .platform import get_arch
from .process_utils import (create_daemon, create_echo_function,
                            reset_sigint_handler, start_message_bus_client,
                            wait_for_exit_signal)
from .signal import check_for_signal, create_signal, get_ipc_directory
from .string_utils import camel_case_split
