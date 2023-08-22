def sum(t1 , t2):
    result = {}
    result["h"] = t1["h"] + t2["h"]
    result["m"] = t1["m"] + t2["m"]
    result["s"] = t1["s"] + t2["s"]
    if result ["s"] >= 60 :
        result["s"] -= 60 
        result["m"] += 1 
    if result["m"] >=60:
        result ["m"]-=60
        result ["h"]+= 1
    return result
    
    
def subtraction_time(t1 ,t2) :
    result= {}
    if t2["h"] > t1["h"]:
        time["h"]=t2["h"]-t1["h"]
        time["m"]=t2["m"]-t1["m"]
        time["s"]=t2["s"]-t1["s"]
        
    else :
        result["h"]=t1["h"] - t2["h"]
        result["m"]=t1["m"] - t2["m"]
        result["s"]=t1["s"] - t2["s"]
        
    if result["s"]<0 :
        result["m"]-=1 
        result["s"]+=60
        
    if result["m"]<0:
        result["h"]-=1
        result["m"]+=60
    
    if result["h"]<0 :
        print("we can't subtract")
        result={"h" : 0 , "m" :0 , "s" :0}
        
    return result   
        



def show(result):
    print(f"{result['h']} : {result ['m']} : {result['s']}")


def menu():
    print("enter ur entering time in 24-hour format : ")
    num1=float(input("hour  => "))
    num2=float(input("minute => "))
    num3=float(input("second  => "))
    print("enter the leaving time")
    num4=float(input("hour =>"))
    num5=float(input("minute =>"))
    num6=float(input("second =>"))
    print(f"the entering time is = {num1}:{num2}:{num3} and the exit time is= {num4}:{num5}:{num6}")
    t1={"h":num1 , "mi":num2 , "se":num3}
    t2={"h":num4 , "mi":num5 , "se":num6}
    print("you want to add or suntract time ? 1-add 2-suntract")
    user_input=int(input())
    if user_input ==1:
        show(add_time(t1,t2))
    elif user_input ==2:
        show(subtraction_time(t1,t2))
    else:
        print("wrong input")


# print(result_s)
menu()