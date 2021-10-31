def fun ():

    print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************""")
menu = [{
     "type" : "Appetizers",
      "list" : ["Wings","Cookies", "Spring Rolls"]
}
,{
     "type" : "Entrees",
      "list" : ["Salmon","Steak", "Meat Tornado","A Literal Garden"]
}
,{
     "type" : "Desserts",
      "list" : ["Ice Cream","Cake", "Pie"]
} 
,{
     "type" : "Drinks",
      "list" : ["Coffee","Tea", "Unicorn Tears"]
}]

""" print the menu """
for x in menu:
 print(x["type"])
 print("-----------")   
 for j in x["list"]:
       print(j)
       
 print("\n")
  



print("""***********************************
** What would you like to order? ** 
***********************************""")
order = str(input('> '))
orderList = []

while order !="quit" :   
  
  if order in orderList :
    my_order_num = {i:orderList.count(i) for i in orderList}
    count =my_order_num[order]
    print("\n")
    print("** "+ str(count+1)+  " order of " + str(order) +" have been added to your meal **")
    print("\n")
    orderList.append(order)

  else :
   orderList.append(order)  
   print("\n") 
   print("** 1 order of " + str(order) +" have been added to your meal **")   
   print("\n")
   
  print("""***********************************
   ** What would you like to order? ** 
   ***********************************""")
  order = str(input('> '))




"""this will call the function only form the terminal"""
if __name__=="__main__" : 
 fun()