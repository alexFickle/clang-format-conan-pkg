from conans import ConanFile, CMake, tools

class ClangFormatConanFile(ConanFile):
    name = "clang_format"
    version = "13.0.0"
    license = "Apache-2.0 with LLVM Exceptions"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports = "LICENSE"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/llvm/llvm-project.git", branch="llvmorg-13.0.0", shallow=True)
    
    def build(self):
        cmake = CMake(self)
        cmake.definitions["LLVM_ENABLE_PROJECTS"] = "clang"
        cmake.definitions["CLANG_BUILD_TOOLS"] = "ON"
        cmake.configure(source_folder="llvm")
        cmake.build(target="clang-format")

    def package(self):
        self.copy("clang-format*", src="bin", dst="bin")
        self.copy("LICENSE.TXT", src="clang", dst="licenses")
    
    def package_id(self):
        del self.info.settings.compiler
        del self.info.settings.build_type
