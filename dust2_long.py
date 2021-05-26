import time
from keys import Keys
import csv
keys = Keys()
def mainloop():
    # THE FOLLOWING COMMAND HAS TO BE PUT INTO CONSOLE. It starts logging your console

    # con_logfile console.log
    keys.directKey("p")
    time.sleep(0.0002)
    keys.directKey("p", keys.key_release)
    try:
        # Read console.log and get the relevant data
        with open(r"C:/Program Files (x86)/Steam/steamapps/common/Counter-Strike Global Offensive/csgo/console.log",
                  "r") as f:
            lines = f.read().splitlines()

            last_line = lines[-1]

            print(last_line)

        if "first kill" in lines[-1] or "first kill" in lines[-2] or"first kill" in lines[-3] or"first kill" in lines[-4]:
            # kys
            print("OMG")
            print("OMG")
            print("OMG")
            keys.directKey("t")
            time.sleep(0.0002)
            keys.directKey("t", keys.key_release)
            time.sleep(2)

            with open(r"C:/Program Files (x86)/Steam/steamapps/common/Counter-Strike Global Offensive/csgo/console.log",
                      "r") as f:
                lines = f.read().splitlines()

                last_lines = lines[len(lines)-20:len(lines)]
                print(last_lines)
            for x in last_lines:
                if "Damage Given" in x:
                    print("HERE")
                    chunk = x.split("-")[1]
                    damage = chunk[:5].replace(" ","")
                    damage = damage[:5].replace("in", "")
                    print(damage)
                    if damage =="102":
                        HS = True
                        with open('longtaps.csv', 'a', newline='\n')as f:
                            thewriter = csv.writer(f)
                            thewriter.writerow(["HEADSHOT"])
            time.sleep(2)
            keys.directKey("u")
            time.sleep(3)
            keys.directKey("j")
            time.sleep(0.003)
            keys.directKey("k")
            time.sleep(0.003)
            keys.directKey("l")
            time.sleep(0.003)
            keys.directKey("g")
            keys.directKey("h")
            keys.directKey("u", keys.key_release)
            keys.directKey("j", keys.key_release)
            keys.directKey("k", keys.key_release)
            keys.directKey("l", keys.key_release)
            keys.directKey("g", keys.key_release)
            keys.directKey("h", keys.key_release)
            time.sleep(2)

        splitted = last_line.split(";")

        coords = splitted[0]
        coords = coords.split(" ")
        angles = splitted[1]
        angles = angles.split(" ")

        class coordinates:
            X = coords[1]
            Z = coords[2]
            Y = coords[3]
            vertical = angles[1]
            horizontal = angles[2]

        print(coordinates.X)
        if float(coordinates.X) > 1462:
            keys.directKey("y")
            time.sleep(0.0001)
            keys.directKey("y", keys.key_release)
            keys.directKey("h")
            keys.directKey("g")
            keys.directKey("h", keys.key_release)
            keys.directKey("g", keys.key_release)
            time.sleep(0.01)
            with open('longtaps.csv','a',newline='\n')as f:
                thewriter = csv.writer(f)
                thewriter.writerow(["Round"])

            return coordinates
            # SAFETY key will stop the bot
    except:
        pass


print("pass")

time.sleep(1)
with open(r"C:/Program Files (x86)/Steam/steamapps/common/Counter-Strike Global Offensive/csgo/console.log","w") as f:
    f.close()
while True:
    mainloop()
    keys.directKey("d")

