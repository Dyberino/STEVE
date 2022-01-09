@echo off
chcp 65001
cd D:\STEVE
:menu
cd D:\STEVE
cls
echo  ====================================================================
type  MENU.txt         
echo.                      
echo  ====================================================================                                                               
echo  Wybierz jedną z poniższych opcji wprowadzając odpowiednią cyfrę:                                
echo  1. Start
echo  2. Informacje o programie                                              
echo  3. Wyniki programu                                                
echo  4. Zakończ                                                                                             
echo  ====================================================================
echo.
set /p choice="Wybierz opcje[1-4]: "

IF %choice%==1 GOTO program
IF %choice%==2 GOTO info
IF %choice%==3 GOTO html
IF %choice%==4 GOTO exit


:program
cls
python main.py
python html.py

set CUR_HH=%TIME:~0,2%
if %CUR_HH% lss 10 (set CUR_HH=0%time:~1,1%)
set CUR_NN=%TIME:~3,2%
set CUR_SS=%TIME:~6,2%


cd raport
copy raport.html ..\backup\raport-%date%-%CUR_HH%.%CUR_NN%.%CUR_SS%.html | echo. && echo Backup wykonany pomyslnie, backup znajduje sie na dysku D w 
echo folderze STEVE\backup.
pause

GOTO :menu

:info
cls
echo.
echo  ==========================================================================
echo               INFORMACJE O PROGRAMIE I JEGO DZIALANIE               
echo  ==========================================================================
echo.
echo  Zadaniem programu Szachownica jest narysowanie w pliku .txt szachownicy
echo  która będzie zawierała na sobie narysowanego określonego koloru 
echo  piona, będzie się on znajdował w określonym miejscu na szachownicy, 
echo  dzięki tym danym program narysuje również na szachownicy symbol "x"
echo  w miejscach do których pion może się poruszyć. 
echo.
echo  W pliku wejściowym mamy zadane dane czyli:
echo  - kolor pionu (b - bialy, c - czarny)
echo  - rząd w krórym ma znajdować sie pion (1-8)
echo  - kolumnę w której ma znajdować sie pion (1-8)
echo  - symbol, który określa dany pion 
echo.
echo  Program na podstawie tych danych narysuje w pliku .txt szachownice
echo  wraz z zaznaczonymi możliwymi ruchami.
echo  ==========================================================================
echo                               DANE WEJSCIOWE               
echo.
echo   Dane wejściowe są zapisane w folderze input, dla każdego zestawu
echo   danych mamy osobny plik o nazwie file{i}.txt, gdzie i to numer
echo   nadany dla pliku
echo.   
echo   Przykladowy zestaw wyglada następująco:
echo. 
echo   b 3 6 h
echo.
echo   W ten sam sposób zapisany jest każdy plik wejściowy.
echo.
echo.
echo  ==========================================================================
echo                          DANE WYJSCIOWE               
echo   Dane wyjściowe sa zapisywane w folderze output, dla każdego zestawu
echo   mamy osobny plik wyjściowy output{i}.txt, gdzie i to numer nadany
echo   dla pliku.
echo.
echo   W każdym pliku zapisana jest szachownica wraz z postawionymi na niej 
echo   odpowienimi znakami.
echo  ==========================================================================
echo  Autor programu: Piotr Dyba, Informatyka II rok, grupa: 4G
echo.
echo.
pause
GOTO :menu

:html
cd D:\STEVE\raport
raport.html


:exit
exit