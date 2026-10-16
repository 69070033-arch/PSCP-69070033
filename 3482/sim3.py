import subprocess
attacks = ['1','2','2','3','1','3','3','2','1','2','1']
p = subprocess.Popen(['python','main.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
p.stdin.write("\n".join(attacks) + "\n")
p.stdin.flush()
print(p.stdout.read())
