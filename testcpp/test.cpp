#include <stdio.h>
#include <windows.h>
typedef int(__cdecl *AddFunc)(int,int);
int main(){
    HINSTANCE hDll = LoadLibrary("math_operations.dll");
    if(!hDll){
        printf("错误加载 DLL");
        return 1;
    }
    AddFunc add = (AddFunc)GetProcAddress(hDll,"addInt");
    if(!add){
        printf("错误加载函数");
        return 2;
    }
    int result = add(5,7);
    printf("5+7=%d\n",result);
    return 0;
}