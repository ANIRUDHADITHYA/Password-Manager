try:
    import stdiomask
    import mysql.connector
    while True:
        user_pass=stdiomask.getpass(prompt='Enter MYSQL Password: ', mask='*')
        connection=mysql.connector.connect(user="root",password=""+user_pass+"",host="localhost")
        while True:
            mycur=connection.cursor()
            print("\\\\checking for database")
            try:
                print("*****Make sure that you have installed MYSQL and runed 'requirements.cmd' once to run PASSWORD MANAGER******")
                mycur.execute("create database password_manager")
                print("creating database.............")
                print("Database Created Sucessfully")
                
                
            except Exception:
                connection1=mysql.connector.connect(user="root",password=""+user_pass+"",host="localhost",database="password_manager")
                mycur1=connection1.cursor()
                mycur1.execute("show tables")
                table_check1=mycur1.fetchall()
                table_check=[('bank_details',), ('inter_banking',), ('pass_db',), ('save_cards',), ('social_media_management',)]
                print("\\\\checking for tables")
                if table_check==table_check1:
                    print("Table Already Created")
                    input("Press any key to exit")
                    exit()
                else:
                    print("creating tables......")
                    print("creating table pass_db...........")
                    mycur1.execute("create table pass_db(user_choice varchar(30), password varchar(30))")
                    print("creating table social_media_management...........")
                    mycur1.execute("create table social_media_management(sno varchar(30), name varchar(30), username varchar(30), password varchar(30), 2fa varchar(30), notes varchar(30))")
                    print("creating table inter_banking...........")
                    mycur1.execute("create table inter_banking(sno varchar(30), bname varchar(30), username varchar(30), password varchar(30), transaction_password varchar(30), register_mobile varchar(30), notes varchar(30))")
                    print("creating table bank_details...........")
                    mycur1.execute("create table bank_details(sno varchar(30), bname varchar(30), acc_holder varchar(30), acc_number varchar(30), ifsc_number varchar(30), branch_name varchar(30), register_mobile varchar(30), register_email varchar(30), customer_number varchar(30), cif_number varchar(30), notes varchar(30))")
                    print("creating table save_cards...........")
                    mycur1.execute("create table save_cards(sno varchar(30), card_provider varchar(30), card_holder varchar(30), card_type varchar(30), card_number varchar(30), card_expiry varchar(30), card_cvv varchar(30), card_register_mobile varchar(30), notes varchar(30))")
                    print("Table Created Sucessfully")
                    print("*****Make sure that you have installed MYSQL and runed 'requirements.cmd' once to run PASSWORD MANAGER******")
                    input("Press any key to exit")
                exit()
except Exception:
    print("Modules not Found")
    print("*****Make sure that you have installed MYSQL and runed 'requirements.cmd' once to run PASSWORD MANAGER******")
    input("Press any key to exit")
    exit()
        
    
    
    
