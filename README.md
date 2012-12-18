$ gcc mywin.c -L. -lbinding_test   -lcef_dll -licudt_dll -lglesv2_dll -legl_dll
 -ld3dx9_43_dll -ld3dcompiler_43_dll  -lstdc++  -lcomctl32 -Wl,--subsystem,wind
ows -lcomdlg32 -lshell32 -luser32 -lkernel32 -lgdi32 -loleaut32


$ hbmk2  -trace test.prg -L. -lbinding_test   -lcef_dll -licudt_dll -lglesv2_dl
l -legl_dll -ld3dx9_43_dll -ld3dcompiler_43_dll -lstdc++  -lgtwvt
hbmk2: Processing environment options: -compiler=mingw
hbmk2: Harbour compiler command (embedded):
(c:\knowhowERP\hbout\bin\harbour.exe) -n2 test.prg -oc:\tmp\hbmk_kax44n.dir\ -ic
:\knowhowERP\hbout\include
Harbour 3.2.0dev (Rev. 17443)
Copyright (c) 1999-2012, http://harbour-project.org/
Compiling 'test.prg'...
Lines 8, Functions/Procedures 1
Generating C source output to 'c:\tmp\hbmk_kax44n.dir\test.c'... Done.
hbmk2: C/C++ compiler command:
gcc.exe -c -O3 -march=i586 -mtune=pentiumpro -fomit-frame-pointer  -W -Wall -pip
e -Ic:/knowhowERP/hbout/include c:/tmp/hbmk_kax44n.dir/test.c c:/tmp/hbmk_y07yab
.c
hbmk2: Linker command:
gcc.exe c:/tmp/hbmk_kax44n.dir/test.o c:/tmp/hbmk_kax44n.dir/hbmk_y07yab.o    -m
console -Wl,--start-group -lbinding_test -lcef_dll -licudt_dll -lglesv2_dll -leg
l_dll -ld3dx9_43_dll -ld3dcompiler_43_dll -lstdc++ -lgtwvt -lhbextern -lhbdebug
-lhbvm -lhbrtl -lhblang -lhbcpage -lgtcgi -lgtpca -lgtstd -lgtwin -lgtwvt -lgtgu
i -lhbrdd -lhbuddall -lhbusrrdd -lrddntx -lrddcdx -lrddnsx -lrddfpt -lhbrdd -lhb
hsx -lhbsix -lhbmacro -lhbcplr -lhbpp -lhbcommon -lhbmainstd -lkernel32 -luser32
 -lgdi32 -ladvapi32 -lws2_32 -lwinspool -lcomctl32 -lcomdlg32 -lshell32 -luuid -
lole32 -loleaut32 -lmpr -lwinmm -lmapi32 -limm32 -lmsimg32 -lwininet -lhbpcre -l
hbzlib   -Wl,--end-group -otest.exe  -Lc:/knowhowERP/hbout/lib/win/mingw -Lc:/kn
owhowERP/hbout/bin -L.
