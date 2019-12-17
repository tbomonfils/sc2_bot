:: C:\\Users\\Thibaud\\Anaconda3\\pythonw.exe start_prompt_mode.py
set PATH=%PATH%;C:\Program Files\Docker Toolbox;C:\Program Files\Mozilla Firefox
set VAR="token="

for /f "tokens=*" %%a in (config.txt) do (set %%a)

set cmd="ipconfig | findstr IPv4"
FOR /F "tokens=*" %%i IN (' %cmd% ') DO SET X=%%i
FOR /F "tokens=1,2,* delims=:" %%j IN ("%X%") DO (SET Y=%%k)
set DISPLAY=%Y:~1%:0.0

for /f "tokens=1,2,3 delims=/ " %%d in ('date /t') do set mydate=%%f%%e%%d
for /f "tokens=1,2* delims=: " %%d in ("%time%") do set mytime=%%d%%e
set host_logs_dir=C:\Users\Thibaud\Desktop\Leisure\starcraft_bot\logs\%mydate%_%mytime%_docker
set docker_logs_dir=/home/AI_core/app/logs/%mydate%_%mytime%_docker
mkdir %host_logs_dir%
set jupyter_logs_file=%host_logs_dir%\jupyter_logs.txt

docker-machine start default

start docker run -it --rm -p 8888:8888 -p 5000:5000 -p 6006:6006 -e DISPLAY=%DISPLAY% -e logs_path=%docker_logs_dir% -v /tmp/.X11-unix:/tmp/.X11-unix -v %host_path%:%docker_path% %docker_name%:%docker_tag%

set t=0

:TimerLoop
if %t% lss 13 (
	if exist %jupyter_logs_file% (
		for /f "usebackq delims=" %%a in (`type %jupyter_logs_file% ^|find %VAR%`) do (
			if "%%a" neq "" (
				for /f "tokens=1,2,* delims==" %%i in ("%%a") do (
					for /f "tokens=1,2,* delims= " %%p in ("%%j") do (
						firefox -new-tab http://127.0.0.1:8888/?token=%%p
						pause
						exit
					)
				)
			) else (
				echo %t% waiting 5 more seconds...
				timeout /NOBREAK /t 5
				set /a t=%t%+1
				goto TimerLoop
			)
		)
	) else (
		echo waiting 5 more seconds...
		timeout /NOBREAK /t 5
		set /a t=%t%+1
		goto TimerLoop
	)
) else (
	echo There is a problem with the docker starting process
	type %fichier%
)

pause