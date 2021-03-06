# Copyright (c) 2006, Mayuresh Phadke
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#         * Redistributions of source code must retain the above copyright
#           notice, this list of conditions and the following disclaimer.
#         * Redistributions in binary form must reproduce the above copyright
#           notice, this list of conditions and the following disclaimer in the
# 	    documentation and/or other materials provided with the distribution.
#         * Neither the name of 'QualEx Systems' nor the names of its
# 	    contributors may be used to endorse or promote products derived from
# 	    this software without specific prior written permission.
# 
#         THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from distutils.core import setup

setup(	name = 'dhtfs',
	version = '0.2.0',
	packages = ['dhtfs'],
	scripts = ['scripts/addTags', 'scripts/mkfs.dhtfs', 'scripts/mount.dhtfs', 'scripts/delTags'],
	author = 'Mayuresh Phadke',
	author_email = 'mayuresh_phadke@qualexsystems.com',
	description = 'Tagging filesystem providing dynamic directory hierarchy using tags',
	long_description = 
	"""
	This package provides a Tagging File System.

	The file system presents dynamic directory hierarchies using tags associated with
	files in the file system.

	The file system is a layered FS developed using FUSE and the python-fuse plugin
	"""
	)
