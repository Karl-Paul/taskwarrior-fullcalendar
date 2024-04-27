from subprocess import Popen, PIPE, STDOUT
#p = Popen(r"C:\Program Files (x86)\bin\bash.exe", '-c', '. /etc/profile;', stdin=PIPE, stdout=PIPE)
p = Popen([r"C:\Program Files (x86)\bin\bash.exe", '-c', '. /etc/profile; task export'], stdout=PIPE, stderr=STDOUT)
#p.stdin.write(b"ls")
#p.stdin.close()
out = p.stdout.read()
print(out)