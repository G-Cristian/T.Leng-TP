@echo off
SET /a GOODLEN = 2
SET /a GOODPASS = 0
SET /a GOODNOTPASS = 0
SET /a BADLEN = 2
SET /a BADPASS = 0
SET /a BADNOTPASS = 0

for /L %%A in (1,1,%GOODLEN% ) do (
  echo Good Test %%A
  del Outputs\exit_test_%%A.txt
  python parser_v2.py GoodTests\test_in_%%A.txt Outputs\exit_test_%%A.txt
  echo.
  if errorlevel 1 (
    SET /a GOODNOTPASS += 1
  ) else (
    fc GoodTests\test_out_%%A.txt Outputs\exit_test_%%A.txt
    echo.
    if errorlevel 1 (
      SET /a GOODNOTPASS += 1
    ) else (
      SET /a GOODPASS += 1
    )
  )
)
for /L %%A in (1,1,%BADLEN% ) do (
  echo Bad Test %%A
  del Outputs\exit_bad_test_%%A.txt
  python parser_v2.py BadTests\test_in_%%A.txt Outputs\exit_bad_test_%%A.txt
  echo.
  if errorlevel 1 (
    SET /a BADNOTPASS += 1
  ) else (
    SET /a BADPASS += 1
  )
)
echo Tests que tienen que funcionar %GOODLEN%
echo Tests que pasaron de archivos que tenian que funcionar %GOODPASS%
echo Tests que no pasaron de archivos que tenian que funcionar %GOODNOTPASS%
echo.
echo Tests que no tienen que funcionar %BADLEN%
echo Tests que pasaron de archivos que no tenian que funcionar %BADPASS%
echo Tests que no pasaron de archivos que no tenian que funcionar %BADNOTPASS%
echo.
if %GOODPASS% == %GOODLEN% (
  if %BADNOTPASS% == %BADLEN% (
    echo Pasaron los tests.
  ) else (
    echo No pasaron tests. Funcionaron programas que no tenian que funcionar.
  )
) else (
  echo No pasaron tests. No funcionaron programas que tenian que funcionar.
)
echo.
pause