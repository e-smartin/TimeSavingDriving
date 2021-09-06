
def main():
    try:
        d = float(input("Introduce the distance\n"))
        s1 = float(input("Introduce the first speed\n")) 
        s2 = float(input("Introduce the second speed\n")) 
        
        t1 = d/s1 *3600
        t2 = d/s2 *3600
        delta = t1 - t2 if t1 >= t2 else t2 - t1 
        result = TimeHMS(delta)
        stringSpeed = "%.2f to %.2f" % (s1,s2) if s1 < s2 else "%.2f to %.2f" % (s2,s1)
        print(f"In {d}km you'll win {result[0]} hours, {result[1]} minutes and {result[2]} seconds by increasing your average speed from {stringSpeed}.")
    except Exception as e:
        print("You need to introduce 3 numbers")
        print(e)
            


def TimeHMS(tiempo_sec):
    
    tiempo_min_now = int(int(tiempo_sec)/60)
    tiempo_sec_now = int(int(tiempo_sec)%60)
    tiempo_hor_now = int(tiempo_min_now/60)
    tiempo_min_now = int(tiempo_min_now%60)
    return[tiempo_hor_now, tiempo_min_now, tiempo_sec_now] 




if __name__ == "__main__":
    main()
