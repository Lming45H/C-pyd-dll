# setup.py
from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir
import pybind11

# 定义扩展模块
ext_modules = [
    Pybind11Extension(
        'simple_add',           # Python 中导入的名字
        ['simple_add.cpp'],     # 源文件列表
        include_dirs=[
            pybind11.get_include(),  # 确保能找到 pybind11 头文件
        ],
        language='c++',
        extra_compile_args=["/std:c++14", "/EHsc"],  # 只保留必要参数
    ),
]
class BuildExt(build_ext):
    def build_extensions(self):
        for ext in self.extensions:
            ext.extra_compile_args = ["/std:c++14", "/EHsc"]
        build_ext.build_extensions(self)
setup(
    name="simple_add",
    version="0.1",
    description="pybind11 module (add + hello, no garbled Chinese)",
    ext_modules=ext_modules,
    cmdclass={"build_ext": BuildExt},
    zip_safe=False,
)