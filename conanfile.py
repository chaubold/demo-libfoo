from conans import ConanFile, CMake, tools


class LibfooConan(ConanFile):
    name = "libfoo"
    version = "0.2"
    license = "<Put the package license here>"
    author = "Carsten Haubold <carstenhaubold@googlemail.com>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Libfoo here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "libfoo/*"

    def build(self):
        cmake = CMake(self, generator="Unix Makefiles")
        cmake.configure(source_folder="libfoo")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include/libfoo", src="libfoo/include/libfoo")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["libfoo"]

