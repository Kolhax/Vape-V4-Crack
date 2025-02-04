#include "Windows.h"
#include <cstdio> 

#define error(message) printf(message); system("pause"); ExitProcess(0);

int 
main(int argc, char* argv[])
{
    if (argc != 2)
        return -1;

    HMODULE kernel;
    LPVOID load_library, process_memory;

    printf("Cracked by Kangaroo Team in less than 2 minutes - vape.rip \n");

    _STARTUPINFOA si; memset(&si, 0, sizeof(si)); si.cb = sizeof(si);
    _PROCESS_INFORMATION pi; memset(&pi, 0, sizeof(pi));

    if (!CreateProcessA(NULL, argv[1], NULL, NULL, FALSE, CREATE_SUSPENDED, NULL, NULL, &si, &pi))
        return -1;

    kernel = GetModuleHandleA("kernel32.dll");
    if (!kernel)
        return -1;

    load_library = GetProcAddress(kernel, "LoadLibraryA");
    if (!load_library)
        return -1;

    process_memory = VirtualAllocEx(pi.hProcess, NULL, strlen("Kangaroo.dll"), MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE);
    if (!process_memory)
        return -1;

    if (!WriteProcessMemory(pi.hProcess, process_memory, "Kangaroo.dll", strlen("Kangaroo.dll"), NULL))
        return -1;

    if (!CreateRemoteThread(pi.hProcess, NULL, NULL, (LPTHREAD_START_ROUTINE)load_library, process_memory, NULL, NULL))
        return -1;

    if (!CloseHandle(pi.hProcess))
        return -1;

    if (ResumeThread(pi.hThread) == -1)
        return -1;

    return 0;
}
