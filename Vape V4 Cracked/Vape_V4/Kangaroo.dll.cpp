#include <Windows.h>
#include <string>
#include "MinHook.h"

DWORD64 base_address = 0;

typedef void *(*Connection)(void*, void*, std::string*, void*);
Connection original_connection = NULL;

void *
connection_hook(void* arg1, void* arg2, std::string *addr, void* arg4)
{
	*addr = "ws://localhost:8080";
	return original_connection(arg1, arg2, addr, arg4);
}

typedef BOOL (*AC)(void);
AC original_allocconsole = NULL;

BOOL 
allocconsole_hook()
{
	base_address = reinterpret_cast<DWORD64>(GetModuleHandleA("Vape_V4.exe"));

	MH_Initialize();

	Connection real_connection = (Connection)reinterpret_cast<LPVOID>((base_address + 0x89c80));
	MH_CreateHook(real_connection, &connection_hook, (void**)&original_connection);
	MH_EnableHook(real_connection);

	MH_DisableHook(&AllocConsole);

	return original_allocconsole();
}

BOOL
DllMain(HMODULE module, DWORD call_reason, LPVOID reserved) {
	if (call_reason == DLL_PROCESS_ATTACH)
	{
		if (!GetModuleHandleA("kernel32.dll")) LoadLibraryA("kernel32.dll");

		MH_Initialize();
		MH_CreateHook(&AllocConsole, &allocconsole_hook, (void**)&original_allocconsole);
		MH_EnableHook(&AllocConsole);
	}
	return TRUE;
}
