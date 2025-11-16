32位编译命令
g++ -O3 -Wall -shared -std=c++17 -fPIC -ID:/workSoftware/python32/include -ID:/workSoftware/python32/lib/site-packages/pybind11/include test.cpp -LD:/workSoftware/python32/libs -lpython311 -o simple_add.pyd





编译.dll命令
g++ -shared -o math_operations.dll math_operations.cpp -DMATHOPERATIONS_EXPORTS