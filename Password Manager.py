import os
import stdiomask
import datetime
from tabulate import tabulate
import mysql.connector
print("|1111111|    |11|    |1111111| |1111111| |1|  |1|1|  |1|   |0000|   |1111111|  |111111|     ")
print("|1|   |1|   |1||1|   |1|   |1| |1|   |1| |1|   |1|   |1|  |0|  |0|  |1|   |1|  |1|    |1|   ")
print("|1|   |1|  |1|  |1|  |1|       |1|       |1|   |1|   |1| |0|    |0| |1|  |1|   |1|     |1|  ")
print("|1111111| |11111111| |1111111| |1111111| |1|   |1|   |1| |0|    |0| |1111|     |1|     |1|  ")
print("|1|       |1|    |1|       |1|       |1| |1|   |1|   |1| |0|    |0| |1|  |1|   |1|     |1|  ")
print("|1|       |1|    |1| |1|   |1| |1|   |1|  |1| |1|1| |1|   |0|  |0|  |1|   |1|  |1|    |1|   ") 
print("|1|       |1|    |1| |1111111| |1111111|   |11|   |11|     |0000|   |1|    |1| |111111|\n     ")



print("                                         |1|    |1|    |11|    |1|\     |1|    |11|      |111111|    |11111111| |1111111|    ")
print("                                         |1|\  /|1|   |1||1|   |1|\\    |1|   |1||1|    |1|     |1|  |1|        |1|   |1|    ")
print("                                         |1| \/ |1|  |1|  |1|  |1| \\   |1|  |1|  |1|  |1|           |1|        |1|  |1|     ")
print("                                         |1|    |1| |11111111| |1|  \\  |1| |11111111| |1|   |11111| |11111111| |1111|       ")
print("                                         |1|    |1| |1|    |1| |1|   \\ |1| |1|    |1| |1|       |1| |1|        |1|  |1|     ")
print("                                         |1|    |1| |1|    |1| |1|    \\|1| |1|    |1|  |1|     |1|  |1|        |1|   |1|    ")
print("                                         |1|    |1| |1|    |1| |1|     \|1| |1|    |1|   |111111|    |11111111| |1|    |1|\n ")

while True:
    try:
        sql_pass=stdiomask.getpass(prompt='Enter your MYSQL Password: ', mask='*')
        connection=mysql.connector.connect(user="root",password=""+sql_pass+"",host="localhost",database="password_manager")
        mycur=connection.cursor()
        break
    except:
        input("Sorry Access Denied !!!")
#######MAIN MENU#########
while True:
    os.system("cls")
    print("***Welcome To Password Manager***\n")
    print("Main Menu")
    print("\n1.Create Your Account")
    print("2.Add your Passwords and Datas")
    print("3.View/Update/Reset your Password")
    print("4.Save Datas to Text File")
    print("5.Info about Password Manager")
    print("6.Help Desk")
    print("7.Exit")   
    try:     
        user_choice=int(input("Enter your Choice: "))
        #Main

        #Main Choice1
        if user_choice==1:
            check_choice=("select user_choice=1 from pass_db")    
            mycur.execute(check_choice)
            check=mycur.fetchall()
            if check==[(1,)]:
                print("Password Alredy Created You can now Directly Log In")
                input("Press Enter To Continue")
                print("\n########################################################################")
            else:   
                create_password=stdiomask.getpass(prompt='Create your Password: ', mask='*')
                pass_db=("""INSERT INTO pass_db(user_choice, password) values (1,'%s')"""%create_password)
                mycur.execute(pass_db)
                connection.commit()
                #connection.close()
                print("Thank You for Choosing Password Manager\nYour Password for Password Manager has been Created")
                input("Press Enter To Continue")
                print("\n########################################################################")
        
        #Main Choice2
        elif user_choice==2:
            mycur.execute("select *from pass_db")
            pre_check=mycur.fetchall()
            pre_check_data=len(pre_check)
            if pre_check_data==0:
                print("Please Create Password to Add Passwords and Datas")
                print("\n########################################################################")
                input("Press Enter To Continue")
                print("\n########################################################################")

            else:
                password=stdiomask.getpass(prompt='Enter the Password: ', mask='*')
                pass_db=("""INSERT INTO pass_db(user_choice, password) values (3,'%s')"""%password)
                mycur.execute(pass_db)
                
                ori_pass=("select password from pass_db where user_choice=1")
                check_pass=("select password from pass_db where user_choice=3")
                mycur.execute(check_pass)
                data1=mycur.fetchall()
                mycur.execute(ori_pass)
                data=mycur.fetchall()
                if data==data1:
                    print("Sucessfully Loged In")
                    mycur.execute("delete from pass_db where user_choice=3")
            #After Log In
                    while True:
                        os.system("cls") 
                        print("1.Add your Passwords of Social Media")
                        print("2.Add your Passwords of Internet Banking Accounts")
                        print("3.Add your Bank Details")
                        print("4.Add your Purchase Cards")
                        print("5.Back")
                        try:
                            add_choice=int(input("Select your option: "))
                    ##SUBCHOICE1
                            if add_choice==1:
                                while True:
                                    os.system("cls")
                                    try:
                                        repeat=int(input("Enter How Many Accounts to be Added in Social Media Management\n(Only 5 Times per run Recommanded)"))
                                        print("Fill Each Option with Correct Information ")
                                        print("########################################################################")
                                        for i in range(repeat):
                                            mycur.execute("select *from social_media_management")
                                            row_no=mycur.fetchall()
                                            sno=len(row_no)+1                             
                                            sname=input("Enter Your Social Media Name: ")
                                            susername=input("Enter Your "+sname+" Username: ")
                                            spassword=input("Enter Your "+sname+" Password: ")
                                            s2fa=input("If 2FA Authendication is Enabled (Optional): ")
                                            snotes=input("You can add Aditional Information if any (optional): ")
                                                    
                                            print("########################################################################")        

                                ##SQl CONNECTION##
                                            add_social=("""INSERT INTO social_media_management(sno, name, username, password, 2fa, notes) values ('%s','%s','%s','%s','%s','%s')"""%(sno, sname, susername, spassword, s2fa, snotes))
                                            mycur.execute(add_social)
                                        connection.commit()
                                        #connection.close()
                                        print("Your Password has been Sucessfully saved in Database as given,\nThank You Have a Nice Day :)")
                                        input("Press Enter To Continue")
                                        print("########################################################################")
                                        break
                                        
                                        
                                        
                                    except ValueError:
                                        print("Enter Only Integer, Invalid Option")
                                        input("Press Enter To Continue")
                                        

                    ##SUBCHOICE2
                                    
                            elif add_choice==2:
                                while True:
                                    os.system("cls") 
                                    try:
                                        repeat1=int(input("Enter How Many Accounts to be Added in Internet Banking Management\n(Only 5 Times per run Recommanded)"))

                                        print("Fill Each Option with Correct Information ")
                                        print("########################################################################")
                                        for i in range(repeat1):
                                            mycur.execute("select *from inter_banking")
                                            row_no1=mycur.fetchall()
                                            sno=len(row_no1)+1
                                            bname=input("Enter Your Bank Name: ")
                                            busername=input("Enter Your "+bname+" Username: ")
                                            bpassword=input("Enter Your "+bname+" Password: ")
                                            btrans_pass=input("Enter Your "+bname+" Transaction Password (Optional): ")
                                            while True:
                                                try:
                                                    breg_mob=int(input("Enter Your "+bname+" Registered Mobile Number (Optional): "))
                                                    break
                                                except ValueError:
                                                    print("Enter Only Integer")
                                                    input("Press Any Key to ReEnter")
                                            bnotes=input("You can add Aditional Information if any (optional): ")
                                            print("########################################################################")
                                    
                                                
                            ##SQl CONNECTION##
                                            add_inter_bank=("""INSERT INTO inter_banking(sno, bname, username, password, transaction_password, register_mobile, notes) values ('%s','%s','%s','%s','%s','%s','%s')"""
                                                             %(sno, bname, busername, bpassword, btrans_pass, str(breg_mob), bnotes))
                                            mycur.execute(add_inter_bank)
                                        connection.commit()
                                        #connection.close()
                                        print("Your Password has been Sucessfully saved in Database as given,\nThank You Have a Nice Day :)")
                                        input("Press Enter To Continue")                                    
                                        print("\n########################################################################")
                                        break
                        
                                    except ValueError:
                                            print("Enter Only Integer, Invalid Option")
                                            input("Press Enter To Continue")
                ##SUBCHOICE3
                                    
                            elif add_choice==3:
                                while True:
                                    os.system("cls") 
                                    try:
                                        repeat2=int(input("Enter How Many Accounts to be Added in Bank Details Management\n(Only 5 Times per run Recommanded)"))

                                        print("Fill Each Option with Correct Information ")
                                        print("########################################################################")
                                        for i in range(repeat2):
                                            mycur.execute("select *from bank_details")
                                            row_no2=mycur.fetchall()
                                            sno=len(row_no2)+1
                                            b_name=input("Enter Bank Name: ")
                                            b_hold=input("Enter Account Holder Name: ")
                                            while True:
                                                try:
                                                    b_number=int(input("Enter "+b_name+" Account Number: "))
                                                    break
                                                except ValueError:
                                                    print("Enter Only Integer, Invalid Input")
                                                    input("Press Enter To Continue")
                                            b_ifsc=input("Enter "+b_name+" IFSC Number: ")
                                            b_branch=input("Enter "+b_name+" Branch Name: ")
                                            while True:
                                                try:
                                                    b_regmob=int(input("Enter "+b_name+" Registered Mobile Number: "))
                                                    break
                                                except ValueError:
                                                    print("Enter Only Integer, Invalid Input")
                                                    input("Press Enter To Continue")
                                            b_regmail=input("Enter "+b_name+" Registered Email Id (Optional): ")
                                            while True:
                                                try:
                                                    b_cusno=int(input("Enter "+b_hold+"'s Customer Number (Optional): "))
                                                    break
                                                except ValueError:
                                                    print("Enter Only Integer, Invalid Input")
                                                    input("Press Enter To Continue")
                                            b_cif=input("Enter "+b_hold+"'s CIF Number (Optional): ")
                                            b_notes=input("You can add Aditional Information if any (optional): ")
                                            print("########################################################################")
                                                
                            ##SQl CONNECTION##
                                            add_bank_details=("""INSERT INTO bank_details
                        (sno, bname, acc_holder, acc_number, ifsc_number, branch_name, register_mobile, register_email, customer_number, cif_number, notes) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
                                                            %(sno, b_name, b_hold, str(b_number), b_ifsc, b_branch, str(b_regmob), b_regmail, str(b_cusno), b_cif, b_notes))
                                            mycur.execute(add_bank_details)
                                        connection.commit()
                                        #connection.close()
                                        print("Your Bank Account Details has been Sucessfully saved in Database as given,\nThank You Have a Nice Day :)")
                                        input("Press Enter To Continue")
                                        print("\n########################################################################")
                                        break
                                    except ValueError:
                                            print("Enter Only Integer, Invalid Option")
                                            input("Press Enter To Continue")

                    ##SUBCHOICE4
                                    
                            elif add_choice==4:
                                while True:
                                    os.system("cls") 
                                    try:
                                        repeat3=int(input("Enter How Many Cards to be Added in Cards Management\n(Only 5 Times per run Recommanded)"))

                                        print("Fill Each Option with Correct Information ")
                                        print("########################################################################")
                                        for i in range(repeat3):
                                            mycur.execute("select *from save_cards")
                                            row_no3=mycur.fetchall()
                                            sno=len(row_no3)+1                    
                                            cpname=input("Enter Your Card Provider Name: ")
                                            chold=input("Enter Card Holder Name: ")
                                            ctype=input("Enter Card Type (Visa/MasterCard/Rupay/GiftCard/Other): ")
                                            while True:
                                                try:
                                                    cnumber=int(input("Enter Card Number: "))
                                                    break
                                                except ValueError:
                                                    print("Enter Only Integer, Invalid Input")
                                                    input("Press Enter To Continue")
                                            cexpiry=input("Enter Card Expiry Date (optional): ")
                                            while True:
                                                try:
                                                    ccvv=int(input("Enter Card CVV NO (optional): "))
                                                    break
                                                except ValueError:
                                                    print("Enter Only Integer, Invalid Input")
                                                    input("Press Enter To Continue")
                                            while True:
                                                try:
                                                    cregmob=int(input("Enter Card Registered Mobile Number (optional): "))
                                                    break
                                                except ValueError:
                                                    print("Enter Only Integer, Invalid Input")
                                                    input("Press Enter To Continue")
                                            cnotes=input("You can add Aditional Information if any(optional): ")                    
                                            print("########################################################################")
                                        
                                                
                            ##SQl CONNECTION##
                                            save_cards=("""INSERT INTO save_cards
                        (sno, card_provider, card_holder, card_type, card_number, card_expiry, card_cvv, card_register_mobile, notes) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
                                                            %(sno, cpname, chold, ctype, str(cnumber), cexpiry, str(ccvv), str(cregmob), cnotes))
                                            mycur.execute(save_cards)
                                        connection.commit()
                                        #connection.close()
                                        print("Your Cards has been Sucessfully saved in Database as given,\nThank You Have a Nice Day :)")
                                        input("Press Enter To Continue")
                                        break
                                    except ValueError:
                                            print("Enter Only Integer, Invalid Option")
                                            input("Press Enter To Continue")
                            elif add_choice==5:
                                break
                            else:
                                print("Wrong Option :( ")
                                input("Press Enter To Continue")
                                print("\n########################################################################")
                                    
                        except ValueError:
                            print("Enter Only Integer, Invalid Option")
                            input("Press Enter To continue")
                else:
                    print("Sorry!!Access Denied")
                    mycur.execute("delete from pass_db where user_choice=3")        
                    connection.commit()
                    #connection.close()
                    input("Press Enter To Continue")
                    print("\n########################################################################")
                
        #Main Choice3

        elif user_choice==3:
            mycur.execute("select *from pass_db")
            pre_check=mycur.fetchall()
            pre_check_data=len(pre_check)
            if pre_check_data==0:
                print("Please Create Password to View/Update/Reset your Datas")
                print("\n########################################################################")
                input("Press Enter To Continue")
                print("\n########################################################################")

            else:
                password=stdiomask.getpass(prompt='Enter the Password: ', mask='*')
                pass_db=("""INSERT INTO pass_db(user_choice, password) values (3,'%s')"""%password)
                mycur.execute(pass_db)

                ori_pass=("select password from pass_db where user_choice=1")
                check_pass=("select password from pass_db where user_choice=3")
                mycur.execute(check_pass)
                data1=mycur.fetchall()
                mycur.execute(ori_pass)
                data=mycur.fetchall()
                if data==data1:
                    print("Sucessfully Loged In")
                    mycur.execute("delete from pass_db where user_choice=3")
                                  
                    while True:
                        os.system("cls")
                        print("1.View\n2.Update Datas\n3.Delete Accounts\n4.Backup and Reset\n5.Back")
                        try:
                            up_view=int(input("Select your Operation: "))
                            if up_view==1:         
                                while True:
                                    os.system("cls")
                                    print('1.Social Media Accounts\n2.Internet Banking Accounts\n3.Bank Details\n4.Saved Cards\n5.Back')
                                    try:
                                        tab_sele=int(input("Choose the Table that you want to View: "))
                                            
                                ##view_table_section###
                                        if tab_sele==1:
                                            mycur.execute("select name, username, password, 2fa, notes from social_media_management")
                                            social_media_data=mycur.fetchall()
                                            print((tabulate(social_media_data, headers=["Social Media Name","Username","Password","2FA","Notes"], tablefmt="psql")))
                                            input("Press Enter To Continue")
                                            
                                        elif tab_sele==2:
                                            mycur.execute("select bname, username, password, transaction_password, register_mobile, notes from inter_banking")
                                            inter_bank_data=mycur.fetchall()
                                            print((tabulate(inter_bank_data, headers=["Bank Name","Username","Password","Transaction Password","Mobile Number","Notes"], tablefmt="psql")))
                                            input("Press Enter To Continue")
                                            
                                        elif tab_sele==3:
                                            mycur.execute("select bname, acc_holder, acc_number, ifsc_number, branch_name, register_mobile, register_email, customer_number, cif_number, notes from bank_details")
                                            bank_data=mycur.fetchall()
                                            print((tabulate(bank_data, headers=
                                                            ["Bank Name","Acc Holder Name","Acc Number","IFSC Code","Branch Name","Mobile Number","Email ID","Customer Number","CIF Number","Notes"], tablefmt="psql")))
                                            input("Press Enter To Continue")
                                            
                                        elif tab_sele==4:
                                            mycur.execute("select card_provider, card_holder, card_type, card_number, card_expiry, card_cvv, card_register_mobile, notes from save_cards")
                                            card_data=mycur.fetchall()
                                            print((tabulate(card_data, headers=
                                                                ["Provider Name","Holder Name","Card Type","Card Number","Expiry Data","CVV Number","Mobile Number","Notes"], tablefmt="psql")))
                                            input("Press Enter To Continue")
                                            
                                        elif tab_sele==5:
                                            break
                                        else:
                                            print("Wrong Option :(")
                                            input("Press Enter To Continue")
                                                
                                    except ValueError:
                                        print("Enter Only Integer, Invalid Option")
                                        input("Press Enter To continue")
                                   
                            
                                
                    ##update_table_section###
                            elif up_view==2:
                                while True:
                                    os.system("cls")
                                    print('1.Social Media Accounts\n2.Internet Banking Accounts\n3.Bank Details\n4.Saved Cards\n5.Back')
                                    try:
                                        tab_sele=int(input("Choose the Table that you want to Replace Datas: "))
                                        if tab_sele==1:
                                            mycur.execute("select *from social_media_management")
                                            social_media_data=mycur.fetchall()
                                            print((tabulate(social_media_data, headers=["Altering\nNumber","name","username","password","2fa","notes"], tablefmt="psql")))
                                            print("\n########################################################################")
                                            user_col=int(input("How many updates do you want to perform?:"))
                                            for i in range(user_col):
                                                col_name=input("Enter Column Name (*Note Case Sensitive): ")
                                                while True:
                                                    try:
                                                        alter_col=int(input("Enter Altering Number of your Updating Row: "))
                                                        break
                                                    except ValueError:
                                                        print("Enter Only Integer, Invalid Input")
                                                        input("Press Enter To Continue")
                                                update_to=input("Enter data what has to be Updated: ")

                                                rep=("update social_media_management set "+col_name+"='"+update_to+"' where sno="+str(alter_col)+";")
                                                mycur.execute(rep)
                                                print("\n########################################################################")
                                            print("Sucessfully Updated in Database as given,\nThank You Have a Nice Day :)")
                                            print("########################################################################")
                                            print("\n=======New Table=======")
                                                
                                            mycur.execute("select name, username, password, 2fa, notes from social_media_management")
                                            social_media_data=mycur.fetchall()
                                            print((tabulate(social_media_data, headers=["Social Media Name","Username","Password","2FA","Notes"], tablefmt="psql")))                  
                                            connection.commit()
                                            #connection.close()
                                            input("Press Enter To Continue")
                                            print("\n########################################################################")

                                        elif tab_sele==2:
                                            mycur.execute("select *from inter_banking")
                                            inter_bank_data=mycur.fetchall()
                                            print((tabulate(inter_bank_data, headers=["Altering\nNumber","bname","username","password","transaction_password","register_mobile","notes"], tablefmt="psql")))                
                                            print("\n########################################################################")
                                            user_col=int(input("How many updates do you want to perform?:"))
                                            for i in range(user_col):
                                                col_name=input("Enter Column Name (*Note Case Sensitive): ")
                                                while True:
                                                    try:
                                                        alter_col=int(input("Enter Altering Number of your Updating Row: "))
                                                        break
                                                    except ValueError:
                                                        print("Enter Only Integer, Invalid Input")
                                                        input("Press Enter To Continue")
                                                update_to=input("Enter data what has to be Updated: ")

                                                rep=("update inter_banking set "+col_name+"='"+update_to+"' where sno="+str(alter_col)+";")
                                                mycur.execute(rep)
                                                print("\n########################################################################")
                                            print("Sucessfully Updated in Database as given,\nThank You Have a Nice Day :)")
                                            print("########################################################################")
                                            print("\n=======New Table=======")
                                            mycur.execute("select bname, username, password, transaction_password, register_mobile, notes from inter_banking")
                                            inter_bank_data=mycur.fetchall()
                                            print((tabulate(inter_bank_data, headers=["Bank Name","Username","Password","Transaction Password","Mobile Number","Notes"], tablefmt="psql")))                                  
                                            connection.commit()
                                            #connection.close()
                                            input("Press Enter To Continue")
                                            print("\n########################################################################")

                                        elif tab_sele==3:
                                            mycur.execute("select *from bank_details")
                                            bank_data=mycur.fetchall()
                                            print((tabulate(bank_data, headers=
                                                            ["Altering\nNumber","bname","acc_holder","acc_number","ifsc_number","branch_name","register_mobile","register_email","customer_number","cif_number","notes"], tablefmt="psql")))
                                            print("\n########################################################################")
                                            user_col=int(input("How many updates do you want to perform?:"))
                                            for i in range(user_col):
                                                col_name=input("Enter Column Name (*Note Case Sensitive): ")
                                                while True:
                                                    try:
                                                        alter_col=int(input("Enter Altering Number of your Updating Row: "))
                                                        break
                                                    except ValueError:
                                                        print("Enter Only Integer, Invalid Input")
                                                        input("Press Enter To Continue")
                                                update_to=input("Enter data what has to be Updated: ")

                                                rep=("update bank_details set "+col_name+"='"+update_to+"' where sno="+str(alter_col)+";")
                                                mycur.execute(rep)
                                                print("\n########################################################################")
                                            print("Sucessfully Updated in Database as given,\nThank You Have a Nice Day :)")
                                            print("########################################################################")
                                            print("\n=======New Table=======")
                                            mycur.execute("select bname, acc_holder, acc_number, ifsc_number, branch_name, register_mobile, register_email, customer_number, cif_number, notes from bank_details")
                                            bank_data=mycur.fetchall()
                                            print((tabulate(bank_data, headers=
                                                            ["Bank Name","Acc Holder Name","Acc Number","IFSC Code","Branch Name","Mobile Number","Email ID","Customer Number","CIF Number","Notes"], tablefmt="psql")))
                                            connection.commit()
                                            #connection.close()
                                            input("Press Enter To Continue")
                                            print("\n########################################################################")

                                        elif tab_sele==4:
                                            mycur.execute("select *from save_cards")
                                            card_data=mycur.fetchall()
                                            print((tabulate(card_data, headers=
                                                                ["Altering\nNumber","card_provider","card_holder","card_type","card_number","card_expiry","card_cvv","card_register_mobile","notes"], tablefmt="psql")))
                                            print("\n########################################################################")
                                            user_col=int(input("How many updates do you want to perform?:"))
                                            for i in range(user_col):
                                                col_name=input("Enter Column Name (*Note Case Sensitive): ")
                                                while True:
                                                    try:
                                                        alter_col=int(input("Enter Altering Number of your Updating Row: "))
                                                        break
                                                    except ValueError:
                                                        print("Enter Only Integer, Invalid Input")
                                                        input("Press Enter To Continue")
                                                update_to=input("Enter data what has to be Updated: ")

                                                rep=("update save_cards set "+col_name+"='"+update_to+"' where sno="+str(alter_col)+";")
                                                mycur.execute(rep)
                                                print("\n########################################################################")
                                            print("Sucessfully Updated in Database as given,\nThank You Have a Nice Day :)")
                                            print("########################################################################")
                                            print("\n=======New Table=======")
                                            mycur.execute("select card_provider, card_holder, card_type, card_number, card_expiry, card_cvv, card_register_mobile, notes from save_cards")
                                            card_data=mycur.fetchall()
                                            print((tabulate(card_data, headers=
                                                                ["Provider Name","Holder Name","Card Type","Card Number","Expiry Data","CVV Number","Mobile Number","Notes"], tablefmt="psql")))
                                            connection.commit()
                                            #connection.close()
                                            input("Press Enter To Continue")
                                            print("\n########################################################################")
                                        elif tab_sele==5:
                                            break
                                        else:
                                            print("Wrong Option :(")
                                            input("Press Enter To Continue")
                                    except ValueError:
                                        print("Enter Only Integer, Invalid Option")
                                        input("Press Enter To continue")
                                    
                    ##delete_row_section##
                            elif up_view==3:
                                while True:
                                    os.system("cls")
                                    print('1.Social Media Accounts\n2.Internet Banking Accounts\n3.Bank Details\n4.Saved Cards\n5.Back')
                                    try:                          
                                        tab_sele=int(input("Choose the Table that you want to Delete Datas: "))
                                        if tab_sele==1:
                                            mycur.execute("select *from social_media_management")
                                            social_media_data=mycur.fetchall()
                                            print((tabulate(social_media_data, headers=["Altering\nNumber","Social Media Name","Username","Password","2FA","Notes"], tablefmt="psql")))
                                            print("\n########################################################################")
                                            user_col=int(input("How many Accounts to be Deleted?:"))
                                            for i in range(user_col):
                                                while True:
                                                    try:
                                                        alter_col=int(input("Enter Altering Number of your Deleting Row: "))
                                                        break
                                                    except ValueError:
                                                        print("Enter Only Integer, Invalid Input")
                                                        input("Press Enter To Continue")
                                                rep=("update social_media_management set name='NULL', username='NULL', password='NULL', 2fa='NULL', notes='NULL' where sno="+str(alter_col)+";")
                                                mycur.execute(rep)
                                                print("########################################################################")
                                            print("Sucessfully Deleted in Database as given,\nThank You Have a Nice Day :)")
                                            print("########################################################################")
                                            print("\n=======New Table=======")
                                                
                                            mycur.execute("select name, username, password, 2fa, notes from social_media_management")
                                            social_media_data=mycur.fetchall()
                                            print((tabulate(social_media_data, headers=["Social Media Name","Username","Password","2FA","Notes"], tablefmt="psql")))                  
                                            connection.commit()
                                            #connection.close()
                                            input("Press Enter To Continue")
                                            print("\n########################################################################")
                                        elif tab_sele==2:
                                            mycur.execute("select *from inter_banking")
                                            inter_bank_data=mycur.fetchall()
                                            print((tabulate(inter_bank_data, headers=["Altering\nNumber","Bank Name","Username","Password","Transaction Password","Mobile Number","Notes"], tablefmt="psql")))                
                                            print("\n########################################################################")
                                            user_col=int(input("How many Accounts to be Deleted?:"))
                                            for i in range(user_col):
                                                while True:
                                                    try:
                                                        alter_col=int(input("Enter Altering Number of your Deleting Row: "))
                                                        break
                                                    except ValueError:
                                                        print("Enter Only Integer, Invalid Input")
                                                        input("Press Enter To Continue")                  
                                                rep=("update inter_banking set bname='NULL', username='NULL', password='NULL', transaction_password='NULL', register_mobile='NULL', notes='NULL' where sno="+str(alter_col)+";")
                                                mycur.execute(rep)
                                                print("########################################################################")
                                            print("Sucessfully Deleted in Database as given,\nThank You Have a Nice Day :)")
                                            print("########################################################################")
                                            print("\n=======New Table=======")

                                            mycur.execute("select bname, username, password, transaction_password, register_mobile, notes from inter_banking")
                                            inter_bank_data=mycur.fetchall()
                                            print((tabulate(inter_bank_data, headers=["Bank Name","Username","Password","Transaction Password","Mobile Number","Notes"], tablefmt="psql")))                  
                                            connection.commit()
                                            #connection.close()
                                            input("Press Enter To Continue")
                                        elif tab_sele==3:
                                            mycur.execute("select *from bank_details")
                                            bank_data=mycur.fetchall()
                                            print((tabulate(bank_data, headers=
                                                            ["Altering\nNumber","Bank Name","Acc Holder Name","Acc Number","IFSC Code","Branch Name","Mobile Number","Email ID","Customer Number","CIF Number","Notes"], tablefmt="psql")))
                                            print("\n########################################################################")
                                            user_col=int(input("How many Accounts to be Deleted?:"))
                                            for i in range(user_col):
                                                while True:
                                                    try:
                                                        alter_col=int(input("Enter Altering Number of your Deleting Row: "))
                                                        break
                                                    except ValueError:
                                                        print("Enter Only Integer, Invalid Input")
                                                        input("Press Enter To Continue")                  
                                                rep=("update bank_details set bname='NULL', acc_holder='NULL', acc_number='NULL', ifsc_number='NULL', branch_name='NULL', register_mobile='NULL', register_email='NULL', customer_number='NULL', cif_number='NULL', notes='NULL' where sno="+str(alter_col)+";")
                                                mycur.execute(rep)
                                                print("########################################################################")
                                            print("Sucessfully Deleted in Database as given,\nThank You Have a Nice Day :)")
                                            print("########################################################################")
                                            print("\n=======New Table=======")

                                            mycur.execute("select bname, acc_holder, acc_number, ifsc_number, branch_name, register_mobile, register_email, customer_number, cif_number, notes from bank_details")
                                            bank_data=mycur.fetchall()
                                            print((tabulate(bank_data, headers=
                                                            ["Bank Name","Acc Holder Name","Acc Number","IFSC Code","Branch Name","Mobile Number","Email ID","Customer Number","CIF Number","Notes"], tablefmt="psql")))
                                            connection.commit()
                                            #connection.close()
                                            input("Press Enter To Continue")
                                            print("\n########################################################################")
                                        elif tab_sele==4:
                                            mycur.execute("select *from save_cards")
                                            card_data=mycur.fetchall()
                                            print((tabulate(card_data, headers=
                                                                ["Altering\nNumber","Provider Name","Holder Name","Card Type","Card Number","Expiry Data","CVV Number","Mobile Number","Notes"], tablefmt="psql")))
                                            print("\n########################################################################")
                                            user_col=int(input("How many Accounts to be Deleted?:"))
                                            for i in range(user_col):
                                                while True:
                                                    try:
                                                        alter_col=int(input("Enter Altering Number of your Deleting Row: "))
                                                        break
                                                    except ValueError:
                                                        print("Enter Only Integer, Invalid Input")
                                                        input("Press Enter To Continue")                 
                                                rep=("update save_cards set card_provider='NULL', card_holder='NULL', card_type='NULL', card_number='NULL', card_expiry='NULL', card_cvv='NULL', card_register_mobile='NULL', notes='NULL' where sno="+str(alter_col)+";")
                                                mycur.execute(rep)
                                                print("########################################################################")
                                            print("Sucessfully Deleted in Database as given,\nThank You Have a Nice Day :)")
                                            print("########################################################################")
                                            print("\n=======New Table=======")

                                            mycur.execute("select card_provider, card_holder, card_type, card_number, card_expiry, card_cvv, card_register_mobile, notes from save_cards")
                                            card_data=mycur.fetchall()
                                            print((tabulate(card_data, headers=
                                                                ["Provider Name","Holder Name","Card Type","Card Number","Expiry Data","CVV Number","Mobile Number","Notes"], tablefmt="psql")))                  
                                            connection.commit()
                                            #connection.close()
                                            input("Press Enter To Continue")
                                            print("\n########################################################################")
                                        elif tab_sele==5:
                                            break
                                        else:
                                            print("Wrong Option :(")
                                            input("Press Enter To Continue")
                                            print("\n########################################################################")
                                    except ValueError:
                                        print("Enter Only Integer, Invalid Option")
                                        input("Press Enter To continue")

                                                                                 
                    ##reset_pass_db_section##
                                    
                            elif up_view==4:
                                while True:
                                    os.system("cls")
                                    print("1.Reset Password Manager Password")
                                    print("2.Backup and Reset Password Manager")
                                    print("3.Back")
                                    try:
                                        bac_reset=int(input("Enter Your Option: "))
                                        if bac_reset==1:
                                            mycur.execute("delete from pass_db where user_choice=1")            
                                            print("Sucessfully Reseted :)")
                                            print("You can now Create New Password in 'Create Password' Section in Main Menu")
                                            connection.commit()
                                            #connection.close()
                                            input("Press Enter To Continue")
                                            print("\n########################################################################")
                                        elif bac_reset==2:
                                            print("bakuping your datas........\ncopying datas.........")

                                            time=datetime.datetime.now()
                                                


                                                    
                                            table=('\n'+tabulate([[1, 'Social Media Accounts'], [2, 'Internet Banking Accounts'], [3, 'Bank Details'], [4, 'Saved Cards']],
                                                                 headers=['Number of Tables', 'Tables you can use'], tablefmt='psql'))


                                            mycur.execute("select name, username, password, 2fa, notes from social_media_management")
                                            social_media_data=mycur.fetchall()
                                            social_data=((tabulate(social_media_data, headers=["Social Media Name","Username","Password","2FA","Notes"], tablefmt="psql")))
                                                        
                                            mycur.execute("select bname, username, password, transaction_password, register_mobile, notes from inter_banking")
                                            inter_bank_data=mycur.fetchall()
                                            inter_data=((tabulate(inter_bank_data, headers=["Bank Name","Username","Password","Transaction Password","Mobile Number","Notes"], tablefmt="psql")))
                                                    
                                            mycur.execute("select bname, acc_holder, acc_number, ifsc_number, branch_name, register_mobile, register_email, customer_number, cif_number, notes from bank_details")
                                            bank_data=mycur.fetchall()
                                            bank_details=((tabulate(bank_data, headers=["Bank Name","Acc Holder Name","Acc Number","IFSC Code","Branch Name","Mobile Number","Email ID","Customer Number","CIF Number","Notes"], tablefmt="psql")))
                                                
                                            mycur.execute("select card_provider, card_holder, card_type, card_number, card_expiry, card_cvv, card_register_mobile, notes from save_cards")
                                            card_data=mycur.fetchall()
                                            save_cards=((tabulate(card_data, headers=["Provider Name","Holder Name","Card Type","Card Number","Expiry Data","CVV Number","Mobile Number","Notes"], tablefmt="psql")))

                                            test_data=open("Password Manager Backup "+time.strftime("%d %B %Y")+".txt","w")
                                            test_data.write("============================================================================TABLE===================================================================\n")
                                            test_data.writelines(table)
                                            test_data.writelines("\n==============================================================SOCIAL MEDIA ACCOUNTS=================================================================\n")
                                            test_data.writelines(social_data)
                                            test_data.writelines("\n============================================================INTERNET BANKING ACCOUNTS===============================================================\n")
                                            test_data.writelines(inter_data)
                                            test_data.writelines("\n==================================================================BANK DETAILS======================================================================\n")
                                            test_data.writelines(bank_details)
                                            test_data.writelines("\n===================================================================SAVED CARDS======================================================================\n")
                                            test_data.writelines(save_cards)
                                            test_data.close()
                                            print("Backuped your Datas to Text File ('Password Manager Backup"+time.strftime("%d %B %Y")+".txt') Sucessfully,")

                                            print("Reseting your tables...." )
                                            mycur.execute("drop table social_media_management")
                                            print("Reseting your tables...." )
                                            mycur.execute("drop table inter_banking")
                                            print("Reseting your tables...." )
                                            mycur.execute("drop table bank_details")
                                            print("Reseting your tables...." )
                                            mycur.execute("drop table save_cards")
                                            print("Reseting your tables...." )
                                            mycur.execute("drop table pass_db")                                              
                                            print("creating tables......")
                                            print("creating table pass_db...........")
                                            mycur.execute("create table pass_db(user_choice varchar(30), password varchar(30))")
                                            print("creating table social_media_management...........")
                                            mycur.execute("create table social_media_management(sno varchar(30), name varchar(30), username varchar(30), password varchar(30), 2fa varchar(30), notes varchar(30))")
                                            print("creating table inter_banking...........")
                                            mycur.execute("create table inter_banking(sno varchar(30), bname varchar(30), username varchar(30), password varchar(30), transaction_password varchar(30), register_mobile varchar(30), notes varchar(30))")
                                            print("creating table bank_details...........")
                                            mycur.execute("create table bank_details(sno varchar(30), bname varchar(30), acc_holder varchar(30), acc_number varchar(30), ifsc_number varchar(30), branch_name varchar(30), register_mobile varchar(30), register_email varchar(30), customer_number varchar(30), cif_number varchar(30), notes varchar(30))")
                                            print("creating table save_cards...........")
                                            mycur.execute("create table save_cards(sno varchar(30), card_provider varchar(30), card_holder varchar(30), card_type varchar(30), card_number varchar(30), card_expiry varchar(30), card_cvv varchar(30), card_register_mobile varchar(30), notes varchar(30))")
                                            print("Table Created Sucessfully")
                                            print("Reseted Sucessfully")
                                            input("Press Enter to Continue")
                                        elif bac_reset==3:
                                            break
                                        else:
                                            print("Wrong Option :(")
                                            input("Press Enter To Continue")
                                    except ValueError:
                                        print("Enter Only Integer, Invalid Option")
                                        input("Press Enter To continue")
                            elif up_view==5:
                                break
                                    
                            else:
                                print("Wrong Option :(")
                                input("Press Enter To Continue")
                        except ValueError:
                            print("Enter Only Integer, Invalid Option")
                            input("Press Enter To continue")
                            
                                                                   
                            
                else:
                    print("Sorry!!Access Denied")
                    mycur.execute("delete from pass_db where user_choice=3")        
                    connection.commit()
                    #connection.close()
                    input("Press Enter To Continue")
                    print("\n########################################################################")

        ##Main Choice4
        elif user_choice==4:
            mycur.execute("select *from pass_db")
            pre_check=mycur.fetchall()
            pre_check_data=len(pre_check)
            if pre_check_data==0:
                print("Please Create Password to Copy Datas")
                print("\n########################################################################")
                input("Press Enter To Continue")
                print("\n########################################################################")

            else:
                password=stdiomask.getpass(prompt='Enter the Password: ', mask='*')
                pass_db=("""INSERT INTO pass_db(user_choice, password) values (3,'%s')"""%password)
                mycur.execute(pass_db)

                ori_pass=("select password from pass_db where user_choice=1")
                check_pass=("select password from pass_db where user_choice=3")
                mycur.execute(check_pass)
                data1=mycur.fetchall()
                mycur.execute(ori_pass)
                data=mycur.fetchall()
                if data==data1:
                    print("Sucessfully Loged In")
                    mycur.execute("delete from pass_db where user_choice=3")
                    print("\n########################################################################")
                    print("copying datas.........")

                    time=datetime.datetime.now()
                


                    
                    table=('\n'+tabulate([[1, 'Social Media Accounts'], [2, 'Internet Banking Accounts'], [3, 'Bank Details'], [4, 'Saved Cards']],
                                    headers=['Number of Tables', 'Tables you can use'], tablefmt='psql'))


                    mycur.execute("select name, username, password, 2fa, notes from social_media_management")
                    social_media_data=mycur.fetchall()
                    social_data=((tabulate(social_media_data, headers=["Social Media Name","Username","Password","2FA","Notes"], tablefmt="psql")))
                        
                    mycur.execute("select bname, username, password, transaction_password, register_mobile, notes from inter_banking")
                    inter_bank_data=mycur.fetchall()
                    inter_data=((tabulate(inter_bank_data, headers=["Bank Name","Username","Password","Transaction Password","Mobile Number","Notes"], tablefmt="psql")))
                    
                    mycur.execute("select bname, acc_holder, acc_number, ifsc_number, branch_name, register_mobile, register_email, customer_number, cif_number, notes from bank_details")
                    bank_data=mycur.fetchall()
                    bank_details=((tabulate(bank_data, headers=["Bank Name","Acc Holder Name","Acc Number","IFSC Code","Branch Name","Mobile Number","Email ID","Customer Number","CIF Number","Notes"], tablefmt="psql")))
                
                    mycur.execute("select card_provider, card_holder, card_type, card_number, card_expiry, card_cvv, card_register_mobile, notes from save_cards")
                    card_data=mycur.fetchall()
                    save_cards=((tabulate(card_data, headers=
                                                ["Provider Name","Holder Name","Card Type","Card Number","Expiry Data","CVV Number","Mobile Number","Notes"], tablefmt="psql")))

                    test_data=open("Password Manager "+time.strftime("%d %B %Y")+".txt","w")
                    test_data.write("============================================================================TABLE===================================================================\n")
                    test_data.writelines(table)
                    test_data.writelines("\n==============================================================SOCIAL MEDIA ACCOUNTS=================================================================\n")
                    test_data.writelines(social_data)
                    test_data.writelines("\n============================================================INTERNET BANKING ACCOUNTS===============================================================\n")
                    test_data.writelines(inter_data)
                    test_data.writelines("\n==================================================================BANK DETAILS======================================================================\n")
                    test_data.writelines(bank_details)
                    test_data.writelines("\n===================================================================SAVED CARDS======================================================================\n")
                    test_data.writelines(save_cards)
                    test_data.close()
                    print("Copied your Datas to Text File ('Password Manager "+time.strftime("%d %B %Y")+".txt') Sucessfully,\nThank You Have a Nice Day :)")
                    input("Press Enter To Continue")
                    print("\n########################################################################")
                    
                else:
                    print("Sorry!!Access Denied")
                    mycur.execute("delete from pass_db where user_choice=3")        
                    connection.commit()
                    #connection.close()
                    input("Press Enter To Continue")
                    print("\n########################################################################")
    ##Main Choice5
        elif user_choice==5:
            print("We Provide you Secure Database \n\nwhere you can Manage Your\n-->Internet Banking\n-->Manage Your Bank Account Details\n-->Save Your Debit/Credit/Other Cards\n-->Your Social Media Accounts")
            input("Press Enter To Continue")
    ##Main Choice6        
        elif user_choice==6:
            print("Under Maintenance")
            input("Press Enter To Continue")
            
            
            print("\n########################################################################")
    ##Main Choice7
        elif user_choice==7:
            quit()
        else:
            print("Invalid Option")
            input("Press Enter to Continue")
    
    except ValueError:
        print("Enter Only Integer, Invalid Option")
        input("Press Enter To continue")                
                
                
                
        
                             
                        
                
                             
                
                    
                
                
                    
                
                
                    







    
    

        

        
                

    
    
        
        
    
    

    
        
        
