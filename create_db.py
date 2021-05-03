import sqlite3



def create_tables() :
    conn = sqlite3.connect('developpers.db')
    c = conn.cursor()

    create_developpers_query = """
        CREATE TABLE IF NOT EXISTS developpers (
            first_name text,
            last_name text,
            techno text,
            experience integer
        )
    """

    create_technos_query = """
        CREATE TABLE IF NOT EXISTS technos (
            name text,
            type text
        )
    """

    c.execute(create_developpers_query)
    c.execute(create_technos_query)

    conn.commit()
    conn.close()


    # c.execute("""UPDATE addresses SET
	# 	first_name = :first,
	# 	last_name = :last,
	# 	address = :address,
	# 	city = :city,
	# 	state = :state,
	# 	zipcode = :zipcode 

	# 	WHERE oid = :oid""",
	# 	{
	# 	'first': f_name_editor.get(),
	# 	'last': l_name_editor.get(),
	# 	'address': address_editor.get(),
	# 	'city': city_editor.get(),
	# 	'state': state_editor.get(),
	# 	'zipcode': zipcode_editor.get(),
	# 	'oid': record_id
	# 	})

    #c.execute("DELETE from addresses WHERE oid = " + delete_box.get())




def populate_tables() :
    conn = sqlite3.connect('developpers.db')
    c = conn.cursor()
    
    developpers = [
        ('alessio', 'rea', 'node.js', 0),
        ('mathieux', 'bordet', 'react', 10),
        ('julien', 'ducros', 'java', 5)
    ]
    insert_developpers_qry = """
        INSERT INTO developpers VALUES (?, ?, ?, ?)
    """
    c.executemany(insert_developpers_qry, developpers)

    create_technos_query = """
        CREATE TABLE IF NOT EXISTS technos (
            name text,
            type text
        )
    """
    insert_technos_qry = """
        INSERT INTO technos VALUES 
        ('node.js', 'web'),
        ('react native', 'mobile'),
        ('jave', 'web'),
        ('swift', 'mobile')
    """    
    c.execute(insert_technos_qry)

    conn.commit()
    conn.close()



def show_tables():

    c.execute("SELECT * FROM developpers WHERE first_name = 'alessio';" )
    results = c.fetchall()
    print(results)


    c.execute("SELECT * FROM technos;" )
    results = c.fetchall()
    print(results)

    conn.commit()
    conn.close()







if __name__ == "__main__":

    create_tables() 

    #populate_tables()

    #show_tables()





    
    



    


    




    
