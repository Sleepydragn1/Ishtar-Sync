for %%f in (.\*.ui) do (
     pyside6-uic %%f > ..\..\ishtar_sync\gui\%%~nf.py
)