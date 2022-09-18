import mysql.connector 
mydb=mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password="1234", 
    database="booking" 
) 
mycursor=mydb.cursor() 
print("welcom to GREAT KIRIKALAN travel's")
print("*custormers statisfaction our first priority*")
# iam direct create my sql server create table and and database 
def select_root(passenger_name,gender,age,aadharno,adult,child,no_of_ticket,ticket_price,start_trip,end_trip,onwarddate):
    sql="INSERT into ticket(passenger_name,gender,age,aadharno,adult,child,no_of_ticket,ticket_price,start_trip,end_trip,onwarddate)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=passenger_name,gender,age,aadharno,adult,child,no_of_ticket,ticket_price,start_trip,end_trip,onwarddate
    mycursor.execute(sql,val)
    mydb.commit()  
    print("data inserted successfully")
def view_data(ticketno):
    mycursor.execute("select * from ticket where ticketno=%s",(ticketno,)) 
    result=mycursor.fetchone() 
    for i in result: 
        print(i)
def modify_data(passenger_name,gender,age,aadharno,adult,child,no_of_ticket,ticket_price,start_trip,end_trip,onwarddate,ticketno):
    sql="update ticket set passenger_name=%s,gender=%s,age=%s,aadharno=%s,adult=%s,child=%s,no_of_ticket=%s,ticket_price=%s,start_trip=%s,end_trip=%s,onwarddate=%s WHERE ticketno=%s"
    val=passenger_name,gender,age,aadharno,adult,child,no_of_ticket,ticket_price,start_trip,end_trip,onwarddate,ticketno
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
def booking_cancel(ticketno):
    mycursor.execute("DELETE FROM ticket where ticketno=%s",(ticketno,))
    mydb.commit()
    print("deleted successfully")
def modify_name(passenger_name,ticketno):
    sql="update ticket set passenger_name=%s WHERE ticketno=%s"
    val=passenger_name,ticketno
    mycursor.execute(sql,val)
    mydb.commit()
    print("updated")
def modify_gender(gender,ticketno):
    sql="update ticket set gender=%s WHERE ticketno=%s"
    val=gender,ticketno
    mycursor.execute(sql,val)
    mydb.commit()
    print("updated")
def modify_age(age,ticketno):
    sql="update ticket set age=%s WHERE ticketno=%s"
    val=age,ticketno
    mycursor.execute(sql,val)
    mydb.commit()
    print("updated")
def modify_aadharno(aadharno,ticketno):
    sql="update ticket set aadharno=%s WHERE ticketno=%s"
    val=aadharno,ticketno
    mycursor.execute(sql,val)
    mydb.commit()
    print("updated")
def modify_adult(adult,ticketno):
    sql="update ticket set adult=%s WHERE ticketno=%s"
    val=adult,ticketno
    mycursor.execute(sql,val)
    mydb.commit()
    print("updated")
def modify_child(child,ticketno):
    sql="update ticket set child=%s WHERE ticketno=%s"
    val=child,ticketno
    mycursor.execute(sql,val)
    mydb.commit()
    print("updated")
def modify_no_of_ticket(no_of_ticket,ticketno):
    sql="update ticket set no_of_ticket=%d WHERE ticketno=%s"
    val=no_of_ticket,ticketno
    mycursor.execute(sql,val)
    mydb.commit()
    print("updated")
def modify_ticket_price(ticket_price,ticketno):
    sql="update ticket set ticket_price=%s WHERE ticketno=%s"
    val=ticket_price,ticketno
    mycursor.execute(sql,val)
    mydb.commit()
    print("updated")
def modify_start_trip(start_trip,ticketno):
    sql="update ticket set start_trip=%s WHERE ticketno=%s"
    val=start_trip,ticketno
    mycursor.execute(sql,val)
    mydb.commit()
    print("updated")
def modify_end_trip(end_trip,ticketno):
    sql="update ticket set end_trip=%s WHERE ticketno=%s"
    val=end_trip,ticketno
    mycursor.execute(sql,val)
    mydb.commit()
    print("updated")
def modify_onwarddate(onwarddate,ticketno):
    sql="update ticket set onwarddate=%s WHERE ticketno=%s"
    val=onwarddate,ticketno
    mycursor.execute(sql,val)
    mydb.commit()
    print("updated")


print("book your  tickets")
print("passenger==1 for ticket booking")
print("passenger==2 for modify your booking")
print("passenger==3 for canceling the booking")
print("passenger==4 is if you wanna see your booked details")
passenger=int(input("enter your number:"))
if passenger==1:
    destination=["kovai","pudukkottai","trichy","madurai","thanjavur"]
    print(f"{destination}_our drop points")
    your_booking=input("enter your destination:").lower().strip()
    if your_booking in destination:
        startpoint=["koyambadu","thambaram","ashokpiller","velacherry","vadapalani"]
        print(f"[{startpoint}]these all are our startpoint's")
        travel_start_from=input("enter your start point:").lower().strip()
        if  travel_start_from in startpoint:
            available_sheets_in_bus=20
            ticketprice=500
            print(f"available tickets_{available_sheets_in_bus}")
            how_many_tickets_you_want=int(input("pleace enter how many tickets you want:"))
            if available_sheets_in_bus <= available_sheets_in_bus:
                your_ticket_amount=ticketprice*how_many_tickets_you_want
                traveldate=input("enter your travel date:").lower().strip()
                print(f"your_ticket_price is:{your_ticket_amount}")
                print("successfully ticket booked")
                passenger_name=input("enter your passenger_name:").lower().strip()
                gender=input("enter your gender:").lower().strip()
                age=int(input("enter your age:"))
                aadharno=int(input("enter your aadharno:"))
                adult=input("enter your adult[yes or no only]:").lower().strip()
                child=input("enter your child[yes or no only]:").lower().strip()
                no_of_ticket=how_many_tickets_you_want
                ticket_price=your_ticket_amount
                start_trip=travel_start_from       
                end_trip=your_booking        
                onwarddate=traveldate 
                select_root(passenger_name,gender,age,aadharno,adult,child,no_of_ticket,ticket_price,start_trip,end_trip,onwarddate)
            else:
                print("not available")
        else:
            print("not available sorry")
    else:
        print("sorry your startpoint(pickep point) not in our root")  
elif passenger==2:
    print("if you want modify all.enter[modify_all]")
    print("other wise specify what you want")
    want_to_modify=input("enter what you to  modify:").lower().strip()
    if want_to_modify=="modify_all":
        passenger_name=input("enter your passenger_name:").lower().strip()
        gender=input("enter your gender:").lower().strip()
        age=int(input("enter your age:"))
        aadharno=int(input("enter your aadharno:"))
        adult=input("enter your adult:").lower().strip()
        child=input("enter your child:").lower().strip()
        no_of_ticket=int(input("enter your no_of_ticket:"))
        ticket_price=int(input("enter your ticket_price:"))
        start_trip=input("enter your start_trip:").lower().strip()        
        end_trip=input("enter your end_trip:").lower().strip()      
        onwarddate=input("enter your onwarddate:").lower().strip()
        ticketno=int(input("enter your ticketno:"))
        modify_data(passenger_name,gender,age,aadharno,adult,child,no_of_ticket,ticket_price,start_trip,end_trip,onwarddate,ticketno)
    elif want_to_modify=="passenger_name":
        passenger_name=input("enter your passenger_name:").lower().strip()
        ticketno=int(input("enter your ticketno:"))
        modify_name(passenger_name,ticketno)
    elif want_to_modify=="gender":
        gender=input("enter your gender:").lower().strip()
        ticketno=int(input("enter your ticketno:"))
        modify_gender(gender,ticketno)
    elif want_to_modify=="age":
        age=int(input("enter your age:"))
        ticketno=int(input("enter your ticketno:"))
        modify_age(age,ticketno)
    elif want_to_modify=="aadharno":
        aadharno=int(input("enter your aadharno:"))
        ticketno=int(input("enter your ticketno:"))
        modify_aadharno(aadharno,ticketno)
    elif want_to_modify=="adult":
        adult=input("enter your adult:").lower().strip()
        ticketno=int(input("enter your ticketno:"))
        modify_adult(adult,ticketno)
    elif want_to_modify=="child":
        child=input("enter your child:").lower().strip()
        ticketno=int(input("enter your ticketno:"))
        modify_child(child,ticketno)
    elif want_to_modify=="no_of_ticket":
        no_of_ticket=int(input("enter your no_of_ticket:"))
        ticketno=int(input("enter your ticketno:"))
        modify_no_of_ticket(no_of_ticket,ticketno)
    elif want_to_modify=="ticket_price":
        ticket_price=int(input("enter your ticket_price:"))
        ticketno=int(input("enter your ticketno:"))
        modify_ticket_price(ticket_price,ticketno)
    elif want_to_modify=="start_trip":
        start_trip=input("enter your start_trip:").lower().strip()
        ticketno=int(input("enter your ticketno:"))
        modify_start_trip(start_trip,ticketno)
    elif want_to_modify=="end_trip":
        end_trip=input("enter your end_trip:").lower().strip()
        ticketno=int(input("enter your ticketno:"))
        modify_end_trip(end_trip,ticketno)
    elif want_to_modify=="onwarddate":
        onwarddate=input("enter your onwarddate:").lower().strip()
        ticketno=int(input("enter your ticketno:"))
        modify_onwarddate(onwarddate,ticketno)
    else:
        print("give properly")
elif passenger==3:
    ticketno=int(input("enter your ticketno:"))
    booking_cancel(ticketno)
elif passenger==4:
    ticketno=int(input("enter your ticketno:"))
    view_data(ticketno)
else:
        print("sorry try next time")  
