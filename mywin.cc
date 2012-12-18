#include <windows.h>
#include <commdlg.h>
#include <shellapi.h>

#include "win32_gui/include/resource.h"

//#include "cefclient/cefclient.h"
#include <stdio.h>
//#include <cstdlib>
//#include <sstream>
#include <string.h>
/*
#include "include/cef_app.h"
#include "include/cef_browser.h"
#include "include/cef_command_line.h"
#include "include/cef_frame.h"
#include "include/cef_runnable.h"
#include "include/cef_web_plugin.h"
#include "include/cef_web_urlrequest.h"
#include "cefclient/cefclient_switches.h"
#include "cefclient/client_handler.h"
#include "cefclient/binding_test.h"
#include "cefclient/string_util.h"
#include "cefclient/util.h"
*/
#include "include/cef_command_line.h"


/*
int WinMain2(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR  lpCmdLine, int  nCmdShow);

//int WinMain3(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow);					 
int WinMain4(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow);					 

		
		
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR  lpCmdLine, int  nCmdShow)
{

char s[20];

sprintf(s, "builrev cef:%d, instance:%d\n", cef_build_revision(), hInstance);
MessageBox(NULL, TEXT(s), TEXT("info"), MB_OK);

return WinMain2(hInstance, hPrevInstance, lpCmdLine,  nCmdShow);		
}
*/


int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
  //INITCOMMONCONTROLSEX icc;
  WNDCLASSEX wc;
  LPCTSTR MainWndClass = TEXT("MyWindows aplikacija");
  HWND hWnd;
  HACCEL hAccelerators;
  HMENU hSysMenu;
  MSG msg;

  // Initialise common controls.
  //icc.dwSize = sizeof(icc);
  //icc.dwICC = ICC_WIN95_CLASSES;
  //InitCommonControlsEx(&icc);

  // Class for our main window.
  wc.cbSize        = sizeof(wc);
  wc.style         = 0;
  //wc.lpfnWndProc   = &MainWndProc;
  wc.lpfnWndProc = &DefWindowProc; //(hWnd, msg, wParam, lParam);

  wc.cbClsExtra    = 0;
  wc.cbWndExtra    = 0;
  wc.hInstance     = hInstance;
  wc.hIcon         = (HICON) LoadImage(hInstance, MAKEINTRESOURCE(IDI_APPICON), IMAGE_ICON, 0, 0, LR_SHARED);
  wc.hCursor       = (HCURSOR) LoadImage(NULL, IDC_ARROW, IMAGE_CURSOR, 0, 0, LR_SHARED);
  wc.hbrBackground = (HBRUSH) (COLOR_BTNFACE + 1);
  wc.lpszMenuName  = MAKEINTRESOURCE(IDR_MAINMENU);
  wc.lpszClassName = MainWndClass;
  wc.hIconSm       = (HICON) LoadImage(hInstance, MAKEINTRESOURCE(IDI_APPICON), IMAGE_ICON, 16, 16, LR_SHARED);

  
  // Register our window classes, or error.
  if (! RegisterClassEx(&wc))
  {
    MessageBox(NULL, TEXT("Error registering window class."), TEXT("Error"), MB_ICONERROR | MB_OK);
    return 0;
  }
  
  
  // Create instance of main window.
  hWnd = CreateWindowEx(0, MainWndClass, MainWndClass, WS_OVERLAPPEDWINDOW, CW_USEDEFAULT, CW_USEDEFAULT,
                        320, 200, NULL, NULL, hInstance, NULL);

  // Error if window creation failed.
  if (! hWnd)
  {
    MessageBox(NULL, TEXT("Error creating main window."), TEXT("Error"), MB_ICONERROR | MB_OK);
    return 0;
  }

  
  CefRefPtr<CefCommandLine> g_command_line = CefCommandLine::CreateCommandLine();
  //g_command_line->InitFromString(::GetCommandLineW());
  
  // Load accelerators.
  //hAccelerators = LoadAccelerators(hInstance, MAKEINTRESOURCE(IDR_ACCELERATOR));

  // Add "about" to the system menu.
  //hSysMenu = GetSystemMenu(hWnd, FALSE);
  //InsertMenu(hSysMenu, 5, MF_BYPOSITION | MF_SEPARATOR, 0, NULL);
  //InsertMenu(hSysMenu, 6, MF_BYPOSITION, ID_HELP_ABOUT, TEXT("About"));

  // Show window and force a paint.
  ShowWindow(hWnd, nCmdShow);
  UpdateWindow(hWnd);

  // Main message loop.
  while(GetMessage(&msg, NULL, 0, 0) > 0)
  {
    //if (! TranslateAccelerator(msg.hwnd, hAccelerators, &msg))
    //{
      TranslateMessage(&msg);
      DispatchMessage(&msg);
    //}
  }

  return (int) msg.wParam;
  
}
