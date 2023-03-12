import subprocess

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

        
def runJavaProgram(programName, arguments):
    command = ["java", programName] + arguments
    # run the Java program
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # wait for the Java program to finish
    print("Waiting for",programName, "to finish")
    process.wait()
    # check the return code to see if the java process completed successfully
    if process.returncode != 0:
        print(programName,"failed with error code: ", process.returncode)
        printStderrLog(process)
        printStdoutLog(process)
    else:
        print(programName,"finished successfully")
        printStdoutLog(process)
