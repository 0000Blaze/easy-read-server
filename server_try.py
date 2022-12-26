
def printStdoutLog(process):
    #print stdout
    print("Outputs: ")
    while True:
        line = process.stdout.readline()
        if not line:
            break
        print(line.decode('utf-8'))

def printStderrLog(process):
    print("Errors: ")
    while True:
        line = process.stderr.readline()
        if not line:
            break
        print(line.decode('utf-8'))

