# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
 
# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install kincat
#
# You can edit this file again by typing:
#
#     spack edit kincat
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------
 
from spack.package import *

# THIS IS A DRAFT FOR USE WITH THE INTERNAL SANDIA REPOSITORY
# You have to edit some things by hand.  Once we push the HDF5-supporting version
# of KinCat to the public repo, we will publish a version of this to the official
# spack repository.
# Here are the steps for now:
# 1. Edit the "url" to be the file path of a .tar.gz that has the version of the git repository that you want to build.
# 2. Generate a SHA256 for that, and paste it in the "version" line below.
# 3. Edit the depends_on("kokkos…") line below to match the architectures you want.
#
# To generate a SHA1:
# shasum -a 256 /path/to/tar.gz
 
class Kincat(CMakePackage):
    """FIXME: Put a proper description of your package here."""
    
    root_cmakelists_dir = "src"
    homepage = "https://github.com/sandialabs/KinCat"
    url = "https://github.com/sandialabs/KinCat/archive/refs/tags/v1.1.1.tar.gz"
    maintainers("cjdanie")
    license("GPL-3.0-or-later")
    version('1.1.1', sha256="6ac368e85930b41d9a496eb0018215c142184c70dd2cf0d194f380975087cd6c")
    #version('1.1.0', sha256="a1b48e54563071f0c0e0b17dac11bc18cdb244b001999e2ea89c658b25b1cad8")
    
#    depends_on("kokkos+cuda+wrapper cuda_arch=80") # FIXME: make cuda/openmp optional, and require cuda_arch to be specified; see the kokkos package.py for syntax, etc. (+wrapper is required if cuda is requested, and we are not building with clang..)
    depends_on("kokkos")
    depends_on("boost@1.75")
#    depends_on("gtest")
    depends_on("hdf5 -mpi") 
    def cmake_args(self):
        spec = self.spec
        args = [
            #self.define_from_variant("BUILD_CODEC", "codec"),
            "-DKOKKOS_INSTALL_PATH:PATH=%s" % spec["kokkos"].prefix,
 #           "-DGTEST_INSTALL_PATH:PATH=%s" % spec["gtest"].prefix,
            "-DBOOST_INSTALL_PATH:PATH=%s" % spec["boost"].prefix,
            "-DKINCAT_ENABLE_VERBOSE=ON",
            "-DHDF5_INCLUDE_DIRS:PATH=%s" % spec["hdf5"].prefix + "/include",
            "-DHDF5_LIBRARY_DIRS:PATH=%s" % spec["hdf5"].prefix + "/lib",
            "-DHDF5_LIBRARIES=hdf5"
        ]
        return args
